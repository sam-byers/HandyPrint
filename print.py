
def print(input):
    from gtts import gTTS
    from playsound import playsound
    import sys
    import os
    import random
    accList = [
        "com.au",
        "co.uk",
        "com.ng",
        "co.za",
        "co.in"
    ]

    if random.random() > 0.6:
        filepath = "C:\\tmp\\tmp.mp3"
        # line = gTTS(input, lang='en', tld=accList[random.randint(0,len(accList) - 1)])
        line = gTTS(input, lang='zh-CN')
        line.save(filepath)
        playsound(filepath)
        os.remove(filepath)
    sys.stdout.write(input + '\n')
    sys.stdout.flush()