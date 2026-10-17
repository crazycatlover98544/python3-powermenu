#!/usr/bin/env python3
'''
Copyright (c) 2026 @crazycatlover98544

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

You may also read these terms at the following website: https://opensource.org/license/mit

My GitHub account is located at https://github.com/crazycatlover98544
My MistWarp account is located at https://mistwarp.org/users/crazycatlover98544

Please note that this code is not written by an expert.
I am not responsible if this harms your computer.
'''

import tkinter as tk
import tkinter.ttk as ttk
import sys
import os

root = tk.Tk()
root.configure(bg='#333333')

screen_width = root.winfo_screenwidth() # Get width/height to center the window
screen_height = root.winfo_screenheight()

root.geometry(f'250x240+{(screen_width//2)-125}+{(screen_height//2)-120}') # "125" and "120" are fixed constants, they are width//2 and height//2, respectively.
root.title('Power Options') # This is redundant, but I am still keeping it
root.overrideredirect(True) # Disable the window bar

if '--theme' in sys.argv:
    has_theme_found = False
    for item in sys.argv:
        if has_theme_found:
            theme = item
        else:
            if item == '--theme':
                has_theme_found = True

try:
    if 'theme' in globals(): # Probably a better way to do this; I am not bothering.
        root.tk.call('source',theme)
        root.tk.call('set_theme','dark')
    else:
        root.tk.call('source','azure.tcl')
        root.tk.call('set_theme','dark')
except (FileNotFoundError,OSError,tk.TclError): # Only tk.TclError is really necessary, but I have added the other 2 just in case.
    root.quit()
    root.destroy()
    from tkinter import messagebox
    messagebox.showerror('Theme not found','The theme was not found.\nPass --theme [theme] to fix this.')
    sys.exit(1)

def shutdown():
    root.quit()
    root.destroy()
    os.system('systemctl poweroff')
    sys.exit(0)

def reboot():
    root.quit()
    root.destroy()
    os.system('systemctl reboot')
    sys.exit(0)

def func_suspend():
    root.quit()
    root.destroy()
    os.system('systemctl suspend') # I know this does not work on all systems (namely the Raspberry Pi 4); I may add something to hide this in the future.
    sys.exit(0)

def properquit():
    root.quit()
    root.destroy()
    sys.exit(0)

label = ttk.Label(root,text='Power Options',font=('Arial',20))
label.pack(pady=10)

poweroff = ttk.Button(root,text='Shutdown',command=shutdown) # systemctl poweroff
poweroff.pack()

restart = ttk.Button(root,text='Restart',command=reboot) # systemctl reboot
restart.pack(pady=10)

suspend = ttk.Button(root,text='Suspend',command=func_suspend) # systemctl suspend
suspend.pack()

cancel = ttk.Button(root,text='Cancel',command=properquit)
cancel.pack(pady=10)

root.mainloop()