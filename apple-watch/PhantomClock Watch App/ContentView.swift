import SwiftUI

// MARK: - Physics Constants
enum PhantomConfig {
    static let sweepSpeed: Double = 0.012
    static let trailSpd: Double = 0.008
    static let couplingSpd: Double = 0.045 // Deep trailing
    static let driftInterval: Double = 480.0 // 8 Minutes
}

// MARK: - State Manager
class PhantomClockState: ObservableObject {
    var hAngle: Double = 0
    var mAngle: Double = 0
    var hTrailAngle: Double = 0
    var mTrailAngle: Double = 0
    
    var rotH: Double = 0
    var rotM: Double = 0
    var rotS: Double = 0
    
    var hTargetAngle: Double = .random(in: 0..<2 * .pi)
    var mTargetAngle: Double = .random(in: 0..<2 * .pi)
    
    @Published var hDrifting: Bool = false
    @Published var mDrifting: Bool = false
    var colorPhase: Double = 0

    private var lastSecond: Int = -1
    private var shiftWorkItem: DispatchWorkItem?

    init() {
        hAngle = hTargetAngle
        mAngle = mTargetAngle
        hTrailAngle = hTargetAngle
        mTrailAngle = mTargetAngle
        scheduleShift(after: 10.0)
    }

    private func sweep(_ current: Double, _ target: Double, speed: Double) -> Double {
        var diff = (target - current).truncatingRemainder(dividingBy: 2 * .pi)
        if diff < -.pi { diff += 2 * .pi }
        if diff > .pi { diff -= 2 * .pi }
        return current + diff * speed
    }

    func scheduleShift(after delay: Double) {
        shiftWorkItem?.cancel()
        let item = DispatchWorkItem { [weak self] in self?.shiftReality() }
        shiftWorkItem = item
        DispatchQueue.main.asyncAfter(deadline: .now() + delay, execute: item)
    }

    func shiftReality() {
        let newH = Double.random(in: 0..<2 * .pi)
        var newM: Double
        repeat { newM = .random(in: 0..<2 * .pi) } while abs(newM - newH) < 1.2 // More separation
        
        withAnimation(.easeInOut(duration: 5.0)) { hDrifting = true }
        DispatchQueue.main.asyncAfter(deadline: .now() + 5.0) { [weak self] in
            self?.hTargetAngle = newH
            DispatchQueue.main.asyncAfter(deadline: .now() + 20.0) {
                withAnimation(.easeInOut(duration: 6.0)) { self?.hDrifting = false }
            }
        }

        let mDelay = 8.0 + .random(in: 0..<5)
        DispatchQueue.main.asyncAfter(deadline: .now() + mDelay) { [weak self] in
            withAnimation(.easeInOut(duration: 5.0)) { self?.mDrifting = true }
            DispatchQueue.main.asyncAfter(deadline: .now() + 5.0) {
                self?.mTargetAngle = newM
                DispatchQueue.main.asyncAfter(deadline: .now() + 20.0) {
                    withAnimation(.easeInOut(duration: 6.0)) { self?.mDrifting = false }
                }
            }
        }
        scheduleShift(after: PhantomConfig.driftInterval)
    }

    func update(to now: Date) {
        let cal = Calendar.current
        let h = cal.component(.hour, from: now)
        let m = cal.component(.minute, from: now)
        let s = cal.component(.second, from: now)

        let realH = (Double(h % 12) + Double(m)/60.0) / 12 * 2 * .pi
        let realM = (Double(m) + Double(s)/60.0) / 60 * 2 * .pi
        
        var targetH = hTargetAngle + realH
        var targetM = mTargetAngle + realM

        // Increased repulsion threshold (0.8 rads)
        let angleDiff = (targetH - targetM).truncatingRemainder(dividingBy: 2 * .pi)
        let normalizedDiff = abs(angleDiff < -.pi ? angleDiff + 2 * .pi : (angleDiff > .pi ? angleDiff - 2 * .pi : angleDiff))
        
        if normalizedDiff < 0.8 {
            let push = (0.8 - normalizedDiff) / 2
            targetH += (angleDiff > 0 ? push : -push)
            targetM += (angleDiff > 0 ? -push : push)
        }

        hAngle = sweep(hAngle, targetH, speed: PhantomConfig.sweepSpeed)
        mAngle = sweep(mAngle, targetM, speed: PhantomConfig.sweepSpeed)
        
        hTrailAngle = sweep(hTrailAngle, hAngle, speed: PhantomConfig.trailSpd)
        mTrailAngle = sweep(mTrailAngle, mAngle, speed: PhantomConfig.trailSpd)

        // Deeper Lag for hands
        rotH = sweep(rotH, hAngle, speed: PhantomConfig.couplingSpd)
        rotM = sweep(rotM, mAngle, speed: PhantomConfig.couplingSpd + 0.01)
        
        if s != lastSecond {
            let diff = (s - lastSecond + 60) % 60
            rotS += Double(diff) * (2 * .pi / 60.0)
            lastSecond = s
        }
        
        colorPhase += 0.005
    }
}

// MARK: - Main UI
struct ContentView: View {
    @StateObject private var state = PhantomClockState()
    
