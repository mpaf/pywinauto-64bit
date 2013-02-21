"""Send some commands to media player - you need to look at the code!!

Media Player needs to be running - note - this has not been tested well :)
"""

import sys

try:
    from pywinauto import application
except ImportError:
    import os.path
    pywinauto_path = os.path.abspath(__file__)
    pywinauto_path = os.path.split(os.path.split(pywinauto_path)[0])[0]
    sys.path.append(pywinauto_path)
    from pywinauto import application

from pywinauto.win32defines import WM_COMMAND

def myMediaFunc(getFunc):
 app = application.Application()
 if getFunc=="next":
  app.WindowsMediaPlayer.TypeKeys("%PN")
 elif getFunc=="next2":
  app.WindowsMediaPlayer.TypeKeys("^f")
 elif getFunc=="next3":
  app.WindowsMediaPlayer.SendMessage(WM_COMMAND, 18811, 0)
 elif getFunc=="prev":
  app.WindowsMediaPlayer.MenuSelect("^b")
 elif getFunc=="mute":
  app.WindowsMediaPlayer.MenuSelect("{F7}")
 elif getFunc=="vold":
  app.WindowsMediaPlayer.MenuSelect("Play->Volume->Down")
 elif getFunc=="volu":
  app.WindowsMediaPlayer.MenuSelect("Play->Volume->Up")
 elif getFunc=="play":
  app.WindowsMediaPlayer.MenuSelect("Play->Play/Pause")
 elif getFunc=="stop":
  app.WindowsMediaPlayer.MenuSelect("Play->Stop")
sendmyFunc=sys.argv[1]
myMediaFunc(sendmyFunc)