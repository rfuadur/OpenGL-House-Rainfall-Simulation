# OpenGL House & Rainfall Simulation

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenGL](https://img.shields.io/badge/Library-PyOpenGL-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📝 Project Overview
This project is a 2D computer graphics simulation developed for **CSE423: Computer Graphics** (Lab Assignment 1)[cite: 1]. [cite_start]It renders a scene featuring a house constructed from basic geometric primitives and simulates a continuous rainfall weather system[cite: 1].

The application allows users to interact with the environment in real-time, controlling wind direction to bend the rain and toggling between day and night modes.

| Key | Function | Description |
| :--- | :--- | :--- |
| **Right Arrow (→)** | Wind Right | Bends the rain angle to the right (Max 45°). |
| **Left Arrow (←)** | Wind Left | Bends the rain angle to the left (Max -45°). |
| **`d`** | Day Mode | Gradually lightens the sky/background. |
| **`n`** | Night Mode | Gradually darkens the sky/background. |
## 🎮 Controls
The simulation uses the keyboard for interaction:

| Key | Function | Description |
| :--- | :--- | :--- |
| **Right Arrow (→)** | Wind Right | [cite_start]Increases rain angle to the right (max 45°)[cite: 3]. |
| **Left Arrow (←)** | Wind Left | [cite_start]Decreases rain angle to the left (max -45°)[cite: 3]. |
| **`d`** | Day Mode | [cite_start]Gradually lightens the background color[cite: 3]. |
| **`n`** | Night Mode | [cite_start]Gradually darkens the background color[cite: 3]. |

## 🛠️ Prerequisites
You need **Python** installed along with the **PyOpenGL** library.

### Installation
1.  Install Python (if not already installed).
2.  Install the OpenGL libraries using pip:
    ```bash
    pip install PyOpenGL PyOpenGL_accelerate
    ```

## 🚀 How to Run
1.  Clone this repository:
    ```bash
    git clone [https://github.com/rfuadur/OpenGL-House-Rainfall-Simulation.git](https://github.com/rfuadur/OpenGL-House-Rainfall-Simulation.git)
2.  Navigate to the project directory:
    ```bash
    cd OpenGL-House-Rainfall-Simulation
    ```
3.  Run the simulation script:
    ```bash
    python OpenGL-House-Rainfall-Simulation.py
    ```

## 📂 File Structure
* `OpenGL-House-Rainfall-Simulation.py`: The main source code containing the OpenGL rendering logic and event listeners[cite: 3].
* `README.md`: Project documentation.

## 👤 Author
* **Md. Fuadur Rahman:**


## 📄 License
This project is for educational purposes.
