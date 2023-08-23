import os
import os.path

DIR_IN = os.path.join(os.path.dirname(os.path.realpath(__file__)), "templating/")
DIR_OUT = os.path.join(os.path.dirname(os.path.realpath(__file__)), "docs/")

def firsthtml(p):
    return next(os.path.join(p, s) for s in os.listdir(p) if s.endswith('.html'))

def onlydirs(p):
    return (os.path.join(p, s) for s in os.listdir(p) if os.path.isdir(os.path.join(p, s)))

def readpath(p):
    with open(p, "r") as f:
        return f.read()

def writepath(p, s):
    with open(p, "w") as f:
        f.write(s)

make_cache = []
def make(dirp):
    if not make_cache:
        text = readpath(firsthtml(DIR_IN))
        i = text.find('<head>')+len('<head>')+1
        j = text.find('></body>')+1
        make_cache.extend([text[:i], text[i:j], text[j:]])

    (a, b, c) = make_cache
    w =  (a + readpath( os.path.join(dirp, 'head') ) + b, c)
    return readpath( firsthtml(dirp) ).join(w)

for dirp in onlydirs(DIR_IN):
    p = os.path.join(DIR_OUT, os.path.basename(dirp) + ".html")
    writepath(p, make(dirp))
    print("written ", p)

print("ok")

