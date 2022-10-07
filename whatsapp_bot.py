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
        except Exception as e:
            print('No green dot found : ', e)

    # nagivate to the input box
    def nav_input_box(self):
        try:
            position = pt.locateOnScreen('paperclip.png', confidence=.6)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100, 10, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('No input box found : ', e)

    # navigate to last message
    def nav_last_message(self):
        try:
            position = pt.locateOnScreen('paperclip.png', confidence=.6)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(50, -60, duration=self.speed)
        except Exception as e:
            print('message not found : ', e)

    # copies the message
    def copy_message(self):
        try:
            pt.tripleClick(interval=self.click_speed)
            pt.hotkey('ctrl', 'c')
            self.message = pc.paste()
            print(self.message)
        except Exception as e:
            print('message not copied : ', e)

    # navigate to the send button
W_bot = Bot(speed=.5, click_speed=.3)
sleep(2)
W_bot.nav_last_message()
W_bot.copy_message()                         