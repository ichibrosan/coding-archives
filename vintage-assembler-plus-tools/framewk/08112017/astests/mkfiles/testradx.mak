# ---------------------------------------------------
# mkfiles/testradx.mak  Ver 11.08.21c  
# Serial No. 2011-1042-654321    All Rights Reserved.
# Copyright (C) 2011 Douglas Goodall,  United States.
# ---------------------------------------------------
# mkfiles/testradx.mak autogenerated by asmall.cpp 
# Sun Aug 21 02:26:51 PDT 2011
# Copyright (c)2011 Douglas Goodall. Rights Reserved.

AS = ../assemble

INCFILES  = assemble.inc banner.inc cpm80.inc gplstuff.inc incl1.inc incl2.inc incl3.inc printhex.inc 

testradx.hex:	testradx.asm $(INCFILES) $(AS) 
	$(AS) testradx 

clean:
	rm -f *.ini *.exp *.obj *.bin  *.lst *.log *.hex

# eof - mkfiles/testradx.mak
