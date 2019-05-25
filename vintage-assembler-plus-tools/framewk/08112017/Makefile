# ---------------------------------------------------
# Makefile     Ver 17.08.11k  x86_64-apple-darwin10.0
# Serial No. 2011-1042-654321    All Rights Reserved.
# Copyright (C) 2011 Douglas Goodall,  United States.
# ---------------------------------------------------
# Created by asmall.cpp  Fri Aug 11 11:01:30 PDT 2017


AS = ../assemble

HEXFILES = parttabl.hex 

INCFILES = 

all:	$(HEXFILES)


parttabl.hex:	parttabl.asm $(AS) Makefile $(INCFILES) 
	$(AS) parttabl 

clean:
	rm -f *.exp *.obj *.bin editthem *.lst *.log *.hex 
	rm -r -f parttabl  *.ini *.sym

# eof - Makefile
