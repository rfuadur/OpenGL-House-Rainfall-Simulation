from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

# Window dimensions
W_Width, W_Height = 500, 500


rain_drops = []
rain_angle = 0  # Initial angle of rain (0 = straight down)
background_color = [0.0, 0.0, 0.0]  # Initial background color (black)
day_night_transition = 0.0  # 0.0 = night, 1.0 = day

class Point:
    def __init__(self, x, y, color=None, direction=None):
        self.x = x
        self.y = y
        
        # If color is not provided, assign a random color
        if color is None:
            self.color = [random.random(), random.random(), random.random()]
        else:
            self.color = color
            
        # If direction is not provided, assign a random direction
        if direction is None:
            # Random diagonal direction
            dx = random.choice([-1, 1]) * random.random()
            dy = random.choice([-1, 1]) * random.random()
            # Normalize to ensure consistent speed
            magnitude = math.sqrt(dx**2 + dy**2)
            self.dx = dx / magnitude
            self.dy = dy / magnitude
        else:
            self.dx, self.dy = direction

def init_rain_drops(num_drops=100):
    """Initialize rain drops with random positions"""
    global rain_drops
    rain_drops = []
    for _ in range(num_drops):
        x = random.uniform(-W_Width/2, W_Width/2)
        y = random.uniform(-W_Height/2, W_Height/2)
        rain_drops.append(Point(x, y, color=[0.5, 0.7, 1.0]))

def draw_house():
    """Draw a simple house using GL_TRIANGLES and GL_LINES"""
    # Adjust colors based on day/night cycle
    house_color = [0.7 , 0.4 , 0.2 ]
    roof_color = [0.9 ,0.2 , 0.1 ]
    window_color = [0.2 , 0.4 , 0.8 ]

    # Main house structure (using GL_TRIANGLES)
    glBegin(GL_TRIANGLES)
    # Left wall
    glColor3f(*house_color)
    glVertex2f(-100, -100)
    glVertex2f(-100, 50)
    glVertex2f(0, -100)
    
    # Right wall
    glVertex2f(0, -100)
    glVertex2f(-100, 50)
    glVertex2f(100, 50)
    
    glVertex2f(0, -100)
    glVertex2f(100, 50)
    glVertex2f(100, -100)
    
    # Roof
    glColor3f(*roof_color)
    glVertex2f(-120, 50)
    glVertex2f(0, 120)
    glVertex2f(120, 50)
    glEnd()
    
    # Door (using GL_TRIANGLES)
    glBegin(GL_TRIANGLES)
    glColor3f(0.6, 0.3, 0.1)
    glVertex2f(-30, -100)
    glVertex2f(-30, -20)
    glVertex2f(30, -100)
    
    glVertex2f(30, -100)
    glVertex2f(-30, -20)
    glVertex2f(30, -20)
    glEnd()
    
    # Window (using GL_TRIANGLES)
    glBegin(GL_TRIANGLES)
    glColor3f(*window_color)
    # Window frame
    glVertex2f(-70, 0)
    glVertex2f(-70, 30)
    glVertex2f(-40, 0)
    
    glVertex2f(-40, 0)
    glVertex2f(-70, 30)
    glVertex2f(-40, 30)
    
    # Another window
    glVertex2f(40, 0)
    glVertex2f(40, 30)
    glVertex2f(70, 0)
    
    glVertex2f(70, 0)
    glVertex2f(40, 30)
    glVertex2f(70, 30)
    glEnd()
    
    # Window cross (using GL_LINES)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glColor3f(0.1, 0.1, 0.1)
    glVertex2f(-55, 0)
    glVertex2f(-55, 30)
    glVertex2f(-70, 15)
    glVertex2f(-40, 15)
    
    glVertex2f(55, 0)
    glVertex2f(55, 30)
    glVertex2f(40, 15)
    glVertex2f(70, 15)
    glEnd()

