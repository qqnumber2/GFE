import time
import random
import pyautogui


def move_mouse_smoothly(dest_x, dest_y, steps=25, duration_range=(0.01, 0.03)):
    """Move the mouse to (dest_x, dest_y) in small steps with jitter."""
    start_x, start_y = pyautogui.position()
    for i in range(steps):
        t = i / float(steps)
        intermediate_x = start_x + (dest_x - start_x) * t + random.uniform(-3, 3)
        intermediate_y = start_y + (dest_y - start_y) * t + random.uniform(-3, 3)
        dt = random.uniform(*duration_range)
        pyautogui.moveTo(intermediate_x, intermediate_y, duration=dt)
    pyautogui.moveTo(dest_x, dest_y, duration=random.uniform(*duration_range))


def random_mouse_move(screen_width, screen_height):
    """Move to a random point on the screen."""
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    move_mouse_smoothly(x, y)


def random_clicker(target_x, target_y, interval_range=(1.0, 3.0)):
    """Continuously move around randomly and click the target at random intervals."""
    screen_width, screen_height = pyautogui.size()
    try:
        while True:
            random_mouse_move(screen_width, screen_height)
            move_mouse_smoothly(target_x, target_y)
            pyautogui.click()
            time.sleep(random.uniform(*interval_range))
    except KeyboardInterrupt:
        print("Stopped")


if __name__ == "__main__":
    screen_width, screen_height = pyautogui.size()
    target_x = screen_width // 2
    target_y = screen_height // 15
    random_clicker(target_x, target_y, interval_range=(1, 299))
