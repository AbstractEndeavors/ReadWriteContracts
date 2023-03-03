import functions as ff
import web3
from web3 import Web3, HTTPProvider
import json
def homeIt():
    changeGlob('home',os.getcwd())
    slash = '//'
    if '//' not in str(home):
        slash = '/'
    changeGlob('slash',slash)
    return home,slash
def changeGlob(x,v):
    globals()[x] = v
def getKeys(js):
    lsN = []
    for key, value in js.items():
        lsN.append(key)
    pen(lsN,'rpckeys.txt')
def tryCheckSum(x):
    try:
        y = w3.toChecksumAddress(x)
        return y
    except:
        return False
def checkIfDud(x):
    if  x != None:
        if len(x)>0:
            if len(x) >1:
                  return x
    return False
def countIt(x,y):
    if y not in x:
        return 0
    return int((len(x)-len(x.replace(y,'')))/len(y))
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
def createInps(ls):
    n = '('
    for i in range(0,len(ls)):
        n = n + ls[i]+ ','
    n = n.replace(' ','__').replace('[]','ls') + ')'
    return n.replace(',)',')')
def stripWeb(x):
    if 'http' in x:
        x = x.replace('https','').replace('http','')
        while x[0] in [':',slash] and len(x)>1:
            x = x[1:]
    return x.split(slash)[0]
def extractRPCdata(js):
    kes = ['nativeCurrency', 'network', 'RPC', 'chainId', 'blockExplorer']
    for i in range(0,len(kes)):
        if kes[i] not in js:
            js[kes[i]] = ""
    changeGlob('nativeCurrency',js['nativeCurrency'])
    changeGlob('network',js['network'])
    changeGlob('blockExplorer',js['blockExplorer'])
    changeGlob('RPC',js['RPC'])
    changeGlob('chainId',js['chainId'])
    changeGlob('scanner',stripWeb(js['blockExplorer']))
    return nativeCurrency,network,RPC,chainId,blockExplorer,scanner,Web3(Web3.HTTPProvider(js['RPC']))
def getTypes(varis):
    spl,n = str(varis)[1:-1].split(','),''
    for k in range(0,len(spl)):
        typ = spl[k].split('__')[0]
        if typ[-len('ls'):] == 'ls':
            if 'int' in  typ:
                ty = 'int'
            elif 'bytes' in typ:
                ty = 'bytes'
            elif 'address' in typ:
                ty = 'address'
            elif 'bool' in typ:
                ty = 'bool'
            else:
                ty = 'str'    
            n = n + 'ifLs("'+str(ty)+'",'+str(spl[k])+'),'
        elif 'int' in  typ:
            n = n + 'int('+str(spl[k])+'),'
        elif 'bytes' in typ:
            n = n + 'kek('+str(spl[k])+'),'
        elif 'bool' in typ:
            n = n + 'bool('+str(spl[k])+'),'
        else:
            n = n + 'str('+str(spl[k])+'),'
    return '('+n[:-1]+')'
def parse_it(add,path,contract,abi,main):
    nativeCurrency,network,RPC,chainId,explorer,scanner,w3 = extractRPCdata(main)
    ff.pen(add,'currInfo.txt')
    import funGet as fun
    js = json.loads(fun.getFuns(path,contract,abi))
    symbol = 'cont'
    call = []
    asks = []
    fun_sheet = ''
    view_sheet = 'def view_all():\n\t'
    js['varis'] = {'view_all':''}
    funs = js['funs']
    funsWhole =  js['function']
    funnames = funsWhole['names']
    lsN = ['view_all()']
    for i in range(0,len(funnames)):
        name = str(funnames[i])
        varis = str(createInps(funsWhole[name]['inputs']))
        js['varis'][name] = varis[1:-1]
        wholeFun = str(name + varis)
        lsN.append(wholeFun)
        if varis == '()' and name in js['view']:
            view_sheet = view_sheet +  'print("'+name+'",":",(cont.functions.'+wholeFun+'.call()))\n\t'
            fun_sheet = fun_sheet + 'def '+wholeFun+':\n\ttx = cont.functions.'+name+varis+'.call()\n\tprint("'+str(name)+' ="+str(tx))\n\treturn tx\n'
        else:
            call.append(wholeFun)
            vLs = str(varis)[1:-1]+'='+'ls\n\t'
            if countIt(varis,',') == 0:
                vLs = ''
                if len(str(varis)[1:-1]) != 0:
                    vLs = str(varis)[1:-1]+'='+'ls[0]\n\t'
            fun_sheet = fun_sheet + 'def '+str(name)+'(ls):\n\t'+str(vLs)+'tx = cont.functions.'+name+getTypes(varis)+".buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(account_1.address), 'from': w3.toChecksumAddress(add)}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})\n\tprint(tx)\n\treturn tx\n"
    if view_sheet == 'def view_all():\n\t':
        view_sheet = 'def view_all():\n\tprint()'
    fun_sheet = fun_sheet+'\ndef getDefVaris(na):\n\tjs = '+str(js['varis'])+'\n\treturn js[na].split(",")\n' +view_sheet
    get_em = [asks,call]
    fun_all = []
    for k in range(0,len(get_em)):
        for i in range(0,len(get_em[k])):
            n = 'funs.'+get_em[k][i].replace('[]','ls').replace(' ,',',').replace(', ',',').replace(' ','_')
            fun_all.append(n)
    fun_sheet = ff.reader('functionTemplate.txt').replace("^^^insertWallHome^^^",'"'+ff.crPa(home,'walls')+'"').replace('^^^^insertABI^^^^',"json.loads('"+str(abi)+"')").replace('^^^^insertFunctions^^^^',fun_sheet).replace('^^^^insertListOfFunctions^^^^',str(lsN)[1:-1]).replace('^^^^insertnativeCurrency^^^^','"'+nativeCurrency+'"').replace('^^^^insertNetwork^^^^','"'+network+'"').replace('^^^^insertRPC^^^^','"'+RPC+'"').replace('^^^^insertChainId^^^^',chainId).replace('^^^^insertBlockExplorer^^^^','"'+blockExplorer+'"').replace('^^^^insertNetworkName^^^^','"'+nativeCurrency+'"').replace('^^^^insertAddress^^^^',str('"'+add+'"'))
    ff.pen('import funcSheet as func\nwhile True:\n\ttry:\n\t\tfunc.hubbub()\n\texcept Exception as e:\n\t\tprint(e)',ff.crPa(path,'dothefunx.py'))
    return funs,asks,call,fun_all,fun_sheet
home,slash = ff.homeIt()
