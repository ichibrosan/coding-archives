// dis6502.c 2010/01/29 dwg - 
// Copyright (C) 2010 Douglas W. Goodall. All Rights Reserved.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define VERBOSE

#include "opcodes.h"

#define PROMSIZE 2048

char cParm8;
char gszTemp[8];

int iParm16,iPC,iTems;

struct INFO_TAG {
	int iByte1;
	int iByte2;
	int iByte3;
	int iFamily;
	int iLength;
	int iMode;
	char szMnem[4];
#ifdef VERBOSE
	char szVERBOSE[32];
#endif
} info[PROMSIZE];

unsigned char prom[PROMSIZE];


int get_prom_image(char *szFilename)
{
	FILE * fp;
	fp = fopen(szFilename,"rb");
	if(NULL == fp) {
		printf("Sorry, cannot open input file\n");
		return(EXIT_FAILURE);
	}
	iTems = fread(prom,sizeof(prom),1,fp);
	//printf("iTems was %d\n",iTems);
	fclose(fp);
	return(EXIT_SUCCESS);
}

char * decode_absolute_address(unsigned int a)
{
	// Monitor Locations
	if(0xf800 == a) return("PLOT");
	if(0xf819 == a) return("HLINE");
	if(0xf828 == a) return("VLINE");
	if(0xf832 == a) return("CLRSCR");
	if(0xf836 == a) return("CLRTOP");
	if(0xf864 == a) return("SETCOL");
	if(0xf940 == a) return("PRNTYX");
	if(0xfdda == a) return("PRBYTE");
	if(0xfb1e == a) return("PREAD");
	if(0xfb2f == a) return("INIT");
	if(0xfb6f == a) return("SETPWRC");
	if(0xfc22 == a) return("VTAB");
	if(0xfc24 == a) return("VTABZ");
	if(0xfc42 == a) return("CLREOP");
	if(0xfc58 == a) return("HOME");
	if(0xfc70 == a) return("SCROLL");
	if(0xfc9c == a) return("CLREOL");
	if(0xfca8 == a) return("WAIT");
	if(0xfd35 == a) return("RDCHAR");
	if(0xfd0c == a) return("RDKEY");
	if(0xfd1b == a) return("KEYIN");
	if(0xfd67 == a) return("GETLNZ");
	if(0xfd6a == a) return("GETLN");
	if(0xfd8e == a) return("CROUT");
	if(0xfde3 == a) return("PRHEX");
	if(0xfded == a) return("COUT");
	if(0xfdf0 == a) return("COUT1");
	if(0xff3a == a) return("BELL");
	if(0xff4a == a) return("SAVE");
	if(0xff3f == a) return("RESTORE");
	if(0xfad7 == a) return("REGDSP");
	if(0xfada == a) return("REGDSP1");
	if(0xff69 == a) return("MONZ");
	
	// Applesoft Routines
	if(0xd566 == a) return("RUN");
	if(0xdb3a == a) return("STROUT");
	if(0xdb3d == a) return("STRPRT");
	if(0xe000 == a) return("BASIC");
	if(0xe003 == a) return("BASIC2");
	if(0xe10c == a) return("AYINT");
	if(0xe2f2 == a) return("GIVAYF");
	if(0xe484 == a) return("GARBAG");
	if(0xe7be == a) return("FADD");
	if(0xe7c1 == a) return("FADDT");
	if(0xe7a7 == a) return("FSUB");
	if(0xe7aa == a) return("FSUBT");
	if(0xe97f == a) return("FMULT");
	if(0xe982 == a) return("FMULTT");
	if(0xea66 == a) return("FDIV");
	if(0xea69 == a) return("FDIVT");
	if(0xea39 == a) return("MUL10");
	if(0xea55 == a) return("DIV10");
	if(0xeafd == a) return("MOVFMT");
	if(0xeb32 == a) return("MOVMFT");
	if(0xed24 == a) return("LINPRT");
	if(0xed2e == a) return("PRNTFAC");
	if(0xee8d == a) return("SQR");
	if(0xef09 == a) return("EXP");
	if(0xe941 == a) return("LOG");
	if(0xefae == a) return("RND");
	if(0xefea == a) return("COS");
	if(0xeff1 == a) return("SIN");
	if(0xf03a == a) return("TAN");
	if(0xf09e == a) return("ATN");
	if(0xf063 == a) return("PI/2");
	if(0xf06b == a) return("TWOPI");
	if(0xf070 == a) return("QUARTER");
	if(0xe913 == a) return("ONE");
	if(0xe92d == a) return("ROOTHALF");
	if(0xe92d == a) return("ROOTTWO");
	if(0xe937 == a) return("MINUSHALF");
	if(0xe93c == a) return("LOG2");
	if(0xee64 == a) return("HALF");
	if(0xe937 == a) return("MILLIARD");
	if(0xf3d8 == a) return("HGR2");
	if(0xf3e2 == a) return("HGR");
	if(0xf3f2 == a) return("HCLR");
	if(0xf3f6 == a) return("BKGND");
	if(0xf411 == a) return("HPOSN");
	if(0xf457 == a) return("HPLOT");
	if(0xf53a == a) return("HLIN");
	if(0xf6ec == a) return("SETHCOLOR");
	if(0xf5cb == a) return("HFIND");
	if(0xf601 == a) return("DRAW");
	if(0xf65d == a) return("XDRAW");
	
	sprintf(gszTemp,"$%04X",a);
	return(gszTemp);
}



