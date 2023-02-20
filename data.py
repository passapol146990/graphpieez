from pyscript import Element
from js import document 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# แปลงข้อมูล ถ้าเป็นตัวหนังสือจะได้ str ถ้าเป็นเลขจะได้ int,float
def check_type(type):
    try:
        if isinstance(int(type[0]),int):
            return setList_int(type)
    except:
        return setList_str(type)
# แปลงข้อมูลจาก srt --> list
def setList_int(x):
    x = str(x)+' '
    sums = []
    a = ''
    for i in x: # loop text
        if(i == ' '): # เช็คว่าเจอช่องว่างไหม
            if '.' in a : # ถ้ามี . ให้ใส่ทศนิยม
                sums.append(float(a))
            else:
                sums.append(int(a))
            a = ''
        else:
            a += i
    return sums

def setList_str(x):
    x = x+' '
    sums = []
    a = ''
    for i in x:
        if i == ' ':
            sums.append(a)
            a =''  
        else:
            a += i
    return sums

# ตัดข้อมูลของแกน X,Y ให้เท่ากัน
def lenList(x,y):
    x = x
    y = y
    while True:
        if(len(x) == len(y)):
            return x, y
        else:
            if len(x) > len(y):
                x.pop()
            else:
                y.pop()

# เรียกใช้กราฟวงกลม
def ok_g3(*args,**kwargs):
    x3 = Element('x3').value
    y3 = Element('y3').value

    title = Element('title3') # ploygraph

    t = [check_type(x3),check_type(y3)]
    fig, ax = plt.subplots()
    ax.pie(t[0],labels=t[1],autopct='%1.1f%%',startangle=90)

    title.write(fig)
    
def clear3(*args,**kwargs):
    title = Element('title3')
    title.element.innerHTML = "<div id='title3'></div>"    