    var body: some View {
        TimelineView(.animation) { timeline in
            GeometryReader { geo in
                let w = geo.size.width
                let h = geo.size.height
                let center = CGPoint(x: w / 2, y: h / 2)
                
                // Rectangular Orbit Constraints
                let safeW = (w - geo.safeAreaInsets.leading - geo.safeAreaInsets.trailing) * 0.45
                let safeH = (h - geo.safeAreaInsets.top - geo.safeAreaInsets.bottom) * 0.45
                
                ZStack {
                    meshBackground(phase: state.colorPhase)
                        .ignoresSafeArea()
                    
                    Canvas { ctx, canvasSize in
                        state.update(to: timeline.date)
                        
                        // Rectangular Trails
                        drawTrail(ctx: ctx, center: center, angle: state.hTrailAngle, rx: safeW * 0.9, ry: safeH * 0.9, opacity: 0.12)
                        drawTrail(ctx: ctx, center: center, angle: state.mTrailAngle, rx: safeW * 1.1, ry: safeH * 1.1, opacity: 0.1)
                        
                        drawHands(ctx: ctx, center: center, rx: safeW, ry: safeH)
                    }
                    
                    labelGroup(state: state, size: max(w, h), rx: safeW, ry: safeH)
                    centerJewel(size: max(w, h))
                }
            }
        }
        .containerBackground(.black, for: .navigation)
        .toolbar(.hidden, for: .automatic)
        .edgesIgnoringSafeArea(.all)
    }
    
    @ViewBuilder
    private func meshBackground(phase: Double) -> some View {
        // Brighter & More Diverse Palette
        let c1 = Color(hue: (phase * 0.2).truncatingRemainder(dividingBy: 1.0), saturation: 0.9, brightness: 0.35)
        let c2 = Color(hue: (0.5 - phase * 0.15).truncatingRemainder(dividingBy: 1.0), saturation: 0.9, brightness: 0.3)
        let c3 = Color(hue: (0.8 + phase * 0.3).truncatingRemainder(dividingBy: 1.0), saturation: 0.8, brightness: 0.32)
        
        ZStack {
            Color.black
            RadialGradient(colors: [c1, .clear], center: .topLeading, startRadius: 0, endRadius: 300)
            RadialGradient(colors: [c2, .clear], center: .bottomTrailing, startRadius: 0, endRadius: 350)
            RadialGradient(colors: [c3, .clear], center: .center, startRadius: 50, endRadius: 280)
        }
        .blur(radius: 45)
    }

    @ViewBuilder
    private func labelGroup(state: PhantomClockState, size: CGFloat, rx: CGFloat, ry: CGFloat) -> some View {
        let now = Date()
        let cal = Calendar.current
        let h = cal.component(.hour, from: now)
        let m = cal.component(.minute, from: now)
        let displayH = h % 12 == 0 ? 12 : h % 12
        let displayM = (m / 5) * 5
        let mStr = displayM < 10 ? "0\(displayM)" : "\(displayM)"

        ZStack {
            phantomLabel(angle: state.hAngle, text: "\(displayH)", size: size, opacity: state.hDrifting ? 0.25 : 1.0, blur: state.hDrifting ? 4 : 0, weight: .bold, rx: rx * 0.85, ry: ry * 0.85)
            phantomLabel(angle: state.mAngle, text: mStr, size: size, opacity: state.mDrifting ? 0.25 : 0.9, blur: state.mDrifting ? 4 : 0, weight: .light, rx: rx * 1.15, ry: ry * 1.15)
        }
    }

    @ViewBuilder
    private func phantomLabel(angle: Double, text: String, size: CGFloat, opacity: Double, blur: CGFloat, weight: Font.Weight, rx: CGFloat, ry: CGFloat) -> some View {
        Text(text)
            .font(.system(size: size * 0.15, weight: weight, design: .rounded))
            .foregroundColor(.white)
            .opacity(opacity)
            .blur(radius: blur)
            .offset(x: sin(angle) * (rx * 0.85), y: -cos(angle) * ry)
            .shadow(color: .black.opacity(0.8), radius: 4)
    }

    private func drawHands(ctx: GraphicsContext, center: CGPoint, rx: CGFloat, ry: CGFloat) {
        drawHand(ctx: ctx, center: center, angle: state.rotH, rx: rx * 0.7, ry: ry * 0.7, width: 6, color: .white.opacity(state.hDrifting ? 0.35 : 1.0))
        drawHand(ctx: ctx, center: center, angle: state.rotM, rx: rx * 1.05, ry: ry * 1.05, width: 2.8, color: .white.opacity(state.mDrifting ? 0.35 : 0.85))
        drawHand(ctx: ctx, center: center, angle: state.rotS, rx: rx * 1.25, ry: ry * 1.25, width: 1.5, color: .red.opacity(0.9))
    }

    private func drawHand(ctx: GraphicsContext, center: CGPoint, angle: Double, rx: CGFloat, ry: CGFloat, width: CGFloat, color: Color) {
        let tip = CGPoint(x: center.x + sin(angle) * rx, y: center.y - cos(angle) * ry)
        ctx.stroke(Path { p in
            p.move(to: center)
            p.addLine(to: tip)
        }, with: .color(color), style: StrokeStyle(lineWidth: width, lineCap: .round))
    }
    
    private func drawTrail(ctx: GraphicsContext, center: CGPoint, angle: Double, rx: CGFloat, ry: CGFloat, opacity: Double) {
        let tip = CGPoint(x: center.x + sin(angle) * rx, y: center.y - cos(angle) * ry)
        ctx.stroke(Path { p in
            p.move(to: center)
            p.addLine(to: tip)
        }, with: .color(.white.opacity(opacity)), style: StrokeStyle(lineWidth: 1.5, dash: [5, 7]))
    }

    @ViewBuilder
    private func centerJewel(size: CGFloat) -> some View {
        ZStack {
            Circle()
                .fill(RadialGradient(colors: [.white, .gray.opacity(0.8)], center: .center, startRadius: 0, endRadius: size * 0.012))
                .frame(width: size * 0.03)
            Circle()
                .fill(.red)
                .frame(width: size * 0.008)
        }
    }
}
