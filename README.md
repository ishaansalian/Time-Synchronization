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

| Date Range           | Milestone                                        | Tasks                                                                                       |
|---------------------|--------------------------------------------------|---------------------------------------------------------------------------------------------|
| 9/29/24 - 10/5/24   | Project Planning and Hardware Pickup             | - Discuss project goals and requirements among team.<br>- Pick up hardware (ESP32s and Raspberry Pi) from the lab. |
| 10/6/24 - 10/19/24  | Initial Tests & Develop Synchronization Protocol (Part 1) | - Establish wireless communication between Raspberry Pi and ESP32 devices.<br>- Test basic sensor data transmission from ESP32 to Raspberry Pi.<br>- Begin developing the initial time synchronization protocol on Raspberry Pi.<br>- Implement basic algorithms for collecting timestamped sensor data.<br>- Work on handling network delays between devices.<br>- Document key challenges and insights. |
| 10/20/24 - 10/26/24 | Develop Synchronization Protocol (Part 2)       | - Complete the synchronization protocol, focusing on clock drift estimation.<br>- Refine the algorithm for synchronizing time between Raspberry Pi and ESP32 devices.<br>- Perform initial tests of the synchronization protocol.<br>- **First Check-in (October)** |
| 10/27/24 - 11/9/24  | Testing and Debugging                            | - Run comprehensive tests to evaluate network delay and synchronization accuracy.<br>- Log and analyze clock drift between the devices.<br>- Identify issues or areas for optimization in both hardware and software.<br>- Adjust hardware timers and communication protocols as needed.<br>- Continue optimizing the synchronization protocol.<br>- Prepare a mid-project status update.<br>- **Second Check-in (November)** |
| 11/10/24 - 11/16/24 | System Integration and Final Adjustments         | - Integrate the synchronization protocol with the full system.<br>- Ensure all hardware components are functioning properly together.<br>- Optimize the final setup for the best performance.<br>- Begin drafting the final report. |
| 11/17/24 - 11/23/24 | System Evaluation and Documentation              | - Evaluate the performance of the system.<br>- Gather results on synchronization accuracy, clock drift, and network delay.<br>- Complete final tests and ensure all deliverables are met.<br>- Finalize the system design documentation. |
| 11/24/24 - 11/30/24 | Final Report and Presentation Preparation        | - Complete the final report, including results, analysis, and recommendations.<br>- Prepare the project presentation, focusing on key insights and contributions.<br>- Rehearse the presentation and receive feedback.<br>- **Third Check-in (December)** |
| 12/1/24 - 12/7/24   | Final Presentation and Project Submission        | - Deliver the final presentation to the class or professor.<br>- Submit the final report, code, and documentation.<br>- Return hardware to the lab.<br>- Conduct a project debrief and discuss lessons learned. |


## References
1. [HAEST: Harvesting Ambient Events to Synchronize Time across Heterogeneous IoT Devices](https://www.computer.org/csdl/proceedings-article/rtas/2024/584100a265/1Y5F2yadseQ)
2. [Automated Synchronization of Driving Data Using Vibration and Steering Events](https://arxiv.org/abs/1510.06113)
3. [Exploiting Smartphone Peripherals for Precise Time Synchronization](https://ieeexplore.ieee.org/document/8886639)
