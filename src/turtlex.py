#
# Python convenience functions to control turtle window appearance and behaviour.
#
# Copyright (c) Robots in Schools Ltd. All rights reserved.
#

def front(screen, alwaysAtFront=False):
    screen._root.attributes("-topmost", True)
    if not alwaysAtFront:
        screen._root.attributes("-topmost", False)

def fullscreen(screen, full=True):
    screen._root.attributes("-fullscreen", full)

def opacity(screen, alpha=0.5):
    screen._root.attributes("-alpha", alpha)

def disabled(screen, disabled=True):
    screen._root.attributes("-disabled", disabled)

def toolwindow(screen, tool=True):
    screen._root.attributes("-toolwindow", tool)

def noresize(screen, x=False, y=False):
    screen._root.resizable(x, y)

def nodecorate(screen, nodecorate=True):
    screen._root.overrideredirect(nodecorate)

def minsize(screen, width=None, height=None):
    screen._root.minsize(width, height)

def maxsize(screen, width=None, height=None):
    screen._root.maxsize(width, height)

def minimise(screen):
    screen._root.iconify()
def minimize(screen):
    minimise(screen)

def maximise(screen):
    screen._root.deiconify()
def maximize(screen):
    maximise(screen)