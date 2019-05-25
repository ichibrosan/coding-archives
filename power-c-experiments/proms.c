/* proms.c - dwg */

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

//void a_out(int device, int data)
//{
//	union REGS regs;
//	regs.h.ah = 1;
//	regs.h.al = data;
//	regs.x.dx = device;
//	int86(0x14,&regs,&regs);
//}

void a_out(int device, int data)
{
	outp(0x3f8,data);
}

//int a_instat(int device)
//{
//	union REGS regs;
//	regs.h.ah = 3;
//	regs.x.dx = device;
//	int86(0x14,&regs,&regs);
//	return regs.h.ah;
//}

int a_instat(int device)
{
	unsigned char c;
	c = inp(0x3f8+5);
	//printf("lsr=%02x ",c);
	return c;
}

//int a_in(int device)
//{
//	union REGS regs;
//	regs.h.ah = 2;
//	regs.x.dx = device;
//	int86(0x14,&regs,&regs);
//	if(1 == DEBUG) 
//		printf("a_in says line status is 0x%02x after read\n",
//			regs.h.ah);
//
//	return regs.h.al;		// Parity None
//	return regs.h.al & 0x7f;	// Parity Even
//}

int a_in(int device)
{
	return inp(0x3f8);
}

void a_wait_tsre(int device)
{
	printf("a_wait_tsre() beginning...\n");
	while ( 0 == ( TSRE & a_instat(PORT) ) );
	printf("a_wait_tsre() ending\n");
}

void a_wait_dr(int device)
{
//	printf("a_wait_dr() starting...\n");
	while ( 0 == ( DR & a_instat(PORT) ) );
//	printf("a_wait_dr() ending\n");
}

int is_dr(int device)
{
//	printf("Entering is_dr()\n");
	return DR & a_instat(PORT);
//	printf("Exiting is_dr()\n");
}

int is_tsre(int device)
{
	printf("Entering is_tsre()\n");
	return (TSRE & a_instat(PORT)) >> 6;
	printf("Exiting is_tsre()\n");
}

int main()
{
	FILE *fp;

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
	printf("readprom.exe(c)           2010/01/09  Version 0.0a\n");
	printf("Serial No. 0000-0000-654321    All Rights Reserved\n");
	printf("Copyright (C) 1991-2010         Douglas W. Goodall\n");
	printf("--------------------------------------------------\n");

	strcpy(szHexRef,"0123456789ABCDEF");

	a_init(PORT,
		INT14_BAUD_1200 | INT14_PARITY_NONE |
		INT14_STOPS_1   | INT14_BITS_8      );

	outp(0x3fc,0x03);

	printf("Draining input buffer\n");
	while(is_dr(PORT)) {
		a_in(PORT);
	}
	printf("Done draining input buffer\n");

	//a_wait_dr(PORT);	
	//c = a_in(PORT);

	//a_wait_tsre(PORT);
	//c = a_out(PORT,'H');

	printf("Sending No Operation Command\n");
	a_wait_tsre(PORT);
	c = a_out(PORT,'H');  a_wait_tsre(PORT);
	c = a_out(PORT,0x0d); a_wait_dr(PORT);	 c = a_in(PORT);
	printf("Char was %c 0x%x\n",c,c);
	a_wait_dr(PORT); c = a_in(PORT);
	printf("Char was %c 0x%x\n",c,c);

	printf("Sending Load Command\n");
	a_wait_tsre(PORT); c = a_out(PORT,'L');
	a_wait_tsre(PORT); c = a_out(PORT,0x0d);
	a_wait_dr(PORT);   c = a_in(PORT);
	printf("Char was %c 0x%x\n",c,c);
	a_wait_dr(PORT);   c = a_in(PORT);
	printf("Char was %c 0x%x\n",c,c);

	fp = fopen("prom.bin","w+b");

	bRunning = 1;

	printf("Sending Output Command\n");
	a_wait_tsre(PORT); c = a_out(PORT,'O');
	a_wait_tsre(PORT); c = a_out(PORT,0x0d);

	//a_wait_dr(PORT);   c = a_in(PORT);
	//printf("Char was %c 0x%x\n",c,c);

	while(1 == bRunning) {

		// try for :
		a_wait_dr(PORT);   c = a_in(PORT);
		while(c != ':') {
			a_wait_dr(PORT);   c = a_in(PORT);

		}
		printf("\n: ");

		a_wait_dr(PORT);   szRecordType[0] = a_in(PORT);
		a_wait_dr(PORT);   szRecordType[1] = a_in(PORT);
	        	           szRecordType[2] = 0;
		iRecordType = atoi(szRecordType);
		printf("%d ",iRecordType);

		if(10 == iRecordType) {
			a_wait_dr(PORT);   szAddress[0] = a_in(PORT);
			a_wait_dr(PORT);   szAddress[1] = a_in(PORT);
			a_wait_dr(PORT);   szAddress[2] = a_in(PORT);
			a_wait_dr(PORT);   szAddress[3] = a_in(PORT);
					   szAddress[4] = 0;			
			printf("%s  ",szAddress);

			a_wait_dr(PORT);   szMiscField[0] = a_in(PORT);
			a_wait_dr(PORT);   szMiscField[1] = a_in(PORT);
		  			   szMiscField[2] = 0;
			printf("%s  ",szMiscField);

			for(i=0;i<16;i++) {

				a_wait_dr(PORT);   szByteBuffer[0] = a_in(PORT);
				a_wait_dr(PORT);   szByteBuffer[1] = a_in(PORT);
		  			   	   szByteBuffer[2] =0;
				printf("%s ",szByteBuffer);

				for(j=0;j<16;j++) {
					if(szHexRef[j] == szByteBuffer[0]) {
						iNybble1 = j;
					}
				}
				for(j=0;j<16;j++) {
					if(szHexRef[j] == szByteBuffer[1]) {
						iNybble2 = j;
					}
				}

				Buffer[i] = (iNybble1*16)+iNybble2;

			}
			fwrite(Buffer,16,1,fp);

			a_wait_dr(PORT);   szByteBuffer[0] = a_in(PORT);
			a_wait_dr(PORT);   szByteBuffer[1] = a_in(PORT);
	  			   	   szByteBuffer[2] = 0;
			strcpy(szChecksum,szByteBuffer);
			printf(" %s",szChecksum);
		}
		if(0 == iRecordType) {
			a_wait_dr(PORT);   szAddress[0] = a_in(PORT);
			a_wait_dr(PORT);   szAddress[1] = a_in(PORT);
			a_wait_dr(PORT);   szAddress[2] = a_in(PORT);
			a_wait_dr(PORT);   szAddress[3] = a_in(PORT);
					   szAddress[4] = 0;			
			printf("Address is %s\n",szAddress);

			a_wait_dr(PORT);   szByteCount[0] = a_in(PORT);
			a_wait_dr(PORT);   szByteCount[1] = a_in(PORT);
					   szByteCount[2] = 0;			
			iByteCount = atoi(szByteCount);
			printf("iByteCount is %d\n",iByteCount);

			for(i=0;i<iByteCount;i++) {
				a_wait_dr(PORT);   szByteBuffer[0] = a_in(PORT);
				a_wait_dr(PORT);   szByteBuffer[1] = a_in(PORT);
		  			   	   szByteBuffer[2] =0;
				printf("%02X ",szByteBuffer);
				Buffer[i] = atoi(szByteBuffer);
			}

			bRunning = 0;
		}


	}
	fclose(fp);
	
	return EXIT_SUCCESS;
}

// eof