def draw_rain():
    """Draw rain drops and update their positions"""
    glPointSize(2.0)
    glBegin(GL_POINTS)
    for drop in rain_drops:
        glColor3f(*drop.color)
        glVertex2f(drop.x, drop.y)
    glEnd()
    
    # Draw rain lines (for better visibility)
    glLineWidth(1.0)
    glBegin(GL_LINES)
    for drop in rain_drops:
        glColor3f(*drop.color)
        # Calculate rain line based on angle
        end_x = drop.x + 7 * math.sin(math.radians(rain_angle))
        end_y = drop.y - 7 * math.cos(math.radians(rain_angle))
        glVertex2f(drop.x, drop.y)
        glVertex2f(end_x, end_y)
    glEnd()

def update_rain():
    """Update rain drop positions"""
    for drop in rain_drops:
        # Update position based on angle
        drop.x += 2 * math.sin(math.radians(rain_angle))
        drop.y -= 2 * math.cos(math.radians(rain_angle))
        
        # Reset position if rain drop goes out of window
        if drop.y < -W_Height/2:
            drop.y = W_Height/2
            drop.x = random.uniform(-W_Width/2, W_Width/2)
        
        # Reset position if rain drop goes out of sides
        if drop.x < -W_Width/2:
            drop.x = W_Width/2
            drop.y = random.uniform(0, W_Height/2)
        elif drop.x > W_Width/2:
            drop.x = -W_Width/2
            drop.y = random.uniform(0, W_Height/2)

def display():
    """Main display function"""
    # Clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(*background_color, 0)
    
    # Reset the model view matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Draw house and rain
    draw_house()
    draw_rain()
    update_rain()
    
    glutSwapBuffers()

def keyboard_listener(key, x, y):
    """Handle regular keyboard events"""
    global day_night_transition, background_color
    
    #Day/Night cycle
    if key == b'd':  # Day (lighter)
        day_night_transition = min(1.0, day_night_transition + 0.1)
        # Adjust background color
        background_color = [day_night_transition * 0.2, 
                           day_night_transition * 0.3, 
                           day_night_transition * 0.5]
        print(f"Day cycle: {day_night_transition:.1f}")
    elif key == b'n':  # Night (darker)
        day_night_transition = max(0.0, day_night_transition - 0.1)
        # Adjust background color
        background_color = [day_night_transition * 0.2, 
                           day_night_transition * 0.3, 
                           day_night_transition * 0.5]
        print(f"Night cycle: {day_night_transition:.1f}")
    
    glutPostRedisplay()

def special_key_listener(key, x, y):
    """Handle special keyboard events (arrow keys, etc.)"""
    global rain_angle
    
    #Left/Right arrows change rain angle
    if key == GLUT_KEY_RIGHT:
        rain_angle = min(45, rain_angle + 5)  # Limit to 45 degrees
        print(f"Rain angle: {rain_angle}")
    elif key ==GLUT_KEY_LEFT :
        rain_angle = max(-45, rain_angle - 5)  # Limit to -45 degrees
        print(f"Rain angle: {rain_angle}")
    
    glutPostRedisplay()

def init():
    """Initialize OpenGL settings"""
    # Clear the screen to black
    glClearColor(0.0, 0.0, 0.0, 1.0)
    
    # Set up the projection matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Set up orthographic projection
    glOrtho(-W_Width/2, W_Width/2, -W_Height/2, W_Height/2, -1.0, 1.0)
    
    # Initialize rain drops
    init_rain_drops()

def timer_func(value):
    """Timer function for animation"""
    glutPostRedisplay()
    glutTimerFunc(16, timer_func, 0)  # ~60 FPS

def main():
    """Main function"""
    glutInit()
    glutInitWindowSize(W_Width, W_Height)
    glutInitWindowPosition(100, 100)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    
    # Create window - Change name as per your ID before submission
    window = glutCreateWindow(b"Task 1: House in Rainfall")
    
    # Register callbacks
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard_listener)
    glutSpecialFunc(special_key_listener)
    glutTimerFunc(0, timer_func, 0)
    
    # Initialize
    init()
    
    # Enter the GLUT main loop
    glutMainLoop()

if __name__ == "__main__":
    main()
