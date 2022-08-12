exit=0
def add_ (x,y):
    print("\nadd of",x,"+",y,"=", x+y)
def sub_ (x,y):
    print("\nsub of",x,"-",y,"=", x-y)
def mul_ (x,y):
    print("\nmull of",x,"*",y,"=", x*y)
def div_ (x,y):
    if y!=0:
        print("\ndiv of",x,"/",y,"=", x/y)
    else :
        print("not defined")

while exit==0:
    print("\n ================================= \n ================================= \n ======= simple calculator ======= \n ================================= \n ================================= \n \n")
    fun=int(input("choose a function \n 1 : add \n 2 : sub \n 3 : mul \n 4 : div \n 0 : exit \n"))
    if fun==0:
        break
    x=int(input("enter 1st number"))
    y=int(input("enter 2nd number"))
    if fun==1:
        add_(x,y)
    elif fun==2:
        sub_(x,y)
    elif fun==3:
        mul_(x,y)
    elif fun==4:
        div_(x,y)
    elif fun==0:
        break
    else :
        print("select a valid function")
