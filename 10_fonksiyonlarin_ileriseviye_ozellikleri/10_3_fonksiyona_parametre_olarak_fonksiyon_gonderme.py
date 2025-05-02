def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1, f2, f3, f4, islemadi):

    if(islemadi=="toplama"):
        print(f1(2,3))
    elif(islemadi=="cikarma"):
        print(f2(2,3))     
    elif(islemadi=="carpma"):
        print(f3(2,3))
    elif(islemadi=="bolme"):
        print(f4(2,3))
    else:
        print("geçersiz işlem")

islem(toplama,cikarma,carpma,bolme,"toplama")
islem(toplama,cikarma,carpma,bolme,"cikarma")
islem(toplama,cikarma,carpma,bolme,"carpma")
islem(toplama,cikarma,carpma,bolme,"bolme")