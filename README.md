<!-- BANNER -->
<h1 align="center" style="font-size:3.2em; font-weight:800; background: linear-gradient(90deg, #0f2027, #203a43, #2c5364); color: white; padding: 1rem; border-radius: 0.5rem;">
Industrial Safety Monitoring using NVIDIA Jetson Nano
</h1>

<p align="center" style="font-size:1.2em; color: #888;">
Real-Time Edge AI Solution | Face Recognition, Helmet Detection, and Activity Classification  
Developed by Rahul Narendra Sharma | CIRD Summer Training 2025
</p>

---

# Industrial Safety Monitoring System using Jetson Nano

**Integration of Multiple Deep Learning Models on NVIDIA Jetson Nano**  
**Real-Time Industrial Safety Monitoring System**  
**Rahul Narendra Sharma**  
**CIRD Summer Industrial Training 2025**  
**6 July 2025**

---

## Problem Statement

- Industrial sites often lack real-time monitoring.
- Manual checks are prone to human error.
- Safety gear and activity monitoring need automation.

---

## Project Overview

- Jetson Nano-based safety compliance system
- Real-time detection and classification
- Components:
  - Face Recognition
  - Helmet Detection
  - Activity Classification
  - Stream Integration

---

## Datasets and Model Training

- Annotated data with Roboflow
- YOLOv8: Helmet + Activity
- InsightFace: Face Recognition
- Preprocessing: Augmentation, Cleaning, PCA

---

## Architecture Diagram

![Demo Output](/working_images/SS.png)
---

## Face Recognition

- YOLOv8 detects faces
- InsightFace extracts embeddings
- Matches using cosine similarity
- Reference folder: `reference_images/`
![Demo Output](/working_images/Screenshot%202025-07-06%20095455.png)

---

## Helmet Detection

- Custom YOLOv8 trained model
- Detects presence/absence of helmets
- Works under variable lighting and angles
![Demo Output](/working_images/output1.jpeg)
---

## Human Activity Recognition

- YOLOv8 classifies posture/tools
- Labels: working / idle
- Combined with helmet info for compliance
![Demo Output](/working_images/output.jpeg)
---

## Full Integration (trivision.py)

- Combines Face + Helmet + Activity models
- Inputs Jetson stream, outputs processed stream
- Flask re-broadcast to LAN

---

## Technical Stack

| Component   | Details                                 |
|------------|------------------------------------------|
| Hardware   | Jetson Nano + Webcam                     |
| Language   | Python                                   |
| Libraries  | OpenCV, Ultralytics, Flask, InsightFace  |
| Deployment | LAN stream (port 5000)                   |
![Demo Output](/working_images/setup.jpg)
---

## Simplified Logic Flow

1. Start Jetson & Camera  
2. Run `cam_processed.py`  
3. Run `trivision.py` on Server  
4. Models detect, annotate  
5. Broadcast to App/Web

---

## Logic Flow Diagram

```mermaid
graph TD;
    A[Jetson Nano Stream] --> B[Face Detection (YOLOv8)]
    A --> C[Helmet Detection]
    A --> D[Activity Recognition]
    B --> E[Face Matching (InsightFace)]
    C --> E
    D --> E
    E --> F[Flask LAN Stream]
```

---

## Working Demo

- Screenshot/stream demo
- Labeled faces + gear + activity
- Access via `http://<server-ip>:5000/processed`

![Demo Output](/working_images/Screenshot%202025-07-03%20154250.png)

---

## Key Features

- Real-time detection on edge device (Jetson Nano)
- No external GPU/cloud dependency
- Web/mobile ready via simple LAN setup
- Works under varying lighting and movement conditions
- Modular Python-based pipeline

---

## Folder Structure

```bash
├── images/
│   ├── architecture_diagram.png
│   ├── working_demo.png
├── reference_images/       # Stored face references
├── cam_processed.py        # Captures and prepares stream
├── trivision.py            # Combines and serves detection models
├── README.md
```

---

## Conclusion

- Modular, scalable edge-AI solution
- Enables industrial safety monitoring
- Integrated with web/mobile for live use
![Demo Output](/working_images/app_feed.jpg)
> A high-performance, edge-computing solution designed for low-latency environments and real-time actionable insights.  
> Author: Rahul Narendra Sharma  
> Developed under CIRD Summer Training Program, 2025

---
