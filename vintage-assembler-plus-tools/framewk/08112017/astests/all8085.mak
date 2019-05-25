# ---------------------------------------------------
# mkfiles/all8085.mak  Ver 11.03.08k  
# Serial No. 2011-1042-654321    All Rights Reserved.
# Copyright (C) 2011 Douglas Goodall,  United States.
# ---------------------------------------------------
# mkfiles/all8085.mak autogenerated by asmall.cpp 
# Tue Mar  8 10:28:38 PST 2011
# Copyright (c)2011 Douglas Goodall. Rights Reserved.

AS = ../assemble

INCFILES  = assemble.inc banner.inc cpm80.inc incl1.inc incl2.inc incl3.inc 

all8085.hex:	all8085.asm $(INCFILES) $(AS) 
	$(AS) all8085 

clean:
	rm -f *.bin  *.lst *.log *.hex

# eof - mkfiles/all8085.mak