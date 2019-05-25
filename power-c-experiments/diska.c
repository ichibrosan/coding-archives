// diska.c(exe) 12/01/2009 dwg - 

#include <stdio.h>
#include <stdlib.h>
#include <bios.h>
#include "ibmbios.h"

/*
; -------------------------------------------------------
;    biosdisk(cmd, drive, head, track, sector, nsects, buffer)
; -------------------------------------------------------
;        int cmd;       /* action to take 0..5 */
;        int drive;     /* disk drive number 0.. */
;        int head;      /* head number */
;        int track;     /* physical track number */
;        int sector;    /* starting sector */
;        int nsects;    /* number of sectors (1..9) */
;        char *buffer;  /* address of buffer */
;
;        return: status word
; -------------------------------------------------------
*/

unsigned char buffer[512*9];

int main(int argc,char **argv)
{
	int c;
	int i;
	int j;
	int rc;

	printf("--------------------------------------------------\n");
	printf("DiskA.exe(c)              2009/12/01  Version 0.0a\n");
	printf("Serial No. 0000-0000-654321    All Rights Reserved\n");
	printf("Copyright (C) 1991-2009         Douglas W. Goodall\n");
	printf("--------------------------------------------------\n");

	biosdisk(INT13_RESET, 0, 0, 0, 0, 0, NULL);

	rc = biosdisk(INT13_READ,0,0,0,1,9,buffer);
	for(j=0;j<32;j++) {
		printf("\n0x%04x: ",j*16);
		for(i=0;i<16;i++) {
			printf("%02x ",buffer[(j*16)+i]);
		}
		printf("  ");
		for(i=0;i<16;i++) {
			c = buffer[(j*16)+i];
			if( (c > 0x1f) && (c < 0x7b) ) {
				printf("%c",c);
			} else {
				printf(".");
			}
		}
	}
}


