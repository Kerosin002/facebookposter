@echo off
echo PROGRAM IS NOW RUNNING
PowerShell -NoProfile -ExecutionPolicy Bypass -Command "& {Start-Process PowerShell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File ""C:\Users\eltim\facebookposter\facebookPosterLauncher.ps1""' -Verb RunAs}"
ps1'"