int get_info()
{
	int bLineBreak;
	
	info[iPC].iByte1 = prom[iPC];
//	printf("info[iPC].iByte1  is 0x%02X\n",info[iPC].iByte1);
	
	info[iPC].iFamily = opcodes[info[iPC].iByte1].iFamily;
//	printf("info[iPC].iFamily is 0x%02x\n",info[iPC].iFamily);
	
	if(green == info[iPC].iFamily) {
		info[iPC].iMode   = opcodes[info[iPC].iByte1].iMode;
		info[iPC].iLength = opcodes[info[iPC].iByte1].iLength;
		if(2 == info[iPC].iLength) info[iPC].iByte2 = prom[iPC+1];
		if(3 == info[iPC].iLength) info[iPC].iByte3 = prom[iPC+2];
		
		strncpy(
			info[iPC].szMnem,
			opcodes[info[iPC].iByte1].szOpcode,
			sizeof(info[iPC].szMnem));
			
#ifdef VERBOSE
		strncpy(
			info[iPC].szVERBOSE,
			opcodes[info[iPC].iByte1] .szVERBOSE,
			sizeof(info[iPC].szVERBOSE));
#endif

		printf("%04X: ",iPC);
			
		switch(info[iPC].iLength) {
			case 1:
				printf("%02X        ",
					info[iPC].iByte1);
				break;
			case 2:
				printf("%02X %02X     ",
					info[iPC].iByte1,
					info[iPC].iByte2);
				break;
			case 3:
				printf("%02X %02X %02X  ",
					info[iPC].iByte1,
					info[iPC].iByte2,
					info[iPC].iByte3);
				break;
		};
		printf("%s ",info[iPC].szMnem);

		switch(info[iPC].iMode) {
			case immediate:
				printf("#$%02X",info[iPC].iByte2);
				break;
			case zeropage:
				printf("$%02X\t",info[iPC].iByte2);
				break;
			case zeropagex:
				printf("$%02X,x",info[iPC].iByte2);
				break;
			case zeropagey:
				printf("$%02X,y",info[iPC].iByte2);
				break;
			case absolute:
				iParm16 = (info[iPC].iByte3*256)+info[iPC].iByte2; 
//				printf("$%04X",iParm16);
				printf("%s",decode_absolute_address(iParm16));
				break;
			case absolutex:
				iParm16 = (info[iPC].iByte3*256)+info[iPC].iByte2; 
				printf("$%04X,x",iParm16);
				break;
			case absolutey:
				iParm16 = (info[iPC].iByte3*256)+info[iPC].iByte2; 
				printf("$%04X,y",iParm16);
				break;
			case indirect:
				iParm16 = (info[iPC].iByte3*256)+info[iPC].iByte2; 
				printf("($%04X)",iParm16);
				break;
			case indirectx:
				iParm16 = (info[iPC].iByte3*256)+info[iPC].iByte2; 
				printf("($%04X),x",iParm16);
				break;
			case indirecty:
				iParm16 = (info[iPC].iByte3*256)+info[iPC].iByte2; 
				printf("($%04X),y",iParm16);
				break;
			case accum:
				printf("a\t");
				break;
			case relative:
				cParm8 = prom[iPC+1];
				
				iParm16 = iPC + info[iPC].iLength + cParm8; 
				printf("$%04X",iParm16);
				break;
			case implied:
				printf("\t");
				//printf("	; iMode is implied");
				//if(0 == strncmp(info[iPC].szMnem,"rts",sizeof(info[iPC].szMnem))) {
					//printf("\nxxxx: xx xx xx  xxx xxxxxxxxxxxxxxxxxxxxxxxxxxx\n");
					//printf("\n               \\___/\n");
				//}
				break;
		}

		bLineBreak = 0;

		if(0 == strncmp(info[iPC].szMnem,"bcc",sizeof(info[iPC].szMnem))) {
				bLineBreak = 1;
		}

		if(0 == strncmp(info[iPC].szMnem,"bcs",sizeof(info[iPC].szMnem))) {
				bLineBreak = 1;
		}

		if(0 == strncmp(info[iPC].szMnem,"beq",sizeof(info[iPC].szMnem))) {
				bLineBreak = 1;
		}

		if(0 == strncmp(info[iPC].szMnem,"bne",sizeof(info[iPC].szMnem))) {
				bLineBreak = 1;
		}

		if(0 == strncmp(info[iPC].szMnem,"bpl",sizeof(info[iPC].szMnem))) {
				bLineBreak = 1;
		}

		
		if(0 == strncmp(info[iPC].szMnem,"jmp",sizeof(info[iPC].szMnem))) {
				bLineBreak = 1;
		}		
		
		if(0 == strncmp(info[iPC].szMnem,"jsr",sizeof(info[iPC].szMnem))) {
				bLineBreak = 1;
		}		

		if(0 == strncmp(info[iPC].szMnem,"rts",sizeof(info[iPC].szMnem))) {
				bLineBreak = 1;
		}		
		
#ifdef VERBOSE
		printf("	; %s, ",info[iPC].szVERBOSE);
		switch(info[iPC].iMode) {
			case immediate:
				printf("immediate");
				break;
			case zeropage:
				printf("zeropage");
				break;
			case zeropagex:
				printf("zeropage indexed");
				break;
			case zeropagey:
				printf("zeropage indexed");
				break;
			case absolute:
				printf("absolute");
				break;
			case absolutex:
				printf("absolute indexed");
				break;
			case absolutey:
				printf("absolute indexed");
				break;
			case indirect:
				printf("indirect");
				break;
			case indirectx:
				printf("indirect indexed");
				break;
			case indirecty:
				printf("indirect indexed");
				break;
			case accum:
				printf("accumulator");
				break;
			case relative:
				printf("relative");
				break;
			case implied:
				printf("implied");
				break;
		}
		
		printf("\n");
#else
		printf("\n");
#endif

		if(1 == bLineBreak) printf("\n");

		return(info[iPC].iLength);	
	}
	
	printf("\n%04X: %02X        db  $%02X\n",iPC,
		info[iPC].iByte1,
		info[iPC].iByte1);
		
	return(1);
}


main(int argc,char **argv)
{
	int i;
	
	iPC = 0;
	
	if(2 != argc) {
		printf("usage - dis6502 <filespec>");
		return(EXIT_FAILURE);
	}
	
	if(EXIT_FAILURE == get_prom_image(argv[1])) {
		exit(EXIT_FAILURE);
	}
	
	while(iPC < (PROMSIZE-2) ) {
		iPC += get_info();
	}
	
	exit(EXIT_SUCCESS);
	
}

