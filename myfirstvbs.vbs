MsgBox "Hello, World!", vbInformation, "Greeting"

' Script to open Notepad
Set objShell = CreateObject("WScript.Shell")
objShell.Run "notepad.exe"


' Create an instance of the WScript.Shell object
Set objShell = CreateObject("WScript.Shell")

' Run the command to open Command Prompt
objShell.Run "cmd.exe"

' Optional: to run with specific parameters, you can include them
objShell.Run "cmd.exe /k echo Hello, World!"