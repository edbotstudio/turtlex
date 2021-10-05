#
# Python convenience functions to control turtle window appearance and behaviour.
#
# Copyright (c) Robots in Schools Ltd. All rights reserved.
#

#
# Send the window to the top of the window stack. If 'alwaysAtFront' is true
# then keep the window at the front.
#
def front(screen, alwaysAtFront=False):
	screen._root.attributes("-topmost", True)
	if not alwaysAtFront:
		screen._root.attributes("-topmost", False)

#
# Setting 'full' to true will make the window fullscreen.
#
def fullscreen(screen, full=True):
	screen._root.attributes("-fullscreen", full)

#
# Set the opacity of the window by setting the alpha value (0 - 1).
#
def opacity(screen, alpha=0.5):
	screen._root.attributes("-alpha", alpha)

#
# Set 'disabled' to true to disable window management functions including
# maximise, minimise, move & close.
#
def disabled(screen, disabled=True):
	screen._root.attributes("-disabled", disabled)

#
# Setting 'tool' to true changes the title bar decoration to a toolbar.
#
def toolwindow(screen, tool=True):
	screen._root.attributes("-toolwindow", tool)

#
# Setting 'x' and 'y' to true prevents window resizing in the horizontal
# and vertical direction respectively.
#
def noresize(screen, x=False, y=False):
	screen._root.resizable(x, y)

#
# Setting 'nodecorate' to true removes the windows decoration including title bar.
#
def nodecorate(screen, nodecorate=True):
	screen._root.overrideredirect(nodecorate)

#
# Set the minimum size of the window in pixels.
#
def minsize(screen, width=None, height=None):
	screen._root.minsize(width, height)

#
# Set the maximum size of the window in pixels.
#
def maxsize(screen, width=None, height=None):
	screen._root.maxsize(width, height)

#
# Minimise the window.
#
def minimise(screen):
	screen._root.iconify()
def minimize(screen):
	minimise(screen)

#
# Restore the window.
#
def restore(screen):
	screen._root.deiconify()