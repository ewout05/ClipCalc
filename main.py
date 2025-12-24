import keyboard
import pyperclip
import time
import re

def safe_eval(expr):
    if not re.match(r'^[0-9+\-*/().\s]+$', expr):
        raise ValueError("Invalid characters detected")
    return eval(expr)

def wait_for_release():
    # Wait until both CTRL and Y are NO longer pressed
    while keyboard.is_pressed('ctrl') or keyboard.is_pressed('y'):
        time.sleep(0.01)

def on_hotkey():
    print("Ctrl+Y detected.. waiting for release")

    # WAITING FOR RELEASE
    wait_for_release()
    print("Released -> Ctrl+C")

    # Clear clipboard
    pyperclip.copy("")

    # Copy
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.05)

    formula = pyperclip.paste().strip()
    print(f"Selected formula: {formula}") 

    if not formula:
        print("Nothing selected")
        return

    try:
        result = safe_eval(formula)
    except Exception as e:
        print(f"Error by calculating: {e}")
        return

    print(f"Result: {result}")

    pyperclip.copy(str(result))
    time.sleep(0.05)

    keyboard.press_and_release('ctrl+v')
    print("Result pasted.")

keyboard.add_hotkey('ctrl+y', on_hotkey)

print("ClipCalc calculator active. Press Ctrl+Y on a formula")
keyboard.wait()