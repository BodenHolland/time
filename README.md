# Time Orientation — Aurora

An ambient, seasonally-aware time visualization clock that dynamically shifts colors based on the solar hour. 

## Features

- **Seasonally Aware Anchors:** Approximates sunrise and sunset via system date to dynamically anchor a 24-hour hue cycle.
- **Vibrant Liquid Glass Bezel:** A 3D raised convex glass effect inspired by iOS vibrant materials, featuring blur, high saturation, and dynamic specular hits.
- **Dynamic Color Shifts:** The center and edge of the clock face smoothly blend between a 24-hour curated color palette, simulating dawn, sunrise, noon, golden hour, sunset, dusk, and night.
- **Viscous Hand Trails:** Smooth, drifting trails that track the hour and minute hands, casting glowing dynamic shadows.
- **Holographic Details:** Iridescent interference shimmer and laser-beam hands that adapt their luminance and contrast to the brightness of the current palette.

## Technical Details

- Pure HTML, CSS, and Vanilla JavaScript.
- Dynamic DOM manipulation and `requestAnimationFrame` for buttery smooth 60fps animations.
- No external libraries or dependencies.

## How It Works

Aurora tracks real-time and normalizes it to a "Virtual Solar Hour". Based on the current day of the year, it calculates the approximate sunrise and sunset for a standard mid-latitude, making summer days feel longer and winter days shorter. The hands use a viscous sweeping algorithm to naturally "drift" and settle onto their targets, offering an organic representation of passing time rather than rigid ticking.
