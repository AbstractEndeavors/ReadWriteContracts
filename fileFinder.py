import json
import os.path
import shutil
import json
from web3 import Web3
import os
import time
import stat
import subprocess
import shutil
def delFile(x):
    os.remove(x)
def foldList(x):
    return os.listdir(x)
def removeIt(x):
    shutil.rmtree(x, ignore_errors=False, onerror=None)
def mkDir(x):
    os.makedirs(x, exist_ok = True)
    return x
def currPath():
    return os.getcwd()
def home_it():
    curr = currPath()
    slash = '//'
    if '//' not in str(curr):
        slash = '/'
    changeGlob('slash',slash)
    changeGlob('home',curr)
    return home
def changeGlob(x,v):
    globals()[x] = v
#HomeFunctions---------------------------------------------------------------------------------------------------------------------------------------------------------------
def removeFromList(x,y):
    i = findIt(x,y)
    if i == len(y):
        return y[:-1]
    ls = []
    for i in range(0,len(y)):
        if y[i] != x:
            ls.append(y[i])
    return ls
def openFileExplorer(x):
    x ='open '+x
    subprocess.Popen(x, shell=True)
def allSizeDays(x,ls,i):
    return timeSpacing(ls,i,str(calcTimeInDays(foldTime(x,ls,i))),str(calcKb(foldSize(x,ls,i))))
def getFolder(inp,x,hidden,typeDisplay):
    exit = False
    n = x
    while exit != True:
        x = x.split(' ')[0]
        changeGlob('lsAll',{'home':str(x),'all':foldList(x),'files':[],'folds':[],'gets':[],'type':typeDisplay})
        filterFandF()
        if hidden == True:
            removeHiddenFolders()
        ask = create_ask(lsAll['folds'],inp)
        if ask == "exit":
            exit == True
        elif ask == "back":
            n = buildToSplitLast(n,slash)
        elif  ask == "open":
            openFileExplorer(x)
        elif str(ask) in lsAll['folds']:
            n = n+slash+ask
        else:
            n = n+slash+ask
        if isFold(n) == True and ask != 'back':
            if boolAsk(fileInputString(splitTo(n,slash,-1))) != False:
                return n
        x = n+slash        
#ASKfunctions-----------------------------------------------------------------------------
def createAlphLs(ls):
     return createAlph(len(ls)),ls
def getNumList(ls):
    lsN = []
    for i in range(0,len(ls)):
        lsN.append(i)
    return [lsN,ls]
def createAskLs(lsAlph,lsCalls):
    n = ''
    for i in range(0,len(lsCalls)):
        n = n + str(lsAlph[i])+') '+ lsCalls[i]+'\n'
    return n
def mergeLists(ls,ls2):
    for i in range(0,len(ls2)):
        ls.append(ls2[i])
    return ls
def mergeLss(lsNum,lsAlph,inquiry):
    nums = getNumList(lsNum)
    alphs = createAlphLs(lsAlph)
    n = inquiry[0]+'\n'
    if len(lsNum) >0:
        n = createAskLs(nums[0],nums[1])
        n = n +inquiry[0]+'\n'
    n = n + createAskLs(alphs[0],alphs[1])
    lsAll = mergeLists(nums[0],alphs[0])
    return lsAll,n,alphs,nums
def isInt(x):
    if type(x) is int:
        return True
    try:
        z = int(x)
        return True
    except:
        return False
def isAnyTypeInLS(x,ls):
    if isInt(x):
        if int(x) in ls:
            return True
    if str(x).lower() in lowerList(ls):
        return True
    if str(x).upper() in higherList(ls):
        return True
    if x in ls:
        return True
    return False

def createAsk(js):

    lsAll,n,alphs,nums= mergeLss(js['calls'][0],js['asks'][0],js['inq'])
    while True:
        ask = input(n)
        if isAnyTypeInLS(ask,lsAll):
            if isInt(ask) == True :
                return js['calls'][1][int(ask)]
            else:
                return js['asks'][1][int(findItStr(str(ask),createAlph(len(js['asks'][0]))))]
        print('looks like you entered an input that was not selectable,please re-input your selection')
def boolAsk(x):
    yes = ['y','yes','true','t','','0']
    no = ['n','no','false','f','1']
    ask = input(x+'\n0) yes\n1) no\n')
    ask = str(ask).lower()
    if isAnyTypeInLS(ask,yes):
        return True
    return False
