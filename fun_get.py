import json
import functions as f
def getKey(js):
    lsN = []
    for key, value in js.items():
        lsN.append(str(key))
    return lsN
def eatIt(x):
    for i in range(0,len(x)):
        if x[0] not in [' ','\t','n','']:
            return x 
        x = x[1:]
    return x
def ifIt(k,lsN):
        return ls
def ifThen(n):
        ls = ['type','name','inputs','payable','stateMutability','output']
        
        for i in range(0,len(ls)):
                if ls[i] in n and ls[i] != False :
                        lsN.append(n[ls[i]])
        n = ''
        for i in range(0,len(lsN)):
              n = n + ifIt(i,lsN)
              print(n)
        print(n)            
        return lsN
def ifNoJs(js,x):
    if x not in js:
        js[x] = {}
    return(js)
def ifNols(js,x):
    if x not in js:
        js[x] = []
    return(js)
def ifNoApp(ls,x):
    if x not in ls:
        ls.append(x)
    return(ls)
def ifIn(x,y):
        if y in x:
                return True
        return False
def ifLen(x,y):
        if y not in x:
                return ''
        if len(x[y])>0:
                return True
        return False
def iLen(i,x):
        if len(x) != i + 1:
                return ' , '
        return ') '
def tOf(x,y):
        if y not in x:
                return ''
        if x[y] == False:
                return ''
        return y
def addItStr(x,y) :
    return str(x) + str(y)
def getInp(x,js):
        n = ''
        if ifLen(x,'type') and ifIn(x,'type'):
                n = n + x['type']
                type = x['type']
                js = ifNoJs(js,type)
                js[type] = ifNols(js[type],'names')
        if ifLen(x,'name') and ifIn(x,'name'):
                name = x['name']
                n = n+' '+name+'('
                js[type]['names'] = ifNoApp(js[type]['names'],name)
                js[type] = ifNoJs(js[type],name)
        else:
            name = 'NA'
            js[type] = ifNoJs(js[type],'NA')
        js[type][name]['inputs'] = []
        if ifLen(x,'inputs') and ifIn(x,'inputs'):
                for i in range(0,len(x['inputs'])):
                        inp = ''
                        if ifLen(x['inputs'][i],'type') and ifIn(x['inputs'][i],'type'):
                                inp = addItStr(inp,x['inputs'][i]['type'])
                        if ifLen(x['inputs'][i],'name') and ifIn(x['inputs'][i],'name'):
                                inp = addItStr(inp,' '+x['inputs'][i]['name'])
                        js[type][name]['inputs'].append(inp)
                        n = addItStr(n,inp+',')
        n = addItStr(n, ') '+tOf(x,'payable')+' ')
        js[type][name]['stateMutability'] = 'public'
        if ifLen(x,'stateMutability') and ifIn(x,'stateMutability'):
                n = addItStr(n,x['stateMutability'])
                js[type][name]['stateMutability'] = x['stateMutability']
                if x['stateMutability'] == 'view' and x['type'] == 'function':
                    js['view'].append(x['name'])
        js[type][name]['outputs'] = []
        if ifLen(x,'outputs') and ifIn(x,'outputs'):
                 n = addItStr(n,' returns(')
                 for i in range(0,len(x['outputs'])):
                         out = ''
                         if ifLen(x['outputs'][i],'type') and ifIn(x['outputs'][i],'type'):
                                out = addItStr(out,x['outputs'][i]['type'])
                         if ifLen(x['outputs'][i],'name') and ifIn(x['outputs'][i],'name'):
                               out = addItStr(out,x['outputs'][i]['name'])
                         js[type][name]['outputs'].append(out)
                         n = addItStr(n,out+',')
                 n = n + ')'
        n = n+ ' {}'
        return js,n
def getFuns(path):
        contract = f.reader(path.replace('ABI.json','SourceCode.json')).replace('\n','').replace('function','\nfunction').replace('{','\n{').split('\n')
        js = {'funs':[],'modified':{'onlyOwner()':[]},'view':[]}
        for i in range(0,len(contract)):
            if 'onlyOwner' in contract[i] and 'function' in contract[i]:
                js['modified']['onlyOwner()'].append(contract[i].split('function ')[1].split('(')[0])
        abi = json.loads(str(f.reader(path)))
        lsN = []
        for i in range(0,len(abi)):
            ab = abi[i]
            js,fun = getInp(ab,js)
            if ifLen(ab,'type') and ifIn(ab,'type'):
                if ab['type'] == 'function':     
                    js['funs'].append(fun.replace(',)',')').replace('  ',' '))
        f.pen(js,f.createPath(path.replace(path.split('/')[-1],''),'allWallVar.json'))
        return js,js['funs']

                
