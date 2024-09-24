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
| Milestone | Deadline |
|-----------|----------|
| Project planning and setup | Week 1 |
| Hardware setup and initial tests | Week 2 |
| Develop synchronization protocol | Week 3-4 |
| Test and evaluate system | Week 5-6 |
| Final report and presentation | Week 7 |

## References
1. [HAEST: Harvesting Ambient Events to Synchronize Time across Heterogeneous IoT Devices](https://www.computer.org/csdl/proceedings-article/rtas/2024/584100a265/1Y5F2yadseQ)
2. [Automated Synchronization of Driving Data Using Vibration and Steering Events](https://arxiv.org/abs/1510.06113)
3. [Exploiting Smartphone Peripherals for Precise Time Synchronization](https://ieeexplore.ieee.org/document/8886639)
