// producea.c 12/01/2009 dwg - 

// The purpose of this program is to read an image file
// created by the dska2img program and write it to a fresh
// unformatted floppy disk. This program formats as it writes
// and is therefore more efficient than having to run formata
// followed by img2dska.

// Copyright (C) 2009 Douglas W. Goodall. All Rights Reserved.

#include <stdio.h>
#include <stdlib.h>
#include <dos.h>
#include <bios.h>
#include "ibmbios.h"

int format_track(int cyl, int head)
{
	union REGS regs;
	struct SREGS sregs;
	unsigned char far * fptr;
	int rc;
	unsigned int vector_off;
	unsigned int vector_seg;

	struct DISK_BASE_TAG {
		unsigned char firstspec;
		unsigned char secondspec;
		unsigned char motorwait;
		unsigned char sectorsize;
		unsigned char endoftrack;
		unsigned char gap;
		unsigned char dtl;
		unsigned char gapforformat;
		unsigned char fillforformat;
		unsigned char headsettle;
		unsigned char motorstart;
	} disk_base;

	void far *pLocal;
	pLocal = &disk_base;

	vector_off = peek(0,0x78);
	vector_seg = peek(0,0x7a);
	poke(0,0x78,FP_OFF(pLocal));
	poke(0,0x7a,FP_SEG(pLocal));

	disk_base.firstspec     = 0xdf;
	disk_base.secondspec    = 2;
	disk_base.motorwait     = 37;
	disk_base.sectorsize    = 2;
	disk_base.endoftrack    = 18;
	disk_base.gap           = 0x2a;
	disk_base.dtl           = 255;
	disk_base.gapforformat  = 0x50;
	disk_base.fillforformat = 0xf6;
	disk_base.headsettle    = 15;
	disk_base.motorstart    = 8;

	printf("Formatting Track %2d Head %d%c",cyl+1,head,0x0d);
	init_chrn_144(cyl,head,18,2);

	regs.h.ah = INT13_FORMAT;
	regs.h.dl = 0; // 0 = A:
	regs.h.dh = head;
	regs.h.ch = cyl;
	regs.h.cl = 18;		// unused for format 
	regs.h.al = 18;
	fptr = &format_144;
	regs.x.bx = FP_OFF(fptr);
	sregs.es  = FP_SEG(fptr);
	rc = int86x(0x13,&regs, &regs, &sregs);
	if(0 != regs.h.ah){
		printf("rc from format call was 0x%x\n",rc);
		printf("ah from format call was 0x%x\n",regs.h.ah);
		switch(regs.h.ah) {
			case    0: printf("Operation Successful");		break;
			case    1: printf("Bad operation ");			break;
			case    2: printf("address mark not found");		break;
			case    4: printf("Requested sector not found");	break;
			case    5: printf("Reset failed");			break;
			case    7: printf("Drive parm activity failed");	break;
			case    9: printf("DMA across 64k boundary");		break;
			case 0x0b: printf("Bad sector flag");			break;
			case 0x10: printf("Bad ECC on disk read");		break;
			case 0x11: printf("ECC corrected data error");		break;
			case 0x20: printf("Con troller failed");		break;
			case 0x40: printf("Seek operation failed");		break;
			case 0x80: printf("Attachment failed to respond");	break;
			case 0xbb: printf("undefined error");			break;
			case 0xff: printf("Sense operation failed");		break;
		  	  default: printf("unknown error number 0x%x",
				regs.h.ah);				break;
		};
		printf("al from format call was 0x%x\n",regs.h.al);
		poke(0,0x78,vector_off);
		poke(0,0x7a,vector_seg);
		exit(EXIT_FAILURE);
	}
	poke(0,0x78,vector_off);
	poke(0,0x7a,vector_seg);
}	

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
#define SPT 18
#define TRKS 80

unsigned char buffer1[512*(SPT/2)];
unsigned char buffer2[512*(SPT/2)];

int main(int argc,char **argv)
{
	FILE *fp;
	int c,head,i,j,rc,track;

	printf("--------------------------------------------------\n");
	printf("ProduceA.exe(c)           2009/12/01  Version 0.0a\n");
	printf("Format and write a 1.44mb floppy in A: from image.\n");
	printf("Serial No. 0000-0000-654321    All Rights Reserved\n");
	printf("Copyright (C) 1991-2009         Douglas W. Goodall\n");
	printf("--------------------------------------------------\n");
	
	if(2 > argc) {
		printf("usage: producea <filename.ext>");
		exit(EXIT_FAILURE);
	}

	fp = fopen(argv[1],"rb");
	if(NULL == fp) {
		printf("Error opening input file %s\n",argv[1]);
		exit(EXIT_FAILURE);
	}

	biosdisk(INT13_RESET, 0, 0, 0, 0, 0, NULL);

	for(track=0;track<TRKS;track++) {
		for(head=0;head<HDS;head++) {
			format_track(track,head);
			printf("Reading    Track %2d Head %d%c",track+1,head,0x0d);
			fread(buffer1,512,SPT/2,fp);
			printf("Writing    Track %2d Head %d%c",track+1,head,0x0d);
			rc = biosdisk(INT13_WRITE,0,head,track,1,SPT/2,buffer1);
			if(0 != rc) {
				printf("1st write error is 0x%02x\n",rc);
				exit(EXIT_FAILURE);
			}
			printf("Verifying  Track %2d Head %d%c",track+1,head,0x0d);
			rc = biosdisk(INT13_VERIFY,0,head,track,1,SPT/2,buffer1);
			if(0 != rc) {
				printf("1st write error is 0x%02x\n",rc);
				exit(EXIT_FAILURE);
			}
			
			printf("Reading    Track %2d Head %d%c",track+1,head,0x0d);
			fread(buffer2,512,SPT/2,fp);
			printf("Writing    Track %2d Head %d%c",track+1,head,0x0d);
			rc = biosdisk(INT13_WRITE,0,head,track,(SPT/2)+1,SPT/2,buffer2);
			if(0 != rc) {
				printf("2nd write error is 0x%02x\n",rc);
				exit(EXIT_FAILURE);
			}
			printf("Verifying  Track %2d Head %d%c",track+1,head,0x0d);
			rc = biosdisk(INT13_VERIFY,0,head,track,(SPT/2)+1,SPT/2,buffer2);
			if(0 != rc) {
				printf("2nd write error is 0x%02x\n",rc);
				exit(EXIT_FAILURE);
			}

		}	
	}
	fclose(fp);
	printf("Completed");
}

// eof
