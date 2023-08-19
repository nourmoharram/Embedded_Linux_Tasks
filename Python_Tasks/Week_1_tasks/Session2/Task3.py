'''
Task description: Using Pyautogui do the next steps :
- install clangd from extension
- install c++ testmate  from extension
- install c++ helper  from extension
- install cmake  from extension
- install cmake tools  from extension

'''

import pyautogui
import time

# Wait for a few seconds 
time.sleep(3)


tools = ['clangd', 'c++ TestMate', 'c++ helper', 'cmake', 'cmake tools']
images = ['sc1.png', 'sc2.png', 'sc3.png','sc4.png']
counter = 0

for tool in tools:
    if tool == 'clangd':
        pyautogui.click(18, 256, 1, 1, button='left')
    else:
        pyautogui.click(18, 256, 2, 1, button='left')


    time.sleep(5)
    pyautogui.click(143, 86, 2, 0.25, button='left')
    pyautogui.press('backspace', presses=10)
    pyautogui.write(tool, interval=0.25)
    time.sleep(5)
    pyautogui.click(190, 148, 2, 0, button='left')
    time.sleep(15)  # wait between every extension

    button_found = False
    
    for image in images:
           
           if pyautogui.locateCenterOnScreen(image):
                button_found = True
                x,y=pyautogui.locateCenterOnScreen(image)
                print(x)
                print(y)
                if image == 'sc3.png' or image == 'sc4.png':
                     break
                else:
                    pyautogui.click(x,y, 1, 1, button='left')
                    break

    if  button_found==False:
        counter += 1
        print(f"Button not found for {tool}")

    time.sleep(15)

if counter == len(tools):
    print("Button Not Found for all tools")

print("Installation process completed.")
