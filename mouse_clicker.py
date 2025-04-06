import pyautogui
import keyboard
import time

def auto_click(x, y):
    try:
        while True:
            # Move the mouse to the specified position
            pyautogui.moveTo(x, y)
            # Perform a mouse click
            pyautogui.click()
            # Wait for a short period to avoid overloading
            time.sleep(0.1)
            # Check if the Escape key has been pressed
            if keyboard.is_pressed('esc'):
                print("Escape key pressed. Exiting.")
                break
    except KeyboardInterrupt:
        print("Program interrupted by user. Exiting.")

if __name__ == "__main__":
    # Set the target position (example: center of a 4K screen)
    # Centrer :x_position = 1980,y_position = 1080
    #x_position = 2260  # x coordinate
    #y_position = 1800  # y coordinate
    #x_position = 1980  # x coordinate
    #y_position = 1950  # y coordinate
    x_position = 1980
    y_position = 1080
    #x_position = 1980
    #y_position = 1380
    #x_position = 1480
    #y_position = 1300
    #x_position = 1480
    #y_position = 1480

    print("Press the Escape key to stop.")
    auto_click(x_position, y_position)
