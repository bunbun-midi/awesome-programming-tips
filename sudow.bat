@powershell.exe -Command "Start-Process cmd \"/k cd /d %cd%\" -Verb RunAs"
REM usage. just like put this in a folder that's in your PATH and then you can run things as administrator
REM for example
REM sudow cmd.exe
