// ibmbios.h 2009/11/29 dwg - 
// Copyright (C) 2009 Douglas W. Goodall. All Rights Reserved.

// See IBM Technical Reference (Blue Book) Page A-36
#define INT13_RESET 0
#define INT13_STATUS 1
#define INT13_READ 2
#define INT13_WRITE 3
#define INT13_VERIFY 4
#define INT13_FORMAT 5

#define INT14_BAUD_9600   0xe0
#define INT14_BAUD_4800   0xc0
#define INT14_BAUD_2400   0xa0
#define INT14_BAUD_1200   0x80
#define INT14_BAUD_600    0x60
#define INT14_BAUD_300    0x40
#define INT14_BAUD_150    0x20
#define INT14_BAUD_110    0x00
#define INT14_PARITY_NONE 0x00
#define INT14_PARITY_ODD  0x08
#define INT14_PARITY_EVEN 0x10
#define INT14_STOPS_1     0x00
#define INT14_STOPS_2     0x04
#define INT14_BITS_7      0x02
#define INT14_BITS_8      0x03

struct sCHRN {
	unsigned char Cylinder;		// 0 rel
	unsigned char Head;		// 0 rel
	unsigned char sectoRnum; 	// actual (1-18)
	unsigned char Numbytes;		// 0=128 1=256 2=512 3=1024
} format_144[18];

init_chrn_144(int c, int h, int r, int n)
{
	int sector;
	//printf("init_chrn_144(%d,%d,%d,%d); called\n",c,h,r,n);
	for(sector=1;sector<19;sector++) {
		format_144[sector-1].Cylinder  = c;
		format_144[sector-1].Head      = h;
		format_144[sector-1].sectoRnum = sector;
		format_144[sector-1].Numbytes  = n;
	}
}



