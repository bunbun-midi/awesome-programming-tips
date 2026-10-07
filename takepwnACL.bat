echo off
REM you would run this from a directory to rename the .dlls and .exes to deactivate them but also would need to enter in the full path for setacl.exe
REM i found that icacls and takeown don't really always work so obviously using setacl.exe would be more robust and successful
REM ive included setacl.exe in the repo feel free to virustotal it it's just the file from setacl 3.1.2 (executable veresion).zip
echo on
takeown /f . /r /d y
icacls . /inheritance:r /grant:r %username%:(OI)(CI)F /t
icacls * /grant "%USERDOMAIN%\%USERNAME%":F
SetACL.exe -on . -ot file -actn ace -ace "n:S-1-5-32-544;p:full;i:so,sc;m:grant" -rec cont_obj
rename *.dll *.dllb
rename *.exe *.exeb
