import pyautogui as pt
import pyperclip as pc
from time import sleep

# Whatsapp Bot - Python
class Bot:
    def __init__(self, speed=.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''
        
    # Function to navigate to the green dot 
    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen('green_dot.png', confidence=.6)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100, 0, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except:
            print('No green dot found')


W_bot = Bot(speed=.5, click_speed=.3)
sleep(2)
W_bot.nav_green_dot()                         