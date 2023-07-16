import os
import os.path

DIR_IN = "templating/"
DIR_OUT = "docs/"

def firstfile(p):
    return next(os.path.join(p, s) for s in os.listdir(p) if not os.path.isdir(os.path.join(p,s)))

def onlydirs(p):
    return (os.path.join(p, s) for s in os.listdir(p) if os.path.isdir(os.path.join(p, s)))

def readpath(p):
    with open(p, "r") as f:
        return f.read()

def writepath(p, s):
    with open(p, "w") as f:
        f.write(s)


text = readpath(firstfile(DIR_IN))
i = text.find('></div>')+1
wrapping = (text[:i], text[i:])

for dirp in onlydirs(DIR_IN):
    dname = os.path.basename(dirp)
    fp = firstfile(dirp)
    fname = os.path.basename(fp)

    i = wrapping[0].find('></title>')+1
    w = (wrapping[0][:i] + fname + wrapping[0][i:], wrapping[1])
    p = os.path.join(DIR_OUT, dname + ".html")
    writepath(p, readpath(fp).join(w))
    print("writing ", p)

print("ok")

