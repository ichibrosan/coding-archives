@echo off
if exist *.bak erase *.bak
if exist *.lst erase *.lst
if exist *.obj erase *.obj
if exist *.map erase *.map
if exist *.lnk erase *.lnk
if exist *.out erase *.out
if exist *.mix erase *.mix
if exist *.xrf erase *.xrf
if exist *.exe erase *.exe
if exist *.img erase *.img
if exist c.err erase c.err
if exist *.trc erase *.trc
if exist *.sym erase *.sym
dir /w