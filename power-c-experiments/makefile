# GNU Makefile for generaic programs
# 2/16/2010 14:00 dwg - initial version 
# Copyright (C) 2010 Douglas W. Goodall. All Rights Reserved.

DEBUG   = -ggdb
SUFFIX  = .exe
BINS    = dis6502$(SUFFIX) dump$(SUFFIX) resistors$(SUFFIX)
CC      = gcc
CFLAGS  = $(DEBUG) 

all:	$(BINS) Makefile


dis6502$(SUFFIX):	dis6502.c
	$(CC) $(CFLAGS) $< -o $@
	./dis6502 sider22.bin > sider22.out

dump$(SUFFIX):		dump.c
	$(CC) $(CFLAGS) $< -o $@

resistors$(SUFFIX):	resistors.c
	$(CC) $(CFLAGS) $< -o $@
	./resistors > resistors.out

clean:
	@rm -f $(BINS) *.out 

