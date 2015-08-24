

import time

dasht = 1
dott = 0.20
lettert = 0.40
wordt = 1.3
# The whole magic happens here so be sure that this is the right file.
# This is the file to which we write on or off to play with led.
path = "/proc/acpi/ibm/led"

# Switch off the led

def off():
    f = open(path, 'w')
    f.write('0 off')
    f.close()
    print "-"

# Switch on the led
def on():
    f = open(path, 'w')
    f.write('0 on')
    f.close()
    print "."
    


def dash():
    off()
    on()
    time.sleep(dasht)
    off()

def dot():
    off()
    on()
    time.sleep(dott)
    off()


#Definetion of letters in morse code
def a():
    dot()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    time.sleep(wordt)

def b():
    dash()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    time.sleep(wordt)

def c():
    dash()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    time.sleep(wordt)

def d():
    dash()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    time.sleep(wordt)

def e():
    dot()
    time.sleep(lettert)
    time.sleep(wordt)
    
def f():
    dot()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    time.sleep(wordt)

def g():
    dash()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    time.sleep(wordt)

def h():
    dot()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    time.sleep(wordt)

def i():
    dot()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    time.sleep(wordt)

def j():
    dot()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    time.sleep(wordt)

def k():
    dash()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    time.sleep(wordt)

def l():
    dot()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    time.sleep(wordt)

def m():
    dash()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    time.sleep(wordt)

def n():
    dash()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    time.sleep(wordt)

def o():
    dash()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    time.sleep(wordt)

def p():
    dot()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    time.sleep(wordt)

def q():
    dash()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    time.sleep(wordt)

def r():
    dot()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    time.sleep(wordt)

def s():
    dot()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    time.sleep(wordt)

def t():
    dash()
    time.sleep(lettert)
    time.sleep(wordt)

def u():
    dot()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    time.sleep(wordt)

def v():
    dot()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    time.sleep(wordt)

def w():
    dot()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    time.sleep(wordt)

def x():
    dash()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)    
    dot()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    time.sleep(wordt)

def y():
    dash()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    dash()
    time.sleep(lettert)
    time.sleep(wordt)

def z():
    dash()
    time.sleep(lettert)    
    dash()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    dot()
    time.sleep(lettert)
    time.sleep(wordt)


def space():
    time.sleep(3)


# Dictionary of letters
letter = {"a":a, "b":b, "c":c, "d":d, "e":e, "f":f, "g":g, "h":h, "i":i, "j":j, "k":k, "l":l, "m":m, "n":n, "o":o, "p":p, "q":q, "r":r, "s":s, "t":t, "u":u, "v":v, "w":w, "x":x, "y":y, "z":z, "space":space}

userinput = raw_input()
userinput = userinput.lower()


for letters in userinput:
    if letters==" ":
        space()
        continue
    
    callme = letter[letters]
    
    #transmit the code
    callme()
    

