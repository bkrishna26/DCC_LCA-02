# Distributed & Cloud Computing (DCC) – LCA-2

## Student Information

* **Name:** Bhavanam Krishna Bharath Reddy
* **Course:** Distributed & Cloud Computing
* **Assignment:** LCA-2

---

# 1. Bully Election Algorithm

## Objective

* To understand leader election in distributed systems
* To simulate process failure and recovery
* To implement coordination using the Bully Election Algorithm

---

## Theory

The Bully Election Algorithm is a leader election algorithm used in distributed systems to select a coordinator when the current coordinator fails.

### Key Concepts

* Each process in the system is assigned a unique ID
* The process with the highest ID is selected as the coordinator
* When a process detects coordinator failure:

  * It sends election messages to all higher-ID processes
  * If no higher process responds, it becomes the coordinator
  * If a higher process responds, it takes over the election

---

## Algorithm Steps

1. Start
2. Input the number of processes
3. Assign status (Active/Failed) to each process
4. Detect coordinator failure
5. Send election messages to higher-ID processes
6. Higher process takes over the election
7. Repeat until the highest active process is found
8. Declare the coordinator
9. Stop

---

## Implementation Summary

The implemented program simulates a distributed system with multiple processes, where each process can be in an active or failed state.

### Functional Features

* Dynamic input of process states (Active/Failed)
* Automatic identification of the initial coordinator
* Simulation of process failure and recovery
* Recursive election mechanism
* Automatic detection of coordinator failure and re-election

The election process ensures that the highest active process is always selected as the coordinator.

---

## Result

The program successfully demonstrates the working of the Bully Election Algorithm by electing the highest active process as the coordinator after failures.

---

## Conclusion

The Bully Algorithm provides an effective mechanism for leader election in distributed systems. However, it may generate higher message overhead and is more suitable for smaller systems.

---

# 2. Network File System (NFS)

## Objective

* To configure an NFS server and client
* To enable file sharing across systems in a network

---

## Overview

The Network File System (NFS) allows a system to share directories over a network, enabling remote systems to access files as if they were local.

---

## Implementation Summary

* Configured NFS server and exported a shared directory
* Mounted the shared directory on the client system
* Verified file sharing between server and client

---

## Result

The client system successfully accessed and modified files from the server’s shared directory.

---

## Conclusion

NFS simplifies file sharing in distributed environments by providing transparent and efficient access to remote data.

---

# 3. Cloud Computing – Smart Agriculture Application

## Objective

* To deploy a web application using cloud services
* To demonstrate application accessibility through a browser

---

## Project Description

A Smart Agriculture Web Application was developed to provide basic recommendations based on user input.

### Features

* User input for crop type and soil type
* Backend processing using Flask
* Display of agricultural suggestions
* Simple and user-friendly interface

---

## Technologies Used

* **Frontend:** HTML, CSS
* **Backend:** Python (Flask)
* **Deployment:** Gunicorn
* **Cloud Platform:** Render

---

## Deployment Process

1. Developed the Flask application
2. Created required files (`requirements.txt`, `Procfile`)
3. Uploaded the project to GitHub
4. Connected the repository to Render
5. Configured deployment settings:

   * Build Command: `pip install -r requirements.txt`
   * Start Command: `gunicorn app:app`
6. Successfully deployed the application

---

## Result

The application is successfully deployed on the cloud and can be accessed through a web browser using a public URL.

---

## Conclusion

Cloud deployment enables applications to be accessible from anywhere. The use of Render simplified the deployment of a full-stack Flask application.

---

# Overall Conclusion

This assignment provided practical understanding of:

* Leader election in distributed systems
* Network-based file sharing using NFS
* Deployment of applications using cloud platforms

These concepts are essential in building scalable and efficient distributed systems.

---
