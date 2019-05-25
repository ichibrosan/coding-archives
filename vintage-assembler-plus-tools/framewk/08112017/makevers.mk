# ---------------------------------------------------
# makevers.mak v17.08.11k for x86_64-apple-darwin10.0
# Serial No. 2017-0501-654321                        
# Copyright (C) 2017 Douglas Goodall,  United States.
# ---------------------------------------------------
# makevers.mak autogenerated by makemake.cpp 
# Fri Aug 11 10:26:03 PDT 2017

CC = g++
CCFLAGS = -w
INCLUDES = ascalc.hpp asdec20.hpp asdec65.hpp asdec68k.hpp asdec80.hpp asdec85.hpp asdecdir.hpp asdecz80.hpp asdefs.hpp aseval.hpp ashexout.hpp asmultip.hpp asomfdef.hpp asomfgen.hpp asouterr.hpp asouthex.hpp asoutlst.hpp asoutwrn.hpp asparse.hpp asparse2.hpp asprint.hpp asresolv.hpp asymbols.hpp bcctrace.hpp cbindefs.hpp cpostfix.hpp defaults.hpp dirclass.hpp dwgalloc.hpp environ.hpp globdata.hpp includes.hpp inibind.hpp memory.hpp pcascii.hpp portab.hpp srcclass.hpp strlwr.hpp strupr.hpp versbind.hpp 

makevers:	makevers.cpp $(INCLUDES) 
	$(CC) $(CCFLAGS) makevers.cpp -o makevers

clean:
	rm -f makevers

# eof - makevers.mak
