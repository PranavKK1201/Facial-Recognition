# Facial-Recognition
# Facial Recognition System README

## Introduction
This repository contains a Python implementation of a facial recognition system using the `deepface` library. The system allows users to enroll new faces, perform face recognition on live camera feeds, and stop the system operation. This README file aims to provide a comprehensive understanding of the project structure, functionalities, dependencies, and usage.

 Follow the prompts displayed in the console to interact with the system:
   - Press `1` to enter a new face.
   - Press `2` to start face recognition on the live camera feed.
   - Press `3` to stop the program completely.

## Functionality
### 1. Enroll New Faces (`newFace` function)
- The `newFace` function allows users to enroll new faces into the system.
- Users are prompted to enter the name of the person and the URL (path) to the image containing the face.
- The image URL is stored in a dictionary (`imageDict`) with the corresponding person's name.

### 2. Start Face Recognition (`recognition` function)
- The `recognition` function initiates face recognition on the live camera feed.
- It captures frames from the camera and compares them with the enrolled faces in the `imageDict`.
- If a match is found, it prints a welcome message with the person's name.
- If no match is found, it prints a message indicating that the face is not recognized.

### 3. Live Feed (`livefeed` function)
- The `livefeed` function captures the live camera feed and displays it on the screen.
- It continuously captures frames until the user presses the 'q' key to exit.

### 4. Utility Functions
- `Capturing`: This function captures frames from the camera. It is used internally by other functions.

