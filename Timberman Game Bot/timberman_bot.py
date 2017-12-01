"""
- Sharad Bhat
- 3rd November, 2017
"""

from PIL import ImageGrab, Image
import pyautogui
import time

class Timberman():
    def __init__(self):
        self.image = None

    def get_screen(self):
        self.image = ImageGrab.grab(bbox = (536, 69, 1063, 860))

    def get_data(self):
        left = self.image.crop((66, 364, 201, 457))
        right = self.image.crop((330, 364, 460, 457))

        return left, right

    def is_branch(self, branch):
        pixel = branch.getpixel((68, 28))

        return pixel == (162, 149, 65)

    def run(self):
        previous = "left"
        while True:
            time.sleep(0.035)
            self.get_screen()
            left, right = self.get_data()

            if self.is_branch(left):
                previous = "right"
                pyautogui.press("right")
                print("right")

            elif self.is_branch(right):
                previous = "left"
                pyautogui.press("left")
                print("left")

            else:
                pyautogui.press(previous)
                print("none")


if __name__ == '__main__':
    timber = Timberman()
    timber.run()
