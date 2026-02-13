# Multi-Container Docker Infrastructure
**Author:** ArifulHudaJoy  
**Project Type:** Container Orchestration & DevOps  

### 📌 Project Overview
This project demonstrates a production-style architecture using Docker. It features two microservices—a **Writer** and a **Reader**—communicating over a virtual network and sharing a persistent storage volume.



### 🏗️ Architecture
* **Writer Service (Python/Flask):** Generates data and writes it to a shared volume.
* **Reader Service (Python/Flask):** Accesses the same volume to display the data.
* **Docker Compose:** Orchestrates the build, networking, and health checks of both services.

### 🛠️ Key DevOps Concepts Demonstrated
* **Multi-Stage Style Builds:** Using custom `Dockerfiles` for microservices.
* **Persistence:** Using Docker **Volumes** to ensure data survives container restarts.
* **Service Discovery:** Internal networking where containers find each other by service name.
* **Health Checks:** Automated monitoring to ensure services are ready before dependencies start.
* **Restart Policies:** Ensuring high availability with `restart: always`.

### 🚀 How to Run
```bash
# Build and start the entire system
docker-compose up --build
