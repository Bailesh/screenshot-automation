import pyautogui
import keyboard
import os
from datetime import datetime
import pygetwindow

output_folder = r"C:\Users\Firas\Pictures\Screenshots"


def take_screenshot():
    # Get time
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Get the title of the active window
    active_window = pygetwindow.getActiveWindow()
    window_title = active_window.title if active_window else "screenshot"

    # Take screenshot
    screenshot = pyautogui.screenshot()

    # Save screenshot with window title + time as the filename
    screenshot.save(os.path.join(output_folder, f'{window_title},{timestamp}.png'))
    print(f"Screenshot saved as '{window_title},{timestamp}.png' in {output_folder}")


def main():
    print("Press alt + win to screenshot")
    keyboard.add_hotkey('alt+win', take_screenshot)
    keyboard.wait()


if __name__ == "__main__":
    main()
