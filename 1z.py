import re

def getarg(s, i, state):
    
    j = 0
    arg = 0
    mass = {'+', '*', '-', '/'} 
    
    if state==0:
        while s[i] not in mass:
            arg += int(s[i])*pow(10, j)
            i-=1
            j+=1
    else:
        while i >= 0:
            arg += int(s[i])*pow(10, j)
            i-=1
            j+=1
            
    return arg, i

def count(a1, a2, z):
    res = 0
    int(a1)
    int(a2)
    if z == '+':
        res = a1+a2
    elif z == '*':
        res = a1*a2
    elif z == '-':
        res = a1-a2
    else:
        res = a1/a2
    return res


def getres(s):    
    i = len(s)-1

    arg1, i = getarg(s, i, 0)
    znak = s[i]    
    i-=1
    arg2, i = getarg(s, i, 1) 
    return count(arg1, arg2, znak)
    

print('Hello')
def main():
    s = input()
    
    s = re.sub(' ', '', s)
    if re.findall('\d+[+*-/]\d+', s):
        res = getres(s)
        print(s, '=', res)
    else: 
        print("Некорректный ввод")
        
main()
