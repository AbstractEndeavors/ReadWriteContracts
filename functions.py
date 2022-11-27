import os
import json
from hexbytes import HexBytes
def copyIt(x,y):
    pen(reader(x),crPa([y,x.split(slash)[-1]]))
def changeGlob(x,v):
    globals()[x] = v
def isFold(x):
    return os.path.isdir(x)
def isFile(x):
    return os.path.isfile(x)
def homeIt():
    changeGlob('home',getCurrPath())
    slash = '//'
    if '//' not in str(home):
        slash = '/'
    changeGlob('slash',slash)
    return home,slash
def changeGears(x):
    changePath(x)
    return getCurrPath()
def changePath(x):
    os.path.abspath(x)
def eatOuter(x,ls):
    for i in range(0,len(x)):
        if x[-1] in ls:
            x = x[:-1]
        else:
            return x
def eatInner(x,ls):
    for i in range(0,len(x)):
        if x[0] in ls:
            x = x[1:]
        else:
            return x
def eatAll(x,ls):
    return eatInner(eatOuter(x,ls),ls)
def eatAllLs(ls,ls2):
    lsN = []
    for i in range(0,len(ls)):
        lsN.append(eatAll(ls[i],ls2))
    return lsN
def crPa(ls):
    if len(ls) == 1 or '' in ls:
        return ls[0]
    x,y = ls
    for i in range(1,len(x)):
        if x[-1] == slash:
            x = x[:-1]
    for i in range(0,len(y)):
        if y[0] == slash:
            y = y[1:]
    return x+slash+y
def isLs(ls):
    if type(ls) is list:
        return True
    return False
def mkLs(ls):
    if isLs(ls) == False:
        ls = [ls]
    return ls
def ifExPass(ls):
    ls =mkLs(ls)
    for i in range(0,len(ls)):
        n = cleanLs(ls[i].split('/'))
        y = n[i]
        for i in range(0,len(n)-1):
            if isFold(y) == False and isFile(y) == False and '.' not in y:
                mkDir(y)
            y = crPa([y,n[i]])
    return y
def createPath(ls):
    return crPa(ls[0],ls[1])
def getCurrPath():
    return os.getcwd()
def exists(x):
    try:
        x = reader(x)
        return True
    except:
        return False
def existsJs(x):
    try:
        x = jsIt(reader(x))
        return x
    except:
        return False
def unspl(x,y):
    n = ''
    for i in range(0,len(x)):
        n = n + y+x[i]
    return n
def delHomePath(x):
    spl = x.split(slash)
    ho = home.split(slash)
    for i in range(0,len(spl)):
        if spl[i] not in ho:
            return unspl(spl[i:],slash)
    return ''
def existsMake(x,y):
    if exists(y) == False:
        pen(x,ifExPass(crPa([home,y])))
        return x
    else:
        return reader(y)
def mkDirLsChk(ls,i):
    if len(ls) == 0 or i == 0 or len(ls) <=i:
        return ls[i]
    if len(ls) == 1 or len(ls)-1 == i:
        return mkDir(ls[i])
    else:
        return ls[i]
def isExt(x):
    if '.' in x:
        return True
    return False
def mkIfExt(ls):
    ls = mkLs(ls)
    if isExt(ls[-1]) == True:
       existMake(crPa(ls))
       return y
    return mkDir(crPa(ls))
def mkDirLs(ls):
    ls = mkLs(ls)
    y = mkIfExt(ls[0])
    for i in range(1,len(ls)):
        if isLs(ls[i]) == True:
            priv = changeGears(y)
            for k in range(1,len(ls[i])):
                mkDir(crPa([y,ls[i][k]]))
        else:
            y = mkIfExt([y,ls[i]])
            

    return y
def existsMakeJs(x,y):
    if exists(y) == False:
        pen(x,y)
        return jsIt(x)
    else:
        return jsIt(reader(y))
def reader(file):
    with open(file, 'r') as f:
        text = f.read()
        return text
def readerB(file):
    with open(file, 'r',encoding='UTF-8') as f:
        text = f.read()
        return text
def readerC(file):
    with open(file, "r",encoding="utf-8-sig") as f:
        text = f.read()
        return text
def penB(paper, place):
    with open(place, 'w',encoding='UTF-8') as f:
        f.write(str(paper))
        f.close()
        return
def pen(paper, place):
    with open(place, 'w') as f:
        f.write(str(paper))
        f.close()
        return
def remVar():
    if exists('variables/vars.txt') == True:
        delFile('variables/vars.txt')
def delFile(x):
    os.remove(x)
def removeIt(x):
    shutil.rmtree(x, ignore_errors=False, onerror=None)
def mkDir(x):
    os.makedirs(x, exist_ok = True)
    return x
def cleanLs(ls):
    lsN = []
    for i in range(0,len(ls)):
        if ls[i] != '':
            lsN.append(ls[i])
    return lsN
def checkSum(x):
    return Web3.toChecksumAddress(str(x))
def jsIt(x):
    return json.loads(str(x).replace("'",'"'))
def hx(x):
    x = "".join(["{:02X}".format(b) for b in HexBytes("0x"+str(x))])
    return x
def isInt(x):
    if type(x) is int:
        return True
    try:
        z = int(x)
        return True
    except:
        return False
def isHex(x):
    try:
        z = x.hex()
        return True
    except:
        return False
def printHex(x):
    if isHex(x):
        return x.hex()
    return x
homeIt()
