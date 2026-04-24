# Intelligent Sortation and Gap Control System
### Advanced Logistics Automation for Fragile Goods Handling

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Configura CET](https://img.shields.io/badge/Configura%20CET-Design-blue?style=for-the-badge)
![IO-Link](https://img.shields.io/badge/IO--Link-Industrial%20Sensing-orange?style=for-the-badge)
![VFD Control](https://img.shields.io/badge/VFD-Control-green?style=for-the-badge)
![Mermaid](https://img.shields.io/badge/Mermaid-Diagrams-FF69B4?style=for-the-badge&logo=mermaid&logoColor=white)

---

## Problem Statement
In traditional high-speed logistics, sortation systems often struggle with fragile goods. Standard systems rely on static timing and fixed gaps, which lead to:
- High Collision Rates: Inability to compensate for belt slippage or inertia.
- Low Throughput: Excessive safety gaps reduce the number of units processed per hour.
- Product Damage: Abrupt stops and starts at merge points can tip or break sensitive items.

The Challenge: How to increase throughput while maintaining a Zero-Collision and Zero-Damage environment for fragile items.

---

## System Architecture and Workflow
The system utilizes a hierarchical control strategy where physical sensor data is processed by a Python-based logic engine to drive Variable Frequency Drives (VFDs).

```mermaid
graph TB
    subgraph Sensing_Layer [Industrial Sensing Layer]
        S1[IO-Link Laser Sensor A]
        S2[IO-Link Laser Sensor B]
        S3[Encoder Feedback]
    end

    subgraph Logic_Engine [Advanced Control Logic - Python]
        direction TB
        Input[Data Aggregator] --> Filter[Kalman Filter - Noise Reduction]
        Filter --> Momentum[Momentum Calculator]
        Momentum --> GapCalc[Dynamic Gap Optimizer]
        GapCalc --> Decision{Merge Protocol}
    end

    subgraph Actuation_Layer [Physical Execution]
        VFD1[Main Line VFD]
        VFD2[Feeder Line VFD]
        Diverter[Pneumatic Shoe Diverter]
    end

    S1 & S2 & S3 --> Input
    Decision -- Acceleration Pulse --> VFD2
    Decision -- Velocity Sync --> VFD1
    Decision -- Trigger --> Diverter

    Actuation_Layer -. Real-time Feedback .-> Sensing_Layer
```

---

## Key Technical Features

### 1. Dynamic Gap Adjustment (DGA) Logic
Implemented in Python, the DGA algorithm replaces static timers with a physics-aware calculation. It factors in:
- Momentum-Based Merging: Calculates the exact acceleration needed for a package to hit a gap without exceeding 0.8 m/s2.
- Slippage Compensation: Uses real-time sensor feedback to detect if a package has drifted from its expected position and sends correction pulses to the VFD.

### 2. Configura CET 3D Layout
- Wedge Merge (45 degree): Optimized for smooth entry into high-speed main lines.
- Zero-Pressure Accumulation (ZPA): Intelligent zones that prevent packages from touching during downstream stalls.
- High-Speed Shoe Sorters: Designed within Configura CET to handle up to 2,100 units per hour.

### 3. Industrial Smart Sensing (IO-Link)
- Sub-millimeter Tracking: Laser distance sensors provide 1mm resolution.
- Real-time Diagnostics: Continuous monitoring of signal quality to prevent ghost detections.

---

## Performance Benchmarks
| Metric | Pre-Optimization | Post-Optimization | Improvement |
| :--- | :--- | :--- | :--- |
| Throughput | 1,800 units/hr | 2,016 units/hr | +12% |
| Minimum Gap | 800mm | 550mm | -31% |
| Collision Rate | ~0.5% | ~0.01% | Near Zero |

---

## Future Roadmap
- AI-Based Prediction: Using LSTM models to predict downstream bottlenecks.
- Digital Twin Integration: Linking the Configura CET model to real-time PLC data.
- Energy Optimization: Reducing VFD power consumption during low-flow periods.

---

## Project Structure
- src/: Core Python logic for the Gap Controller.
- docs/: Technical specifications and system parameters.
- assets/: 3D Layout snapshots and flow diagrams.
