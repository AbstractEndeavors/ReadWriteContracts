import os
def copyIt(x,y):
    pen(reader(x),createPath([y,x.split(slash)[-1]]))
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
def createJsLs(ls,js):
    for i in range(0,len(ls)):
        js[ls[i]] = []
    return js
def changeGlob(x,v):
    globals()[x] = v
def getCurrPath():
    return os.getcwd()
def homeIt():
    changeGlob('home',getCurrPath())
    slash = '//'
    if '//' not in str(home):
        slash = '/'
    changeGlob('slash',slash)
    return home,slash
def checkIfDud(x):
    if  x != None:
        if len(x)>0:
            if len(x) >1:
                  return x
    return False
def eatX(x):
    if checkIfDud(x) != False:
        while x[-1] == slash and len(x)>1:
            x = x[:-1]
    return x
def eatY(y):
    if checkIfDud(y) != False:
        while y[0] == slash and len(y) >1:
            y[1:]
    return y
def createPath(x,y):
    return eatX(x)+'/'+eatY(y)
def isFold(x):
    return os.path.isdir(x)
def listFolds(x):
    ls = os.listdir(x)
    lsN = []
    for i in range(0,len(ls)):
        if isFold(createPath(x,ls[i])):
            lsN.append(ls[i])
    return lsN
def jsIt(x):
    return json.loads(str(x).replace("'",'"'))
def copyAndStart(path):
        copyIt(createPath(path,'funcSheet.py'),'currFun')
        copyIt(createPath(path,'Info.json'),'currFun')
        copyIt(createPath(path,'allCalls.json'),'currFun')
        copyIt(createPath(path,'ABI.json'),'currFun')
        import currFun.funcSheet as func
        allCalls = f.jsIt(f.readerC(createPath('currFun','allCalls.json')))
        if guiNet.simpleBool('would you like to view all viewable variables in the contract?'):
            find.createAsk(func.view_all())
        ex = createInp(allCalls['call'])
def checkVarFold():
    varis = {'adds': {'all': []}, 'networks': [],'jsAll':{'names':[],'contracts':{}}}
    varis['adds'] = {}
    varis['adds']['all'] = []
    varis['netNames'] = listFolds('variables')
    varis = createJsLs(varis['netNames'],varis)
    for i in range(0,len(varis['netNames'])):
        netName = varis['netNames'][i]
        netNamefold = createPath('variables',netName)
        currFolds = listFolds(netNamefold)
        if 'netNames' not in varis:
            varis['netNames'] = []
        if netName not in varis[netName]:
            varis[netName] = {}
            varis['netNames'].append(netName)
        for kk in range(0,len(currFolds)):
            currNet = currFolds[kk]
            currNetsfold = createPath(netNamefold,currNet)
            chainIds = listFolds(currNetsfold)
            if 'currNets' not in varis[netName]:
                varis[netName]['currNets'] = []
            if currNet not in varis[netName]:
                varis[netName][currNet] = {}
                varis[netName]['currNets'].append(currNet)
            for k in range(0,len(chainIds)):
                chainId = chainIds[k]
                chainIdFold = createPath(currNetsfold,chainId)
                adds = listFolds(chainIdFold)
                if 'chainIds' not in varis[netName][currNet]:
                    varis[netName][currNet]['chainIds'] = []
                if chainId not in varis[netName][currNet]:
                    varis[netName][currNet][chainId] = {}
                    varis[netName][currNet]['chainIds'].append(chainId)
                for c in range(0,len(adds)):
                    addr = adds[c]
                    rpcFold = createPath(chainIdFold,addr)
                    rpcs = listFolds(rpcFold)
                    if 'addrs' not in varis[netName][currNet][chainId]:
                        varis[netName][currNet][chainId]['addrs'] = []
                    if addr not in varis[netName][currNet][chainId]:
                        varis[netName][currNet][chainId][addr] = {}
                        varis[netName][currNet][chainId]['addrs'].append(addr)
                    for j in range(0,len(rpcs)):
                        rpcN = rpcs[j]
                        path = createPath(rpcFold,rpcN)
                        if 'rpcs' not in varis[netName][currNet][chainId][addr]:
                            varis[netName][currNet][chainId][addr]['rpcs'] = []
                        if rpcN not in varis[netName][currNet][chainId][addr]:
                            varis[netName][currNet][chainId][addr][rpcN] = {}
                            varis[netName][currNet][chainId][addr]['rpcs'].append(rpcN)
                        if False not in [f.exists(createPath(path,'funcSheet.py')),f.exists(createPath(path,'Info.json')),f.exists(createPath(path,'allCalls.json')),f.exists(createPath(path,'ABI.json'))]:
                            varis['adds']['all'].append(addr)
                            varis['adds'][addr] = path
                            Info = jsIt(f.reader(createPath(path,'Info.json')))
                            name = Info['name']
                            if name not in varis['jsAll']['contracts']:
                                varis['jsAll']['contracts'][name] = {'RPCs':[],'SourceCode':[]}
                            if name not in varis['jsAll']['names']:
                                varis['jsAll']['names'].append(name)
                                varis['jsAll']['contracts'][name] = {}
                                varis['jsAll']['contracts'][name]['RPCs'] = [Info['RPC']]
                                varis['jsAll']['contracts'][name]['SourceCode'] = [Info]
    pen(varis,createPath('variables','varis.json'))
    return varis
homeIt()
print(checkVarFold())
