import keyboard
import pyperclip

notes_filename = "notes.txt"

def on_triggered():
    copied_text = pyperclip.paste()
    if copied_text:
        with open(notes_filename, "a") as notes_file:
            notes_file.write(copied_text + "\n")
            print("Copied content appended to notes.")

def listen_for_shortcut():
    # Set the desired shortcut key combination (Example: Ctrl + Alt + S)
    shortcut = "shift + alt + s"

    # Register the callback function for the shortcut
    keyboard.add_hotkey(shortcut, on_triggered)

    # Continuously listen for keyboard events
    keyboard.wait()


# Start listening for the shortcut
listen_for_shortcut()
