#! /usr/bin/env python


import sys
import Tkinter
import tkFileDialog
import os
from Tkinter import *


root = Tk()

maxrow = 16

STEPS = 1
PAGES = 1
VARS = 1

NOFS = 2
NOFP = 5
NOFV = 3

stepAry = []
pageAry = []
varAry = []
blankAry = []
entrylist = []
entrylistX = []
entrylistY = []

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
    h = find_in_grid(root, 3, 0)
#print h

def find_in_grid(frame, row, column):
    global entrylist, entrylistX, entrylistY, blankAry
    
    print "entrylist: "
    print entrylist
    print "STEPS: %d" % STEPS
    print "PagesO %d" % PAGES
    print "Vars: %d" % VARS
    g = 0
    blankAry = []
    ent = []
    while(g < len(entrylistX)):
        if g < (STEPS * NOFS):
            ent = []
            for field in range(0, NOFS):
                ent.append(entrylist[g + field].get())
            blankAry.append(ent)
            #blankAry.append([entrylist[i].get(), entrylist[i+1].get()])
            g = g + NOFS
        elif g < (PAGES * NOFP) + (STEPS * NOFS):
            ent = []
            for field in range(0, NOFP):
                ent.append(entrylist[g + field].get())
            blankAry.append(ent)
            #blankAry.append([entrylist[i].get(), entrylist[i+1].get()])
            g = g + NOFP
        else:
            ent = []
            for field in range(0, NOFV):
                ent.append(entrylist[g + field].get())
            blankAry.append(ent)
            g = g + NOFV
    print "array "
    print blankAry
    '''for children in frame.children.values():
        info = children.grid_info()
        #note that rows and column numbers are stored as string
        print info['row']
        print info['column']
        if info['row'] == str(row) and info['column'] == str(column):
            return children'''
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

def addstep():
    global STEPS
    STEPS = STEPS + 1
    maketable(STEPS, PAGES, VARS)

def addpage():
    global PAGES
    PAGES = PAGES + 1
    maketable(STEPS, PAGES, VARS)

def addvar():
    global VARS
    VARS = VARS + 1
    maketable(STEPS, PAGES, VARS)

def substep():
    global STEPS
    if STEPS > 1:
        STEPS = STEPS - 1
        maketable(STEPS, PAGES, VARS)

def subpage():
    global PAGES
    if PAGES > 1:
        PAGES = PAGES - 1
        maketable(STEPS, PAGES, VARS)

def subvar():
    global VARS
    if VARS > 1:
        VARS = VARS - 1
        maketable(STEPS, PAGES, VARS)

def e2aStep(e):
    return e - 2

def e2aPage(e):
    global STEPS
    return e - 4 - STEPS

def e2aVar(e):
    global STEPS
    global PAGES
    return e - 6 - STEPS - PAGES

def a2eStep(a):
    return a + 2

def a2ePage(a):
    global STEPS
    return a + 4 + STEPS

def a2eVar(a):
    global STEPS
    global PAGES
    return a + 6 + STEPS + PAGES

def maketable(nosteps, nopages, novars):
    for label in root.grid_slaves():
        label.grid_forget()
    
    
    global NOFS, NOFP, NOFV, stepAry, pageAry, varAry, entrylist, entrylistX, entrylistY, blankAry

    entrylist = []
    entrylistX = []
    entrylistY = []
    
    sl = 0
    sl2 = 1
    so = 2
    sd = so + nosteps
    pl = sd + 0
    pl2 = sd + 1
    po = sd + 2
    pd = po + nopages
    vl = pd + 0
    vl2 = pd + 1
    vo = pd + 2
    vd = vo + novars
    em = vd + 1

    steptitle = Label(root, text="STEPS")
    stepadd = Button(root, text="Add Step", command = addstep)
    stepsub = Button(root, text="Remove Step", command = substep)
    stepnumber = Label(root, text="Step Number")
    steplabel = Label(root, text="Step Label")
    pagetitle = Label(root, text="PAGES")
    pageadd = Button(root, text="Add Page", command = addpage)
    pagesub = Button(root, text="Remove Page", command = subpage)
    pagenumber = Label(root, text=" Number")
    pagelabel = Label(root, text="Step Label")
    vartitle = Label(root, text="VARIABLES")
    varadd = Button(root, text="Add Variable", command = addvar)
    varsub = Button(root, text="Remove Variable", command = subvar)
    varnumber = Label(root, text="Variable Name")
    varlabel = Label(root, text="Variable Type")
    c = Button(root, text="Save", command=callback)
    d = Button(root, text="Open", command=callbackopen)
    e = Button(root, text="Run", command=callback3)
    f = Button(root, text="Exit", command=root.quit)

    steptitle.grid(row=sl, column=0)
    stepadd.grid(row=sl, column=1)
    stepsub.grid(row=sl, column=2)
    stepnumber.grid(row=sl2, column=0)
    steplabel.grid(row=sl2, column=1)
    for i in range(so, sd): #Rows
        print "i: %d" % i
        print "steps: %d" % STEPS
        for j in range(NOFS): #Columns
            b = Entry(root, text="")
            if blankAry != [] and i <= a2eStep(STEPS) :
                b.insert(END, '%s' % blankAry[e2aStep(i)][j])
            else:
                b.insert(END, '%s.%s' % (i, j))
            entrylist.append(b)
            entrylistX.append(i)
            entrylistY.append(j)
            b.grid(row=i, column=j)
    
    pagetitle.grid(row=pl, column=0)
    pageadd.grid(row=pl, column=1)
    pagesub.grid(row=pl, column=2)
    pagenumber.grid(row=pl2, column=0)
    pagelabel.grid(row=pl2, column=1)
    for i in range(po, pd): #Rows
        for j in range(NOFP): #Columns
            b = Entry(root, text="")
            if blankAry != [] and i < e2aPage(i)+1:
                b.insert(END, '%s' % blankAry[e2aPage(i)][j])
            else:
                b.insert(END, '%s.%s' % (i, j))
            entrylist.append(b)
            entrylistX.append(i)
            entrylistY.append(j)
            b.grid(row=i, column=j)
    
    vartitle.grid(row=vl, column=0)
    varadd.grid(row=vl, column=1)
    varsub.grid(row=vl, column=2)
    varnumber.grid(row=vl2, column=0)
    varlabel.grid(row=vl2, column=1)
    for i in range(vo, vd): #Rows
        for j in range(NOFV): #Columns
            '''if j == 1:
                b = Listbox(root)
                b.insert(END, "Variable Type")

                for item in ["one", "two", "three", "four"]:
                    b.insert(END, item)
            else:'''
            b = Entry(root, text="")
            if blankAry != [] and i < e2aVar(i)+1:
                b.insert(END, '%s' % blankAry[e2aVar(i)][j])
            else:
                b.insert(END, '%s.%s' % (i, j))
            entrylist.append(b)
            entrylistX.append(i)
            entrylistY.append(j)
            b.grid(row=i, column=j)
    c.grid(row=em, column=0)
    d.grid(row=em, column=1)
    e.grid(row=em, column=2)
    f.grid(row=em, column=3)



#Create Step Grid
maketable(STEPS, PAGES, VARS)

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
filemenu.add_command(label="Run", command=root.quit)
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
root.title("A2J Builder")


mainloop()

root.withdraw() #use to hide tkinter window
# = find_in_grid(root, 1, 1).get()
#print d



#tkFileDialog.asksaveasfilename([options]).


