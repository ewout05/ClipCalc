import keyboard
import pyperclip
import time
import re

def safe_eval(expr):
    if not re.match(r'^[0-9+\-*/().\s]+$', expr):
        raise ValueError("Ongeldige karakters in formule")
    return eval(expr)

def wait_for_release():
    # Wacht tot zowel CTRL als Y NIET meer ingedrukt zijn
    while keyboard.is_pressed('ctrl') or keyboard.is_pressed('y'):
        time.sleep(0.01)

def on_hotkey():
    print("Ctrl+Y gedetecteerd… wachten tot losgelaten…")

    # WACHTEN TOT LOSGELATEN
    wait_for_release()
    print("Losgelaten → nu pas Ctrl+C uitvoeren")

    # Clipboard leegmaken
    pyperclip.copy("")

    # Kopiëren
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.05)

    formula = pyperclip.paste().strip()
    print(f"Geselecteerde formule: {formula}")

    if not formula:
        print("Niets geselecteerd")
        return

    try:
        result = safe_eval(formula)
    except Exception as e:
        print(f"Fout bij berekenen: {e}")
        return

    print(f"Resultaat: {result}")

    pyperclip.copy(str(result))
    time.sleep(0.05)

    keyboard.press_and_release('ctrl+v')
    print("Resultaat geplakt.")

keyboard.add_hotkey('ctrl+y', on_hotkey)

print("ClipCalc‑achtige formule‑calculator actief. Druk Ctrl+Y op een formule…")
keyboard.wait()