def isFile(x):
    return os.path.isfile(x)
def buildToSplitLast(x,y):
    nSpl = splitIt(x,y)
    n = ''
    if nSpl != False:
        for i in range(0,len(nSpl)-1):
            n += nSpl[i] + y
        return removeLast(n,y)
    return x
def removeFromList(x,y,i):
    newLs = []
    if i == int(-1):
        for l in range(0,len(x)):
            if y not in x[l]:
                newLs.append(x[l])
    else:
        for l in range(0,len(x)):
            if y != x[l][i]:
                newLs.append(x[l])
    return newLs

def fileInputString(x):
    return "is "+str(x)+" the file you would like to choose?"

def splitTo(x,spl,i):
    tryIt = x
    num = splitNum(x,spl)
    keepUp = True
    while keepUp == True:
        if i == -1 and num == 1:
            return x
        tryIt = x.split(spl)[i]
        if num > i:
            if fileInputString(tryIt) != False:
                return tryIt
            
            i +=1
def isTypeFile(x,path,ls):
    lsN,lsN2 = [],[]
    for i in range(0,len(ls)):
        if isFile(createPath(path,ls[i])):
            if x in ls[i]:
                lsN.append(ls[i])
        if isFold(createPath(path,ls[i])):
            lsN2.append(ls[i])
    for i in range(0,len(lsN)):
        lsN2.append(lsN[i])
    return lsN2
def fileAsk():
    while True:
        file = str(AnyAsk(['please enter a file path','enter here: ']))
        if file == 'exit':
            return file
        if isFile(file) == True:
            if '.py' not in file.split(slash)[-1]:
                if boolAsk('looks as if the file '+str(x.split(slash)[-1])+' is not a python file, did you want to continue anyway?'):
                    return file
            else:
                return file
        else:
            print('looks like that is not a recognized file')
def lowerList(x):
    lsN = []
    if isLs(x) == False:
        x = [x]
    for i in range(0,len(x)):
        lsN.append(str(x[i]).lower())
    return lsN
def higherList(x):
    lsN = []
    if isLs(x) == False:
        x = [x]
    for i in range(0,len(x)):
        lsN.append(str(x[i]).upper())
    return lsN
def AnyAsk(x):
    if len(x) == 2:
        inp = x[0]+'\n0) exit\n'+x[1]
    else:
        inp = x+'\n0) exit\n'
    ask = input(inp)
    if ask == '0':
        return 'exit'
    return ask
#CleanStrings--------------------------------------------------------------------------------------------------------------------------------------------
def findIt(x,ls):
    if len(ls) == 0:
        return False
    if x  == ls[0]:
        return 0
    for i in range(0,len(ls)):
        if x == ls[i]:
            return i
def findItStr(x,ls):
    if len(ls) == 0:
        return False
    if str(x)  == str(ls[0]):
        return 0
    for i in range(0,len(ls)):
        if str(x) == str(ls[i]):
            return i

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def calcTimeInDays(x):
    return str(round((getTime()-x)/(60*24*60),2))+' days'
def calcKb(x):
    return str(round(x/1000,2))+' kb'
def foldTime(x,ls,i):
    return os.stat(x+'/'+ls[i])[9]
def foldSize(x,ls,i):
    return os.stat(x+'/'+ls[i])[6]
def timeSpacing(x,i,time,size):
    teb = ' \t'
    h = x[i]
    var = [time,size]
    teb = '             '
    exSpace = len(str()+teb)-len(str(x[i]))
    for k in range(0,2):
        te = ' \t'
        if k ==0:
            te = ' \t'
            now = exSpace-(len(x)+len(te))
            take = int(now)/len(' ')
            for c in range(0,int(exSpace)):
                h = h+' '
        h = h+te+var[k]
    return  h
def createAlph(i):
    k = int(i/int(26) + 1)
    alph = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')
    alphNew = []
    alLen = i
    for l in range(0,k):
        lenNow = i
        if i>int(26):
            lenNow = int(26)
        for c in range(0,lenNow):
            n = alph[c]
            for ck in range(0,l):
                n = n + alph[c]
            alphNew.append(n)
        i -=1
    return alphNew
def isFold(x):
    return os.path.isdir(x)
def splitIt(x,y):
    if str(y) in str(x):
        return x.split(y)
    return False
def removeLast(x,y):
    if x.replace(x[0:-len(y)],'') == y:
        return x[0:-len(y)]
    return x
