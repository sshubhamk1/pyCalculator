            #import module

from tkinter import *
import math

def sums(a,b):
    return a+b
def diff(a,b):
    return b-a
def mult(a,b):
    return a*b
def divs(a,b):
    return a/b
def mod(a,b):
    return a%b
def power(a,b):
    return a**b
def sqrroot():
    return math.sqrt(a)
def absolute(a):
    return abs(a)
def ceil(a):
    return math.ceil(a)
def floor(a):
    return math.floor(a)
def exp(a):
    return math.exp(a)
def log(a):
    return math.log(a)
def floordivision(a,b):
    return a//b
def sin(a):
    return math.sin(a)
def cos(a):
    return math.cos(a)
def tan(a):
    return math.tan(a)
def asin(a):
    return math.asin(a)
def acos(a):
    return math.acos(a)
def atan(a):
    return math.atan(a)
def operations(a,b,op):
    if op =='+':
        return sums(a,b)
    elif op=='-':
        return diff(a,b)
    elif op=='*':
        return mult(a,b)
    elif op=='div':
        return divs(b,a)
    elif op=='%':
        return mod(a,b)
    elif op=='pow':
        return power(a,b)
    elif op=='sqrt':
        return sqrroot(a)
    elif op=='exp':
        return exp(a)
    elif op=='Log':
        return log(a)
    elif op=='sin':
        return sin(a)
    elif op=='cos':
        return cos(a)
    elif op=='tan':
        return tan(a)
    elif op=='asin':
        return asin(a)
    elif op=='acos':
        return acos(a)
    elif op=='atan':
        return atan(a)
    return
flag=0
temp1=''
temp2=''
opcode=''
result=''

def flush():
    global temp1
    global temp2
    global opcode
    global result
    global flag
    temp1=''
    temp2=''
    opcode=''
    result=''
    flag = 0
    return
top = Tk()
top.title("Calculator")
top.minsize(275,335)
top.maxsize(275,335)
flush()
menu=Label(top,width=33,relief='raised',bg='red',fg='white',text='student\'s calculator')
menu.pack()
display = Label(top,width=15,relief='sunken',bg='white')
display.config(text='00000000000')
display.pack()
def takenum(val):
        global temp1
        temp1=temp1[:]+val
        displays(temp1)
        return
def displays(valu):
    display.config(text=valu)
def equal():
    global temp1,temp2,opcode
    if temp2=='':
        #print("single value")
        displays(temp1)
    else:
        #print('double value')
        result=operations(float(temp1),float(temp2),opcode)
        displays(str(result))
        flush()
    return
def clr():
    global temp1
    global temp2
    global flag
    if(flag==0):
        temp1 = temp1[:len(temp1)-1]
        displays(temp1)
    else:
        temp2 = temp2[:len(temp2)-1]
        displays(temp2)
    return
def takefns(val):
    global flag,temp1,temp2,result,opcode
    if(flag==0):
        temp2 = float(temp1[:])
        #print(temp2)
        temp1 =''
        flag=1
        opcode= val
        displays(temp1)
    elif(flag==1):
        #print("sec2")
        #print(temp1)
        #print(temp2)
        temp1 = float(temp1)
        temp2 = str(operations(float(temp2),float(temp1),val))
        opcode=val
        displays(temp2)
        temp1 = ''
        flag=1
