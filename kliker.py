import mouse
from time import sleep


while(True):
    if mouse.is_pressed(button = 'left'):
        while(True):
            sleep(0.1)
            mouse.double_click(button = 'left')
    
