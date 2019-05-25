#include <stdio.h>
#include <stdlib.h>
#include <bios.h>
#include "ibmbios.h"

// used to test includability of generated file
//#include "data.h"

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

unsigned char buffer[512];

int main(int argc,char **argv)
{
	char szTemp[80];
	FILE *fp;
	int byte;
	int c;
	int i;
	int j;
	int k;
	int rc;
	int drive, head, track,sector;

	printf("--------------------------------------------------\n");
	printf("Sec2Hdr.exe(c)            2009/12/01  Version 0.0a\n");
	printf("Serial No. 0000-0000-654321    All Rights Reserved\n");
	printf("Copyright (C) 1991-2009         Douglas W. Goodall\n");
	printf("--------------------------------------------------\n");


	if(argc != 5) {
		printf(" usage -  sec2hdr <dr> <head> <track> <sector>");
		exit(EXIT_FAILURE);
	}

	biosdisk(INT13_RESET, 0, 0, 0, 0, 0, NULL);

	rc = biosdisk(INT13_READ,
		drive = atoi(argv[1]),	// drive
		head = atoi(argv[2]),	// head
		track = atoi(argv[3]),	// track
		sector = atoi(argv[4]),	// sector
		1,buffer);

	sprintf(szTemp,"h%dt%02ds%02d.h",head,track,sector);
	fp = fopen(szTemp,"w");
	if(NULL == fp) {
		printf("Error opening output file %s\n",szTemp);
		exit(EXIT_FAILURE);
	}		

	fprintf(fp,"unsigned char d%dt%02dh%ds%02d[512] = {\n",
		drive,head,track,sector);

	byte = 0;
	for(j=0;j<32;j++) {
		fprintf(fp,"      ");
		for(i=0;i<16;i++) {
			fprintf(fp,"0x%02x",buffer[(j*16)+i]);
			if(++byte<512) {
				fprintf(fp,",");
			} else {
				fprintf(fp," ");
			}
			if(i==7) {
				fprintf(fp,"    // 0x%04x (%3d)  ",byte-1-7,byte-1-7);
				for(k=0;k<8;k++) {
					c = buffer[(j*16)+i-1-7+k];
					if( (c > 0x1f) && (c < 0x7b) ) {
						fprintf(fp,"%c",c);
					} else {
						fprintf(fp,".");
					}
				}
				fprintf(fp,"\n      ");
			}
		}
		fprintf(fp,"    // 0x%04x (%3d)  ",byte-1-7,byte-1-7);
		for(k=0;k<8;k++) {
			c = buffer[(j*16)+i-1-7+k];
			if( (c > 0x1f) && (c < 0x7b) ) {
				fprintf(fp,"%c",c);
			} else {
				fprintf(fp,".");
			}
		}
		fprintf(fp,"\n");
	}
	fprintf(fp,"};\n");
	fclose(fp);
}