main= Frame(top,width=50,height=200)
main.pack()
one= Button(main,width=10,height=1,text='1',bg='black',fg='white',relief='raised',command=lambda:takenum('1'))
one.grid(row=0,column=0,columnspan=1)
two= Button(main,width=10,height=1,text='2',bg='black',fg='white',relief='raised',command=lambda:takenum('2'))
two.grid(row=0,column=1,columnspan=1)
three= Button(main,width=10,height=1,text='3',bg='black',fg='white',relief='raised',command=lambda:takenum('3'))
three.grid(row=0,column=2,columnspan=1)
four= Button(main,width=10,height=1,text='4',bg='black',fg='white',relief='raised',command=lambda:takenum('4'))
four.grid(row=1,column=0,columnspan=1)
five= Button(main,width=10,height=1,text='5',bg='black',fg='white',relief='raised',command=lambda:takenum('5'))
five.grid(row=1,column=1,columnspan=1)
six= Button(main,width=10,height=1,text='6',bg='black',fg='white',relief='raised',command=lambda:takenum('6'))
six.grid(row=1,column=2,columnspan=1)
seven= Button(main,width=10,height=1,text='7',bg='black',fg='white',relief='raised',command=lambda:takenum('7'))
seven.grid(row=2,column=0,columnspan=1)
eight= Button(main,width=10,height=1,text='8',bg='black',fg='white',relief='raised',command=lambda:takenum('8'))
eight.grid(row=2,column=1,columnspan=1)
nine= Button(main,width=10,height=1,text='9',bg='black',fg='white',relief='raised',command=lambda:takenum('9'))
nine.grid(row=2,column=2,columnspan=1)
plus= Button(main,width=10,height=1,text='+',bg='black',fg='white',relief='raised',command=lambda:takefns('+'))
plus.grid(row=3,column=0,columnspan=1)
zero= Button(main,width=10,height=1,text='0',bg='black',fg='white',relief='raised',command=lambda:takenum('0'))
zero.grid(row=3,column=1,columnspan=1)
dot= Button(main,width=10,height=1,text='.',bg='black',fg='white',relief='raised',command=lambda:takenum('.'))
dot.grid(row=3,column=2,columnspan=1)

mul= Button(main,width=10,height=1,text='*',bg='black',fg='white',relief='raised',command=lambda:takefns('*'))
mul.grid(row=4,column=0,columnspan=1)
div= Button(main,width=10,height=1,text='/',bg='black',fg='white',relief='raised',command=lambda:takefns('div'))
div.grid(row=4,column=1,columnspan=1)
exp= Button(main,width=10,height=1,text='exp',bg='black',fg='white',relief='raised',command=lambda:takefns('exp'))
exp.grid(row=4,column=2,columnspan=1)
log= Button(main,width=10,height=1,text='log',bg='black',fg='white',relief='raised',command=lambda:takefns('log'))
log.grid(row=5,column=0,columnspan=1)
sin= Button(main,width=10,height=1,text='sin',bg='black',fg='white',relief='raised',command=lambda:takefns('sin'))
sin.grid(row=5,column=1,columnspan=1)
cos= Button(main,width=10,height=1,text='cos',bg='black',fg='white',relief='raised',command=lambda:takefns('cos'))
cos.grid(row=5,column=2,columnspan=1)
tan= Button(main,width=10,height=1,text='tan',bg='black',fg='white',relief='raised',command=lambda:takefns('tan'))
tan.grid(row=6,column=0,columnspan=1)
asin= Button(main,width=10,height=1,text='asin',bg='black',fg='white',relief='raised',command=lambda:takefns('asin'))
asin.grid(row=6,column=1,columnspan=1)
acos= Button(main,width=10,height=1,text='acos',bg='black',fg='white',relief='raised',command=lambda:takefns('acos'))
acos.grid(row=6,column=2,columnspan=1)
atan= Button(main,width=10,height=1,text='atan',bg='black',fg='white',relief='raised',command=lambda:takefns('atan'))
atan.grid(row=6,column=2,columnspan=1)
clears= Button(main,width=10,height=1,text='clear',bg='black',fg='white',relief='raised',command=clr)
clears.grid(row=7,column=0,columnspan=1)
minus= Button(main,width=10,height=1,text='-',bg='black',fg='white',relief='raised',command=lambda:takefns('-'))
minus.grid(row=7,column=1,columnspan=1)
equals= Button(main,width=10,height=1,text='=',bg='red',fg='green',relief='raised',command=equal)
equals.grid(row=7,column=2,columnspan=1)
top.mainloop()
