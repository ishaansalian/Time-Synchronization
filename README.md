# Time-Synchronization Via Sensing
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
- **Ishaan Salian**
  - Lead role: Hardware System Integration (Raspberry PI)
  - Responsibilities:
    - Integrate the time synchronization protocol on the Raspberry Pi, ensuring that it effectively uses data from ESP32 devices.
    - Characterize network delay and clock drift between devices, and analyze the overall performance of the system.
    - Perform real-world tests to validate the system’s accuracy under various network conditions.
  - Key Focus:
    - Measuring and optimizing the performance of the hardware setup, focusing on synchronization accuracy, clock drift, and system integration.

- **Haoran Zhang**
  - Lead role: Hardware Communication (ESP32)
  - Responsibilities:
    - Set up and manage communication between the Raspberry Pi and ESP32 devices (e.g., Bluetooth, Wi-Fi).
    - Ensure the physical connections (GPIO, I2C, SPI) and wireless communication protocols are functioning correctly.
    - Develop and troubleshoot the firmware for ESP32 devices to send sensor data with accurate timestamps.
  - Key Focus:
    - Ensuring reliable data transmission and minimizing delay in network communication. Managing the hardware interface and connectivity of ESP32 and Raspberry Pi.
  

## **Project Timeline**

| **Milestone** | **Tasks** | **Deadline** | **Check-in** |
|---------------|-----------|--------------|--------------|
| **9/29/24 - 10/5/24: Project Planning and Hardware Pickup** | <ul><li>Discuss project goals and requirements with team and professor.</li><li>Pick up hardware (ESP32s and Raspberry Pi) from the lab after signing the checkout sheet.</li><li>Create GitHub repository and set up initial documentation (motivation, design goals, system blocks, timeline).</li><li>Divide roles and responsibilities.</li><li>Research references provided and other relevant papers for time synchronization techniques.</li></ul> | **End of Week 1** | |
| **10/6/24 - 10/19/24: Initial Tests & Develop Synchronization Protocol (Part 1)** | <ul><li>Establish wireless communication (e.g., Bluetooth or Wi-Fi) between Raspberry Pi and ESP32 devices.</li><li>Test basic sensor data transmission from ESP32 to Raspberry Pi.</li><li>Confirm timestamps are being accurately transmitted and logged.</li><li>Begin developing the initial time synchronization protocol on Raspberry Pi.</li><li>Implement basic algorithms for collecting timestamped sensor data.</li><li>Work on handling network delays between devices.</li><li>Document key challenges and insights.</li></ul> | **End of Week 2** | |
| **10/20/24 - 10/26/24: Develop Synchronization Protocol (Part 2)** | <ul><li>Complete the synchronization protocol, focusing on clock drift estimation.</li><li>Refine algorithm for synchronizing time between Raspberry Pi and ESP32 devices.</li><li>Perform initial tests of the synchronization protocol.</li></ul> | **End of Week 4** | **First Check-in (October)** |
| **10/27/24 - 11/9/24: Testing and Debugging** | <ul><li>Run comprehensive tests to evaluate network delay and synchronization accuracy.</li><li>Log and analyze clock drift between the devices.</li><li>Identify issues or areas for optimization in both hardware and software.</li><li>Adjust hardware timers and communication protocols as needed.</li><li>Continue optimizing the synchronization protocol.</li><li>Prepare mid-project status update.</li></ul> | **End of Week 6** | **Second Check-in (November)** |
| **11/10/24 - 11/16/24: System Integration and Final Adjustments** | <ul><li>Integrate the synchronization protocol with the full system.</li><li>Ensure all hardware components are functioning properly together.</li><li>Optimize the final setup for the best performance.</li><li>Begin drafting the final report.</li></ul> | **End of Week 7** | |
| **11/17/24 - 11/23/24: System Evaluation and Documentation** | <ul><li>Evaluate the performance of the system.</li><li>Gather results on synchronization accuracy, clock drift, and network delay.</li><li>Complete final tests and ensure all deliverables are met.</li><li>Finalize the system design documentation.</li></ul> | **End of Week 8** | |
| **11/24/24 - 11/30/24: Final Report and Presentation Preparation** | <ul><li>Complete the final report, including results, analysis, and recommendations.</li><li>Prepare the project presentation, focusing on key insights and contributions.</li><li>Rehearse the presentation and receive feedback.</li></ul> | **End of Week 9** | **Third Check-in (December)** |
| **12/1/24 - 12/7/24: Final Presentation and Project Submission** | <ul><li>Deliver the final presentation to the class or professor.</li><li>Submit the final report, code, and documentation.</li><li>Return hardware to the lab.</li><li>Conduct a project debrief and discuss lessons learned.</li></ul> | **End of Week 10** | |


## References
1. [HAEST: Harvesting Ambient Events to Synchronize Time across Heterogeneous IoT Devices](https://www.computer.org/csdl/proceedings-article/rtas/2024/584100a265/1Y5F2yadseQ)
2. [Automated Synchronization of Driving Data Using Vibration and Steering Events](https://www.sciencedirect.com/science/article/abs/pii/S0167865516000581)
3. [Exploiting Smartphone Peripherals for Precise Time Synchronization](https://ieeexplore.ieee.org/document/8886639)
