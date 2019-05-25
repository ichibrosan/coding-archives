// writepro.c(exe) 2009/01/09 dwg - 
// Copyright (C) 2010 Douglas Goodall. All Rights Reserved.

// Write to 2716 from Socket 1 of Data I/O 280 Set Programmer 

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

void a_init(int parms)
{
	union REGS regs;
	regs.h.ah = 0;
	regs.h.al = parms;
	regs.x.dx = PORT;
	int86(0x14,&regs,&regs);
}

void a_out(int data)
{
	outp(0x3f8-(0x100*PORT),data);
}

int a_instat(void)
{
	unsigned char c;
	c = inp(0x3f8+5-(0x100*PORT));
	return c;
}

int a_in(void)
{
	return inp(0x3f8-(0x100*PORT));
}

void a_wait_tsre(void)
{
	while ( 0 == ( TSRE & a_instat() ) );
}

void a_wait_dr(void)
{
	while ( 0 == ( DR & a_instat() ) );
}

int is_dr(void)
{
	return DR & a_instat();
}

int is_tsre(void)
{
	return (TSRE & a_instat()) >> 6;
}

int main(int argc, char **argv)
{
	FILE *fp_bin;

	char szRecordType[4];
	char szAddress[6];
	char szMiscField[3];
	char szByteBuffer[3];
	unsigned char Buffer[16];
	char szChecksum[3];
	char szByteCount[3];
	char szHexRef[17];

	int c;
	int iByteCount;
	int iRecordType;
	int i;
	int iNybble1,iNybble2;
	int j;
	int bRunning;

	printf("--------------------------------------------------\n");
	printf("writepro.exe from Data I/O 2010/02/21 Version 0.0a\n");
	printf("Serial No. 0000-0000-654321    All Rights Reserved\n");
	printf("Copyright (C) 1991-2010         Douglas W. Goodall\n");
	printf("--------------------------------------------------\n");

	strcpy(szHexRef,"0123456789ABCDEF");

	fp_bin = fopen("readprom.bin","w+b");

	a_init(	INT14_BAUD_1200 | INT14_PARITY_NONE |
		INT14_STOPS_1   | INT14_BITS_8      );

	// assert hardware handshaking lines 
	// to Data I/O wants to talk
	outp(0x3fc-(0x100*PORT),0x03);

	while(is_dr()) {
		a_in();
	}

	a_wait_tsre();
	a_out('H');  a_wait_tsre();
	a_out(0x0d); a_wait_dr();   c = a_in();
	a_wait_dr(); c = a_in();


	//printf("Setting Intel 2716 Device Type\n");
	a_wait_tsre(); a_out('1');  
	a_wait_tsre(); a_out('9');  
	a_wait_tsre(); a_out('2');  
	a_wait_tsre(); a_out('3');  
	a_wait_tsre(); a_out('@');  
	a_wait_tsre(); a_out(0x0d); 
	a_wait_dr();   c = a_in();
	a_wait_dr();   c = a_in();

	//printf("Loading device data into ram\n");
	a_wait_tsre(); a_out('L');
	a_wait_tsre(); a_out(0x0d);
	a_wait_dr();   c = a_in();
	a_wait_dr();   c = a_in();


	bRunning = 1;

	//printf("Transferring ram buffer to host computer\n");
	a_wait_tsre(); a_out('O');
	a_wait_tsre(); a_out(0x0d);

	while(1 == bRunning) {

		a_wait_dr();   c = a_in();
		while(c != ':') {
			a_wait_dr();   c = a_in();

		}
		printf(":");

		a_wait_dr();   szByteCount[0] = a_in();
		a_wait_dr();   szByteCount[1] = a_in();
	        	           szByteCount[2] = 0;


		for(j=0;j<16;j++) {
			if(szHexRef[j] == szByteCount[0]) {
				iNybble1 = j;
				break;
			}
		}
		for(j=0;j<16;j++) {
			if(szHexRef[j] == szByteCount[1]) {
				iNybble2 = j;
				break;
			}
		}
		iByteCount = (iNybble1*16)+iNybble2;
		printf("%s",szByteCount);


		a_wait_dr();   szAddress[0] = a_in();
		a_wait_dr();   szAddress[1] = a_in();
		a_wait_dr();   szAddress[2] = a_in();
		a_wait_dr();   szAddress[3] = a_in();
				   szAddress[4] = 0;			
		printf("%s",szAddress);


		a_wait_dr();   szRecordType[0] = a_in();
		a_wait_dr();   szRecordType[1] = a_in();
	  			   szRecordType[2] = 0;

		for(j=0;j<16;j++) {
			if(szHexRef[j] == szRecordType[0]) {
				iNybble1 = j;
				break;
			}
		}
		for(j=0;j<16;j++) {
			if(szHexRef[j] == szRecordType[1]) {
				iNybble2 = j;
				break;
			}
		}
		iRecordType = (iNybble1*16)+iNybble2;
		printf("%s",szRecordType);

		if(0 == iRecordType) {

			for(i=0;i<iByteCount;i++) {

				a_wait_dr();   szByteBuffer[0] = a_in();
				a_wait_dr();   szByteBuffer[1] = a_in();
		  			   	   szByteBuffer[2] =0;
				printf("%s",szByteBuffer);

				for(j=0;j<16;j++) {
					if(szHexRef[j] == szByteBuffer[0]) {
						iNybble1 = j;
						break;
					}
				}
				for(j=0;j<16;j++) {
					if(szHexRef[j] == szByteBuffer[1]) {
						iNybble2 = j;
						break;
					}
				}

				Buffer[i] = (iNybble1*16)+iNybble2;

			}

			fwrite(Buffer,iByteCount,1,fp_bin);

		}
		if(1 == iRecordType) {
			bRunning = 0;
			a_wait_dr();   szByteBuffer[0] = a_in();
			a_wait_dr();   szByteBuffer[1] = a_in();
	  			   	   szByteBuffer[2] = 0;
			strcpy(szChecksum,szByteBuffer);
			printf("%s",szChecksum);

		}

		printf("\n");
	}
	fclose(fp_bin);

	return EXIT_SUCCESS;
}

// eof
