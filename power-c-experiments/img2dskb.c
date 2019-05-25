// img2dskb.c 2009/11/29 dwg - 
// Copyright (C) 2009 Douglas W. Goodall. All Rights Reserved.

// The purpose of this program is to read the contents
// of a file and deposit the data on a floppy in the
// proper sectors to reproduce the orginal contents of
// the disk. The floppy must be properly formatted.

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

#define HDS 2
#define SPT 15
#define TRKS 80

unsigned char buffer1[512*9];
unsigned char buffer2[512*6];

int main(int argc,char **argv)
{
	FILE *fp;
	int c,head,i,j,rc,track;

	printf("--------------------------------------------------\n");
	printf("Img2DskB.exe(c)           2009/12/01  Version 0.0a\n");
	printf("Serial No. 0000-0000-654321    All Rights Reserved\n");
	printf("Copyright (C) 1991-2009         Douglas W. Goodall\n");
	printf("--------------------------------------------------\n");

	
	if(2 > argc) {
		printf("usage: img2dskb <filename.ext>");
		exit(EXIT_FAILURE);
	}

	fp = fopen(argv[1],"rb");
	if(NULL == fp) {
		printf("Error opening output file %s\n",argv[1]);
		exit(EXIT_FAILURE);
	}

	biosdisk(INT13_RESET, 0, 0, 0, 0, 0, NULL);

	for(track=0;track<TRKS;track++) {
		for(head=0;head<HDS;head++) {
			printf("Writing T %2d H %d%c",track+1,head,0x0d);

			fread(buffer1,512,9,fp);
			rc = biosdisk(INT13_WRITE,
				0,head,track,1,9,buffer1);
			if(0 != rc) {
				printf("1st write error is 0x%02x\n",rc);
				exit(EXIT_FAILURE);
			}
			
			fread(buffer2,512,6,fp);
			rc = biosdisk(INT13_WRITE,
				0,head,track,10,6,buffer2);
			if(0 != rc) {
				printf("2nd write error is 0x%02x\n",rc);
				exit(EXIT_FAILURE);
			}

		}	
	}
	fclose(fp);
	printf("Writing Completed");
}

// eof
