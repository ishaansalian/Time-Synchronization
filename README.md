# Time-Synchronization
This project implements a time synchronization protocol for embedded devices using timestamped sensor data. The system leverages ESP32 devices and a Raspberry Pi to estimate network delays and relative clock drift, offering an efficient solution for time synchronization in resource-constrained IoT environments.

## Motivation
Time synchronization is crucial for distributed applications in networked embedded devices, such as smart homes, automated agriculture, and autonomous vehicles. Many resource-constrained devices at the edge lack the capacity for traditional timing services. However, these devices regularly transmit timestamped sensor data to gateways. This project aims to utilize that data to synchronize embedded devices efficiently.

## Design Goals
- Develop a time synchronization protocol using timestamped sensor data.
- Characterize network delay between Raspberry Pi and edge devices.
- Estimate and adjust for relative clock drift between the devices.

## Deliverables
1. Time synchronization protocol running on Raspberry Pi.
2. Analysis of network delay between the Raspberry Pi and ESP32 devices.
3. Estimation of clock drift between devices.
4. Final report with performance evaluation and recommendations.

## System Block Diagram


## Hardware/Software Requirements
- **Hardware:**
  - ESP32 Things
  - Raspberry Pi
- **Software:**
  - Programming for ESP32 and Raspberry Pi
  - Communication protocols (Bluetooth, Wi-Fi)
  - Basic machine learning algorithms for time drift estimation

## Team Members & Responsibilities
- **Ishaan Salian:**
  - Lead role: 
  - Responsibilities: 
- **Haoran Zhang:**
  - Lead role:
  - Responsibilities:


## Project Timeline

| **Milestone** | **Tasks** | **Deadline** | **Check-in** |
|---------------|-----------|--------------|--------------|
| **Week 1: Project Planning and Hardware Pickup** | <ul><li>Discuss project goals and requirements with team and professor</li><li>Pick up hardware (ESP32 and Raspberry Pi) from the lab after signing the checkout sheet</li><li>Create GitHub repository and set up initial documentation (motivation, design goals, system blocks, timeline)</li><li>Divide roles and responsibilities</li><li>Research references provided and other relevant papers for time synchronization techniques</li></ul> | **End of Week 1** | |
| **Week 2: Hardware Setup and Initial Tests** | <ul><li>Set up Raspberry Pi and ESP32 hardware environment</li><li>Establish wireless communication (e.g., Bluetooth or Wi-Fi) between Raspberry Pi and ESP32 devices</li><li>Test basic sensor data transmission from ESP32 to Raspberry Pi</li><li>Confirm timestamps are being accurately transmitted and logged</li></ul> | **End of Week 2** | |
| **Week 3: Develop Synchronization Protocol (Part 1)** | <ul><li>Begin developing the initial time synchronization protocol on Raspberry Pi</li><li>Implement basic algorithm for collecting timestamped sensor data</li><li>Work on handling network delays between devices</li><li>Document key challenges and insights</li></ul> | **End of Week 3** | |
| **Week 4: Develop Synchronization Protocol (Part 2)** | <ul><li>Complete the synchronization protocol, focusing on clock drift estimation</li><li>Refine algorithm for synchronizing time between Raspberry Pi and ESP32 devices</li><li>Perform initial tests of the synchronization protocol</li></ul> | **End of Week 4** | **First Check-in (October)** |
| **Week 5: Testing and Debugging (Part 1)** | <ul><li>Run comprehensive tests to evaluate network delay and synchronization accuracy</li><li>Log and analyze clock drift between the devices</li><li>Identify issues or areas for optimization in both hardware and software</li><li>Adjust hardware timers and communication protocols as needed</li></ul> | **End of Week 5** | |
| **Week 6: Testing and Debugging (Part 2)** | <ul><li>Continue optimizing the synchronization protocol</li><li>Test under different network conditions to simulate real-world scenarios</li><li>Ensure synchronization remains stable and accurate</li><li>Prepare mid-project status update</li></ul> | **End of Week 6** | **Second Check-in (November)** |
| **Week 7: System Integration and Final Adjustments** | <ul><li>Integrate the synchronization protocol with the full system</li><li>Ensure all hardware components are functioning properly together</li><li>Optimize the final setup for the best performance</li><li>Begin drafting the final report</li></ul> | **End of Week 7** | |
| **Week 8: System Evaluation and Documentation** | <ul><li>Evaluate the performance of the system</li><li>Gather results on synchronization accuracy, clock drift, and network delay</li><li>Complete final tests and ensure all deliverables are met</li><li>Finalize the system design documentation</li></ul> | **End of Week 8** | |
| **Week 9: Final Report and Presentation Preparation** | <ul><li>Complete the final report, including results, analysis, and recommendations</li><li>Prepare the project presentation, focusing on key insights and contributions</li><li>Rehearse the presentation and receive feedback</li></ul> | **End of Week 9** | **Third Check-in (December)** |
| **Week 10: Final Presentation and Project Submission** | <ul><li>Deliver the final presentation to the class or professor</li><li>Submit the final report, code, and documentation</li><li>Return hardware to the lab</li><li>Conduct a project debrief and discuss lessons learned</li></ul> | **End of Week 10** | |


## References
1. [HAEST: Harvesting Ambient Events to Synchronize Time across Heterogeneous IoT Devices](https://www.computer.org/csdl/proceedings-article/rtas/2024/584100a265/1Y5F2yadseQ)
2. [Automated Synchronization of Driving Data Using Vibration and Steering Events](https://arxiv.org/abs/1510.06113)
3. [Exploiting Smartphone Peripherals for Precise Time Synchronization](https://ieeexplore.ieee.org/document/8886639)
