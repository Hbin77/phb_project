from pynput import keyboard

def on_press(key):
    try:
        if key.char == 'q':
            print("q pressed")
            return False  # Stop listener
    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
