#! /usr/bin/env python


import sys
import Tkinter
import tkFileDialog
import os
from Tkinter import *


root = Tk()

height = 5
width = 5
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Entry(root, text="")
        b.grid(row=i, column=j)


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
    h = find_in_grid(root, 1, 1).get()
    print h

def find_in_grid(frame, row, column):
    for children in frame.children.values():
        info = children.grid_info()
        #note that rows and column numbers are stored as string                                                                         
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

c = Button(root, text="Save", command=callback)
c.grid()

d = Button(root, text="Open", command=callbackopen)
d.grid()

e = Button(root, text="Value", command=callback3)
e.grid()


mainloop()

root.withdraw() #use to hide tkinter window
# = find_in_grid(root, 1, 1).get()
#print d



#tkFileDialog.asksaveasfilename([options]).


