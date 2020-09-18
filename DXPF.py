# Import utils
import misc.EUtil as EUtil

# Clear The Screen
EUtil.clearScreen()

# Import misc
import misc.helper as helper
import misc.logger as logger
import misc.db as db

# Choosing Colors
SuccessColor = helper.bcolors.OKBLUE
FailColor = helper.bcolors.FAIL
HeaderColor = helper.bcolors.HEADER

# Import base modules needed for reading database
print(HeaderColor + "\n[[ IMPORTING OS ]]")
try:
    import os
    print(SuccessColor + "\nLOADED SUCCESSFULLY!")
except Exception as e:
    print(FailColor + "\nFAILED TO LOAD... ERROR: {}".format(e))

print(HeaderColor + "\n[[ IMPORTING TIME ]]")
try:
    import time
    print(SuccessColor + "\nLOADED SUCCESSFULLY!")
except Exception as e:
    print(FailColor + "\nFAILED TO LOAD... ERROR: {}".format(e))

print(HeaderColor + "\n[[ IMPORTING RANDOM.CHOICE ]]")
try:
    from random import choice
    print(SuccessColor + "\nLOADED SUCCESSFULLY!")
except Exception as e:
    print(FailColor + "\nFAILED TO LOAD... ERROR: {}".format(e))

# Import pynput for emulating keyboard
print(HeaderColor + "\n[[ IMPORTING PYNPUT.MOUSE AND PYNPUT.KEYBOARD ]]")
try:
    from pynput import mouse, keyboard
    from pynput.mouse import Button
    from pynput.keyboard import Key
    print(SuccessColor + "\nLOADED SUCCESSFULLY!")
except Exception as e:
    print(FailColor + "\nFAILED TO LOAD... ERROR: {}".format(e))
    print(HeaderColor + "\n[[ DOWNLOADING PYNPUT ]]")

    if os.system("python3 -m pip install --user pynput") == 0:
        print(SuccessColor + "\nDOWNLOADED SUCCESSFULLY!")
        print(HeaderColor + "\n[[ IMPORTING PYNPUT.MOUSE AND PYNPUT.KEYBOARD ]]")
        from pynput import mouse, keyboard
        from pynput.mouse import Button
        from pynput.keyboard import Key
        print(SuccessColor + "\nLOADED SUCCESSFULLY!")
    else:
        print(FailColor + "\nFAILED TO DOWNLOAD...")

# Class definition for everything to exist in one place
class DXPF:
    '''
    This is a class allowing easy way of making macros
    '''
    # Initialization of class
    def __init__(self):
        # Get Database
        self.DB = db.DB()

        # Get Mouse and Keyboard Controller
        self.mc = mouse.Controller()
        self.kc = keyboard.Controller()

        # Set a typing speed in second
        self.speed = 0.1

        # Set a delay before every writing in seconds
        self.delay = 61

        # Set a default mouse position
        self.mousePosition = (500,500)

    # Print Current Mouse Posistion
    def getCurrentPosition(self, savePos=False):
        '''
        Used to print current position of mouse.
        '''
        print("Mouse Position: {}".format(self.mc.position))

        # Check If Position Should Be Saved
        if savePos:
            self.mousePosition = self.mc.position

    # Write now
    def startWriting(self, mousePos=False):
        '''
        By Calling This Function, The Bot Start! 
        '''
        print(helper.bcolors.WARNING + "\n\nRUNNING ON WHILE LOOP, DO CTRL + C TO CANCEL...")
        log = 0
        while True:
            time.sleep(self.delay)
            toSay = choice(self.DB)
            if mousePos != False:
                self.mc.position = mousePos
            else:
                self.mc.position = self.mousePosition
            
            self.mc.press(Button.left)
            self.mc.release(Button.left)

            for i in toSay:
                self.kc.press(i)
                self.kc.release(i)
                time.sleep(self.speed)
            
            self.kc.press(Key.enter)
            self.kc.release(Key.enter)

            print("\nMessage #{}: {}".format(log, toSay))
            log += 1

if __name__ == "__main__":
    d = DXPF()
    d.getCurrentPosition(savePos=True)
    d.startWriting()
