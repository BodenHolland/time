# Apple Watch Implementation Plan: Time Orientation
**Objective**: Deploy the "Trailing Future" abstract clock on watchOS as a full-screen, immersive experience that hides the native system time.

---

## 1. The "Stealth" Full-Screen Strategy
To bypass the native watchOS status bar (the digital time in the corner), we will use the **Video Player Overlay Hack**.

*   **Logic**: watchOS automatically hides the status bar when a video is being played to avoid obstructing the content.
*   **Execution**:
    1.  Embed a hidden `AVPlayer` or `VideoPlayer` view in the background.
    2.  Loop a 1-second silent, empty video file (or a 1x1 pixel black fragment).
    3.  Layer the SwiftUI "Trailing Future" UI on top of this container.
    4.  The system will treat the app as a "Media Player" and grant true edge-to-edge real estate.

## 2. Technical Architecture (SwiftUI)
- **Engine**: `TimelineView(.animation)` will drive the UI updates at 60fps, providing the same fluid performance as our `requestAnimationFrame` loop.
- **Rendering**: `Canvas` or nested `ZStack` with `rotationEffect`.
- **Haptics**: Use `WKInterfaceDevice.current().play(.click)` on every second "tick" and `.impact` on Reality Shifts.

## 3. Core Logic Porting
The following logic units from our JavaScript version must be maintained for parity:

### A. The 3-Minute Milestone Buffer
```swift
// Swift version of our milestone logic
let m = currentMinute
let baseline = m - 3
let mMilestone = Int(floor(Double(max(0, baseline)) / 5.0)) * 5
```

### B. Cumulative Rotation (Zero-Rewind Fix)
To prevent the hands from "spinning backward" when crossing the 12 o'clock mark:
- Store rotations as **cumulative doubles** (e.g., instead of 350° -> 0°, go 350° -> 360°).
- Ensure `shiftReality()` adds to the existing total rotation rather than resetting.

### C. The 6-14s Reality Shift
- Trigger a `Timer` with randomized intervals.
- Use SwiftUI's `.interpolatingSpring` or `.easeInOut` with the **1.74s duration** to match the "heavy" glide feel.

## 4. Hardware Optimization (OLED)
- **Background**: Pure `#000000` (zero power usage on OLED).
- **Burn-in Protection**: The "Dynamic Reality" shifts every 10 seconds are ideal for Apple Watch longevity, as they naturally rotate the pixels being used for labels and hands.
- **Battery**: Use `TimelineView`'s context to drop the framerate to 1fps when the wrist is lowered (Always-On mode), hiding the second hand to save power.

## 5. Deployment Checklist
1. [ ] **Xcode Project**: Create a new watchOS App (SwiftUI).
2. [ ] **Background Mode**: Enable "Audio, AirPlay, and Picture in Picture" to help maintain app persistence.
3. [ ] **Wake Settings**: Configure Watch Settings -> General -> Return to Clock -> **After 1 Hour**.
4. [ ] **Assets**: Include a 1fps silent black MP4 for the status bar hack.

---

**Current Status**: Design and logic verified in Browser Prototype. Ready for Swift translation.
