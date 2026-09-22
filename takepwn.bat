takeown /f . /r /d y
icacls . /inheritance:r /grant:r %username%:(OI)(CI)F /t
icacls * /grant "%USERDOMAIN%\%USERNAME%":F
rename *.dll *.dllb
rename *.exe *.exeb