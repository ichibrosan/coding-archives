// qsector.c 2009/12/1 dwg - 
// Copyright (C) 2009 Douglas W. Goodall. All Rights Reserved.

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
	printf("QSector.exe(c)            2009/12/01  Version 0.0a\n");
	printf("Serial No. 0000-0000-654321    All Rights Reserved\n");
	printf("Copyright (C) 1991-2009         Douglas W. Goodall\n");
	printf("--------------------------------------------------\n");


	if(argc != 5) {
		printf("usage - qsector <drv> <head> <track> <sector>\n");
		printf("  for a: floppy - qsector 0 {0|1} {0-79} {1-18}\n");
		printf("  for b: floppy - qsector 0 {0|1} {0-79} {1-18}\n");
		printf("  for c: hard d - qsector 128 {0|1} {0-79} {1-18}\n");
		exit(EXIT_FAILURE);
	}

	biosdisk(INT13_RESET, 0, 0, 0, 0, 0, NULL);

	// drv head track sector
	rc = biosdisk(INT13_READ,atoi(argv[1]),atoi(argv[2]),atoi(argv[3]),atoi(argv[4]),1,buffer);
	if(0 == rc) {
		printf("Sector read was successful\n");
	} else {
		printf("Return code from read call was 0x%x\n",rc);
		exit(EXIT_FAILURE);
	}
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


