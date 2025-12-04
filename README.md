# OpenGL House & Rainfall Simulation

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenGL](https://img.shields.io/badge/Library-PyOpenGL-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📝 Project Overview
This project is a 2D computer graphics simulation developed for **CSE423: Computer Graphics**. It demonstrates the use of fundamental OpenGL primitives to construct a scene and implement 2D animation logic.

The simulation renders a house using `GL_TRIANGLES` and `GL_LINES` and features a continuous rainfall animation. Users can interact with the system to simulate wind (bending the rain) and change the time of day.The application allows users to interact with the environment in real-time, controlling wind direction to bend the rain and toggling between day and night modes.


## 🎮 Controls
The simulation uses the keyboard for interaction:

| Key | Function | Description |
| :--- | :--- | :--- |
| **Right Arrow (→)** | Wind Right | Bends the rain angle to the right (Max 45°). |
| **Left Arrow (←)** | Wind Left | Bends the rain angle to the left (Max -45°). |
| **`d`** | Day Mode | Gradually lightens the sky/background. |
| **`n`** | Night Mode | Gradually darkens the sky/background. |

## 🛠️ Prerequisites
You need **Python** installed along with the **PyOpenGL** library.

### Installation
1.  Install Python (if not already installed).
2.  Install the OpenGL libraries using pip:
    ```bash
    pip install PyOpenGL PyOpenGL_accelerate
    ```

## 🚀 How to Run

### 1. Install Dependencies
This project requires **Python** and the **PyOpenGL** library. If you haven't installed the library yet, run this command in your terminal or command prompt:

```bash
pip install PyOpenGL PyOpenGL_accelerate
```
### 2. Run the Simulation
Once the dependencies are installed, you can run the project by executing the python file:

```bash
python src/OpenGL-House-Rainfall-Simulation.py
```
## 📂 File Structure

```text
.
├── src/
│   └── OpenGL-House-Rainfall-Simulation.py   # Main simulation source code
├── requirements.txt                          # List of required Python libraries
├── .gitignore                                # Config file to ignore unnecessary local files
└── README.md                                 # Project documentation
```
## 👤 Author
* **Md. Fuadur Rahman**


## 📄 License
This project is for educational purposes.
