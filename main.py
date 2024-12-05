import pygame
import serial
import math
from collections import deque

# --- Configuration ---
PORT = "COM5"  # Replace with your Arduino's COM port
BAUD_RATE = 9600
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30

# --- Initialize Serial Communication ---
try:
    ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
    print(f"Connected to {PORT}")
except Exception as e:
    print(f"Error connecting to serial port: {e}")
    exit()

# --- Initialize Pygame ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Radar Visualization")
clock = pygame.time.Clock()

# Colors
BACKGROUND_COLOR = (0, 0, 0)
LINE_COLOR = (0, 255, 0)
OBJECT_COLOR = (255, 0, 0)
TEXT_COLOR = (255, 255, 255)

# Fonts
font_large = pygame.font.SysFont("Arial", 40)
font_small = pygame.font.SysFont("Arial", 25)

# Variables
angle = 0
distance = 0
max_distance = 80  # Max distance for radar visualization (in cm)
angle_history = deque(maxlen=50)  # Store up to 5 angles
distance_history = deque(maxlen=50)  # Store up to 5 distances

# --- Functions ---
def draw_radar():
    """Draws the radar grid and scanning lines."""
    center_x = SCREEN_WIDTH // 2
    center_y = SCREEN_HEIGHT // 2
    max_radius = SCREEN_WIDTH // 2 - 50  # Radius of the radar
    

    
    # Draw scanning angle lines (from 0° to 180°)
    for i in range(0, 181, 30):  # Step through 0 to 180 degrees
        angle = math.radians(i)  # Convert angle to radians
        x = center_x + max_radius * math.cos(angle)  # Calculate x based on angle
        y = center_y - max_radius * math.sin(angle)  # Calculate y based on angle
        pygame.draw.line(screen, LINE_COLOR, (center_x, center_y), (x, y), 2)  # Draw the line from center to edge

def draw_object():
    """Draws the detected object based on angle and distance as a continuous line."""
    center_x = SCREEN_WIDTH // 2
    center_y = SCREEN_HEIGHT // 2
    max_radius = SCREEN_WIDTH // 2 - 50
    
    # Convert distance to pixel size
    pixel_distance = distance * max_radius / max_distance
    
    if distance <= max_distance:
        # Convert polar coordinates (angle, distance) to Cartesian (x, y)
        x = center_x + pixel_distance * math.cos(math.radians(angle))
        y = center_y - pixel_distance * math.sin(math.radians(angle))
        
        # Add the new point to the history, will automatically remove the oldest when maxlen is reached
        angle_history.append(x)
        distance_history.append(y)

        # Draw a continuous line for the last 5 points
        for i in range(1, len(angle_history)):
            pygame.draw.line(screen, OBJECT_COLOR, (angle_history[i-1], distance_history[i-1]), 
                             (angle_history[i], distance_history[i]), 2)

def draw_text():
    """Displays the angle and distance text on the screen."""
    angle_text = font_large.render(f"Angle: {angle}°", True, TEXT_COLOR)
    distance_text = font_large.render(f"Distance: {distance} cm", True, TEXT_COLOR)
    
    screen.blit(angle_text, (20, SCREEN_HEIGHT - 100))
    screen.blit(distance_text, (20, SCREEN_HEIGHT - 50))

# --- Main Loop ---
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read data from Arduino
    try:
        if ser.in_waiting > 0:
            raw_data = ser.readline().decode('utf-8').strip()
            if ',' in raw_data:
                angle, distance = map(int, raw_data.split(','))
    except Exception as e:
        print(f"Serial Read Error: {e}")
    
    # Draw radar components
    draw_radar()
    draw_object()
    draw_text()

    pygame.display.flip()
    clock.tick(FPS)

# Clean up
ser.close()
pygame.quit()
