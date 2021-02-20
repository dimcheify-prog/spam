import pyautogui, time

time.sleep(5)
f = open("text", 'r')
spam = True
for word in f:
    while spam:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        pyautogui.PAUSE = 0.000000000000000000000000000001