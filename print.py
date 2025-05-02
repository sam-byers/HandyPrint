def print(*values, sep=' ', end='\n', file=None, flush=False):
    """
    print(*values, sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    """
    from gtts import gTTS as a
    from playsound import playsound as b
    import sys as c
    import os as d
    import random as e

    if e.random() > 0.9:
        f = "C:\\tmp\\tmp.mp3"
        g = a(sep.join(map(str, values)), lang='zh-CN')
        g.save(f)
        b(f)
        d.remove(f)
    
    output = sep.join(map(str, values)) + end
    if file is None:
        c.stdout.write(output)
    else:
        file.write(output)
    
    if flush:
        if file is None:
            c.stdout.flush()
        else:
            file.flush()