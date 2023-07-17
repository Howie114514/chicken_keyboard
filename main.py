import winsound
import keyboard
from threading import Thread

s="jntm"

def j():
    winsound.PlaySound("j.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)

def n():
    winsound.PlaySound("n.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)

def t():
    if s=="jntm":
        winsound.PlaySound("t.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    elif s=="ctrl":
        winsound.PlaySound("dance.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)

def m():
    winsound.PlaySound("m.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)

def c():
    global s
    winsound.PlaySound("sing.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    s="ctrl"

def r():
    global s
    winsound.PlaySound("rap.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    s="ctrl"

def q():
    global s
    winsound.PlaySound("basketball.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    s="jntm"

def callback(k:keyboard.KeyboardEvent):
    name=k.name
    if k.event_type=="down":
        if name=="j":
            j()
        elif name=="n":
            n()
        elif name=="t":
            t()
        elif name=="m":
            m()
        elif name=="c":
            c()
        elif name=="r":
            r()
        elif name=="q" or name=="l":
            q()

keyboard.on_press(callback=callback)
keyboard.wait()