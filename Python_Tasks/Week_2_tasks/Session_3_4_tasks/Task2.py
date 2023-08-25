#import keyboard library to monitor keyboard events
import keyboard
#import pyperclip library to access copied data in clipboard
import pyperclip

# The filename for notes
notes_filename = "notes.txt"

# A flag to indicate when to append clipboard content to notes
append_to_notes = False
# A flag to end the program execution
End_Program = True

# function used as a callback function to be called everytime a key pressed on keyboard and monitor which keys pressed
def on_key_event(event):
    global append_to_notes, End_Program  # Declare them as global
    
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == "s" and keyboard.is_pressed("alt+shift"):
            append_to_notes = True
            print("Append to notes: ", append_to_notes)
        elif event.name == "e" and keyboard.is_pressed("alt+shift"):
            End_Program = False
            print("Program End")

#function to copy the copied data from clipboard to notes.txt
def append_copied_text():
    global append_to_notes
    
    if append_to_notes:
        copied_text = pyperclip.paste()
        if copied_text:
            with open(notes_filename, "a") as notes_file:
                notes_file.write(copied_text + "\n")
            print("Copied content appended to notes.")
        append_to_notes = False

#hook to observe the keyboard events
keyboard.hook(on_key_event)

#program main loop that iterate infinite till the flag of end program change to false using alt+shift+e
try:
    while End_Program:
        append_copied_text()
except KeyboardInterrupt:
    pass
