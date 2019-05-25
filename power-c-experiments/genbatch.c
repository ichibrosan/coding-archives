// genbatch.c
#include <stdio.h>

main()
{
	int drive;
	int head;
	int sector;
	int track;

	printf("--------------------------------------------------\n");
	printf("GenBatch.exe(c)           2009/12/01  Version 0.0a\n");
	printf("Serial No. 0000-0000-654321    All Rights Reserved\n");
	printf("Copyright (C) 1991-2009         Douglas W. Goodall\n");
	printf("--------------------------------------------------\n");


	drive = 0;
	for(track=0;track<80;track++) {
		for(head=0;head<2;head++) {
			for(sector=0;sector<18;sector++) {
				printf("sec2hdr %d %d %d %d\n",
					drive,head,track,sector+1);
			}
		}
	}
}