def splitNum(x,spl):
    return len(x.split(spl))
def createPath(x,y):
    x = eatOuterMod(x,[slash,' ',''])
    y = eatInnerMod(y,[slash,' ',''])
    return x+slash+y
def getTime():
    return time.time()
def eatInnerMod(x,ls):
    if strInList(x,ls) != False:
        x = strInList(x,ls)
    return x
def eatOuterMod(x,ls):
    if strInListRev(x,ls) != False:
        x = strInListRev(x,ls)
    return x
def isLs(x):
    if type(x) is list:
        return True
    return False
def strInList(x,ls):
    if ifOverZero(x) == True:
        if x[0] in ls:
            return x[1:]
    return False
def strInListRev(x,ls):
    if ifOverZero(x) == True:
        if x[-1] in ls:
            return x[:-1]
    return False
def ifOverZero(x):
    if len(x) >1:
        return True
    return False
def getLists():
    lsA = lsAll['folds'],lsAll['files']
    for k in range(0,len(lsA)):
        ls,lsN = lsA[k],[]
        for i in range(0,len(ls)):
            lsN.append(allSizeDays(lsAll['home'],ls,i))
            lsAll['gets'].append(lsN[-1])
def currateFiles(spec):
    ls = lsAll['files']
    lsN = []
    for i in range(0,len(ls)):
        if ls[i][-len(spec):] == spec:
            lsN.append(ls[i])
    lsAll['files'] = lsN
def removeHiddenFolders():
    ls = lsAll['folds']
    lsN = []
    for i in range(0,len(ls)):
        if ls[i][0] != '.':
            lsN.append(ls[i])
    lsAll['folds'] = lsN
def listQuery(ask):
    x = lsAll['home']
    n =''
    ex = False
    if ask == "exit":
        return True
    elif ask == "back":
        x = buildToSplitLast(x,slash)
    elif  ask == "open":
        openFileExplorer(x)
    elif  ask == "old":
        return getFolder('which folder would you like to choose?',x)
    elif ask == "custom":
        x = str(fileAsk())
        if x == 'exit':
            return True
    elif lsAll['type'] == 'file' and str(ask) in lsAll['file']:
        a,ask,ex = checkFile(createPath('file',ask))
    elif lsAll['type'] == 'fold' and str(ask) in lsAll['fold']:
        a,ask,ex = checkFold(createPath('file',ask))
    else:
       ask = x+slash+ask
    return x,ask,ex
def filterFandF():
    ls = lsAll['all']
    for i in range(0,len(ls)):
        if isFold(createPath(lsAll['home'],ls[i])) == True:
            lsAll['folds'].append(ls[i])
        if isFile(createPath(lsAll['home'],ls[i])) == True:
            lsAll['files'].append(ls[i])
def fileAsk(ls):
    ask = create_ask(ls,'current Directory '+str(lsAll['home'])+'\nwhich '+lsAll['type']+'would you like to use?')
    return str(ask.split(' ')[0])
def foldAsk(ls):
    ask = create_ask(ls,'current Directory '+str(lsAll['home'])+'\nwhich '+lsAll['type']+'would you like to use?')
    return str(ask.split(' ')[0])
def checkFold(n):
    ex = False
    if isFold(n) == True:
        if boolAsk(fileInputString(splitTo(n,slash,-1))) == False:
            n = buildToSplitLast(n,slash)
        else:
            return n
    return n+slash,n,boolIt
def checkFile(n):
        ex = False
        if isFile(n) == True:
            boolIt = boolAsk(fileInputString(splitTo(n,slash,-1)))
            if boolIt == False:
            	n = buildToSplitLast(n,slash)
            else:
                return lsAll['home'],n,True
        return n+slash,n,boolIt
def displayFiles(x,curate,hidden,typeDisplay):
    ex = False
    while ex != True:
        x = x.split(' ')[0]
        changeGlob('lsAll',{'home':str(x),'all':foldList(x),'files':[],'folds':[],'gets':[],'type':typeDisplay})
        filterFandF()
        if hidden == True:
            removeHiddenFolders()
        if len(curate) > 0:
            currateFiles(curate)
        getLists()
        if lsAll['type'] == 'file':
            ex = fileAsk(lsAll[typeDisplay])
        else:
            ex = foldAsk(lsAll[typeDisplay])
        x,n,ex = listQuery(ex)
    return x,n
home_it()

