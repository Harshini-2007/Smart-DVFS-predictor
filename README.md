**AI-Assisted Dynamic Voltage and Frequency Scaling Framework**
---

 Overview
 ---

Dynamic Voltage and Frequency Scaling (DVFS) is widely used to reduce power consumption by adjusting CPU frequency according to workload demands.

However, traditional DVFS mechanisms are reactive — they respond only to current CPU load. This often leads to:

Sudden frequency spikes

Thermal overshoot

Power instability

Oscillatory behavior

Delayed response to workload bursts

This project proposes a lightweight AI-assisted, thermal-aware DVFS controller that improves stability, responsiveness, and hardware safety.

 Core Idea
 ---

Predict short-term workload and apply thermal constraints before adjusting frequency.

Instead of reacting to the present workload, the system anticipates near-future demand and integrates temperature rise trends into its decision-making process.


 Implementation Details
 ---
**1️ Workload Prediction (ML Layer)**

**Model: Linear Regression**

Input: Current CPU Load

Output: Predicted Next CPU Load

This makes the controller proactive instead of reactive.

2️ Temperature Trend Monitoring
---

Temperature rise is calculated as:

**Temp_Rise = Current_Temperature − Previous_Temperature**


If temperature increases rapidly, frequency boosting is restricted.

This prevents:

Thermal spikes

Overheating

Emergency throttling

3️ Constrained DVFS Controller
---

Frequency decisions depend on:

Predicted workload

Temperature rise rate

Maximum frequency limit

Gradual ramp-up / ramp-down

This ensures:

Smooth frequency transitions

Reduced oscillations

Hardware-safe operation

 Dataset & Training
---
Features:

CPU Load (%)

Temperature (°C)

Frequency Level

Workload prediction target:

Next time-step CPU load

Dataset split:

80% Training

20% Testing (time order preserved)

Time-series integrity is maintained (shuffle=False).

 many systems treat thermal and predictive mechanisms separately.

 How This Project Differs
---
This framework combines:

 -Short-term workload prediction
- Temperature rise constraint
- Lightweight ML model
- Gradual frequency scaling

Unlike deep learning–heavy solutions, this design:

Maintains very low computational cost

Is suitable for real-time systems

Is embedded-friendly

Bridges predictive intelligence and thermal safety



 Technologies Used
 ---

Python

Pandas

NumPy

Scikit-learn
---


 Expected Benefits

Reduced thermal spikes

More stable power behavior

Fewer unnecessary frequency boosts

Author 
---
Harshini Perumal

