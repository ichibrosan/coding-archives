# ---------------------------------------------------
# mkfiles/testsyml.mak  Ver 11.03.24c  
# Serial No. 2011-1042-654321    All Rights Reserved.
# Copyright (C) 2011 Douglas Goodall,  United States.
# ---------------------------------------------------
# mkfiles/testsyml.mak autogenerated by asmall.cpp 
# Thu Mar 24 02:23:40 PDT 2011
# Copyright (c)2011 Douglas Goodall. Rights Reserved.

AS = ../assemble

INCFILES  = assemble.inc banner.inc cpm80.inc incl1.inc incl2.inc incl3.inc 

testsyml.hex:	testsyml.asm $(INCFILES) $(AS) 
	$(AS) testsyml 

clean:
	rm -f *.bin  *.lst *.log *.hex

# eof - mkfiles/testsyml.mak
