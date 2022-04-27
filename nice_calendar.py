import calendar
import _tkinter as tk
from tkinter import Text, Tk
import tkinter

window = Tk()
window.title('Nice Calendar')
window.geometry('650x450')

year = tkinter.IntVar()
month = tkinter.IntVar()
hint = tkinter.StringVar()

def printLog(text):
    hint = print(text)
    hint_log.insert(hint)

def loadMonth():
    attempts = 0
    yearLoaded = year.get()
    monthLoaded = month.get()

    if monthLoaded > 12:
        while monthLoaded > 12:
            attempts = attempts+1

            if attempts == 1:
                printLog('i said from 1 to 12 ;_;')
                printLog("k let's try it again...")
            else:
                printLog('you know that a year has just 12 months right?')
                printLog("k bro one more time...")

            monthLoaded = int # this is to not show the previous value on the terminal
            monthLoaded = int(input(monthLoaded))

    month_result = print(calendar.month(yearLoaded,monthLoaded))
    month_result = tkinter.Label(window,text = print('{}'.format(month_result)),font = ('Futura Md BT',12,'normal'))
    month_result.grid(row = 4,column = 2)


label_year = tkinter.Label(window,text = 'Year (any A.C. one): ',font = ('Futura Md BT',12,'normal'))
label_year.grid(row = 1,column = 1)
entry_year = tkinter.Entry(window,textvariable = year,font = ('Futura Md BT',12,'normal'))
entry_year.grid(row = 1,column = 2)

label_month = tkinter.Label(window,text = 'Month (from Jan to Dec - 1 to 12): ',font = ('Futura Md BT',12,'normal'))
label_month.grid(row = 2,column = 1)
entry_month = tkinter.Entry(window,textvariable = month,font = ('Futura Md BT',12,'normal'))
entry_month.grid(row = 2,column = 2)

btn_loadCalendar = tkinter.Button(window,text = 'Load this month!',command = loadMonth)
btn_loadCalendar.grid(row = 3,column = 2)

# hint_log = tkinter.Entry(window,textvariable = '',font = ('Futura Md BT',12,'normal'),state = ['readonly'])
# hint_log.grid(row = 4,column = 1)

hint_log = Text(window,font = ('Futura Md BT',12,'normal'),width = 25,height = 2)
hint_log.grid(row = 4,column = 1)

month_result = tkinter.Label(window,text = 'The month is supposed to be displayed here',font = ('Futura Md BT',12,'normal'))
month_result.grid(row = 5,column = 2)

window.mainloop()