/* test.c Fri, Nov 27, 2009 - dwg */

#include <stdio.h>
#include <stdlib.h>
#include <dos.h>

#include "ibmbios.h"

#define COM1 0
#define COM2 1
#define DEBUG 0
#define PORT COM1
#define DR   1
#define TSRE 0x40

void a_init(int device,int parms)
{
	union REGS regs;
	regs.h.ah = 0;
	regs.h.al = parms;
	regs.x.dx = device;
	int86(0x14,&regs,&regs);
}

void a_out(int device, int data)
{
	union REGS regs;
	regs.h.ah = 1;
	regs.h.al = data;
	regs.x.dx = device;
	int86(0x14,&regs,&regs);
}

int a_instat(int device)
{
	union REGS regs;
	regs.h.ah = 3;
	regs.x.dx = device;
	int86(0x14,&regs,&regs);
	return regs.h.ah;
}

int a_in(int device)
{
	union REGS regs;
	regs.h.ah = 2;
	regs.x.dx = device;
	int86(0x14,&regs,&regs);
	if(1 == DEBUG) 
		printf("a_in says line status is 0x%02x after read\n",
			regs.h.ah);

//	return regs.h.al;		// Parity None
	return regs.h.al & 0x7f;	// Parity Even
}

void a_wait_tsre(int device)
{
	while ( 0 == ( TSRE & a_instat(PORT) ) );
}

void a_wait_dr(int device)
{
	while ( 0 == ( DR & a_instat(PORT) ) );
}

int is_dr(int device)
{
	return DR & a_instat(PORT);
}

int is_tsre(int device)
{
	return (TSRE & a_instat(PORT)) >> 6;
}

int main()
{
	int c;
	int i;

	printf("--------------------------------------------------\n");
	printf("Serial.exe(c)             2009/12/01  Version 0.0a\n");
	printf("Serial No. 0000-0000-654321    All Rights Reserved\n");
	printf("Copyright (C) 1991-2009         Douglas W. Goodall\n");
	printf("--------------------------------------------------\n");

	a_init(PORT,
		INT14_BAUD_9600 | INT14_PARITY_NONE |
		INT14_STOPS_1   | INT14_BITS_8      );

	for(i=0;i<26;i++) {
		a_wait_tsre(PORT);
		a_out(PORT,'A'+i);
		sleep(1);
	}

	a_wait_dr(PORT);	
	c = a_in(PORT);

	printf("Char was %c 0x%x\n",c,c);
	
	return EXIT_SUCCESS;
}

// eof
