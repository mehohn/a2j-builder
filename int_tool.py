#! /usr/bin/env python


import sys
import Tkinter
import tkFileDialog
import os
from Tkinter import *


root = Tk()

maxrow = 16



#master = Tk()

def callback():
    currdir = os.getcwd()
    savedir = tkFileDialog.asksaveasfilename(parent=root,defaultextension='.bin', initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print "You chose %s" % savedir
    return savedir

def callbackopen():
    currdir = os.getcwd()
    tempdir = tkFileDialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print "You chose %s" % tempdir
    return tempdir

def callback3():
    h = find_in_grid(root, 3, 0).get()
    print h

def find_in_grid(frame, row, column):
    for children in frame.children.values():
        info = children.grid_info()
        #note that rows and column numbers are stored as string
        print info['row']
        print info['column']
        if info['row'] == str(row) and info['column'] == str(column):
            return children
    return None

def makepage():
    temppage = "<PAGE NAME=\"" + pagename + "\" " + "TYPE=\"A2J\" "
    return temppage

def makevar(varname, vartext, varcomment):
    tempvar = "<VARIABLE NAME=\"" + varname + "\" TYPE=\"" + vartext + "\" COMMENT=\"" + varcomment + "\"/>"
    return tempvar

def makestep(stepnum, steptext):
    tempstep = "<STEP NUMBER=\"" + stepnum + "\"><TEXT>" + steptext + "</TEXT></STEP>"
    return tempstep

def makefield(fieldtext, fieldreq, fieldlabel, fieldname):
    tempfield =  "<FIELD TYPE=\"" + fieldtext +"\" REQUIRED=\"" + fieldreq + "\" CALCULATOR=\"false\"><LABEL>" + fieldlabel + "</LABEL><NAME>" + fieldname + "</NAME></FIELD>"
    return tempfield

def hello():
    print "hello!"

def maketable(nosteps, nopages, novars):
    sl = 0
    sl2 = 1
    so = 2
    sd = so + nosteps
    pl = sd + 1
    pl2 = sd + 2
    po = sd + 3
    pd = po + nopages
    vl = pd + 1
    vl2 = pd + 2
    vo = pd + 3
    vd = vo + novars
    em = vd + 1

    steptitle = Label(root, text="STEPS")
    stepadd = Button(root, text="Add Step", command = root.quit)
    stepnumber = Label(root, text="Step Number")
    steplabel = Label(root, text="Step Label")
    pagetitle = Label(root, text="PAGES")
    pageadd = Button(root, text="Add Page", command = root.quit)
    pagenumber = Label(root, text=" Number")
    pagelabel = Label(root, text="Step Label")
    vartitle = Label(root, text="VARIABLES")
    varadd = Button(root, text="Add Variable", command = root.quit)
    varnumber = Label(root, text="Step Number")
    varlabel = Label(root, text="Step Label")
    c = Button(root, text="Save", command=callback)
    d = Button(root, text="Open", command=callbackopen)
    e = Button(root, text="Value", command=callback3)
    f = Button(root, text="Quit", command=root.quit)

    steptitle.grid(row=sl, column=0)
    stepadd.grid(row=sl, column=1)
    stepnumber.grid(row=sl2, column=0)
    steplabel.grid(row=sl2, column=1)
    for i in range(so, sd): #Rows
        for j in range(2): #Columns
            b = Entry(root, text="")
            b.grid(row=i, column=j)
    
    pagetitle.grid(row=pl, column=0)
    pageadd.grid(row=pl, column=1)
    pagenumber.grid(row=pl2, column=0)
    pagelabel.grid(row=pl2, column=1)
    for i in range(po, pd): #Rows
        for j in range(5): #Columns
            b = Entry(root, text="")
            b.grid(row=i, column=j)
    
    vartitle.grid(row=vl, column=0)
    varadd.grid(row=vl, column=1)
    varnumber.grid(row=vl2, column=0)
    varlabel.grid(row=vl2, column=1)
    for i in range(vo, vd): #Rows
        for j in range(3): #Columns
            b = Entry(root, text="")
            b.grid(row=i, column=j)
    c.grid(row=em, column=0)
    d.grid(row=em, column=1)
    e.grid(row=em, column=2)
    f.grid(row=em, column=3)



#Create Step Grid
maketable(5, 5, 5)

'''
height = 5
width = 2
b2 = Label(root, text="Step Number")
b2.grid(row=0, column=0)
b3 = Label(root, text="Step Label")
b3.grid(row=0, column=1)
for i in range(1, height): #Rows
    for j in range(width): #Columns
        b = Entry(root, text="")
        b.grid(row=i, column=j)


height2 = height + 5
width = 5
for i in range(height, height2): #Rows
    for j in range(width): #Columns
        b = Entry(root, text="")
        b.grid(row=i, column=j)

l1.grid(row=maxrow - 1,column=0)
l2.grid(row=maxrow - 1,column=1)
l3.grid(row=maxrow - 1,column=2)
l4.grid(row=maxrow - 1,column=3)
c.grid(row=maxrow, column=0)
d.grid(row=maxrow, column=1)
e.grid(row=maxrow, column=2)
f.grid(row=maxrow, column=3)'''

menubar = Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=callbackopen)
filemenu.add_command(label="Save", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
#editmenu = Menu(menubar, tearoff=0)
#editmenu.add_command(label="Cut", command=hello)
#editmenu.add_command(label="Copy", command=hello)
#editmenu.add_command(label="Paste", command=hello)
#menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)



mainloop()

root.withdraw() #use to hide tkinter window
# = find_in_grid(root, 1, 1).get()
#print d



#tkFileDialog.asksaveasfilename([options]).


