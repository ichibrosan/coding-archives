// sider.c(exe) dwg - 

#include <stdio.h>
#include <stdlib.h>

#define PROMSIZE 2048

char bRunning;

unsigned char bCode1[PROMSIZE];
unsigned char bCode2[PROMSIZE];
unsigned char bCode3[PROMSIZE];
unsigned char bData1[PROMSIZE];
unsigned char bData2[PROMSIZE];
unsigned char bData4[PROMSIZE];
unsigned char prom[PROMSIZE];

int code1[] = { 0x7e1 };
int code2[] = { 0xf4, 0xf9 };
int code3[] = { 0x73, 0x76, 0x87, 0xf1, 0xf6 };

int data1[] = { 0x7f1 };
int data2[] = { 0x7f2 };
int data4[] = { 0x7f4 };

FILE *fp;

int pc;

impl()
{
	switch(prom[pc]) {
		case 0x00: printf("%04X: brk",pc); break;
		case 0x18: printf("%04X: clc",pc); break;
		case 0xd8: printf("%04X: cld",pc); break;
		case 0x58: printf("%04X: cli",pc); break;
		case 0xb8: printf("%04X: clv",pc); break;
		case 0xca: printf("%04X: dex",pc); break;
		case 0x88: printf("%04X: dey",pc); break;
		case 0xe8: printf("%04X: inx",pc); break;
		case 0xc8: printf("%04X: iny",pc); break;
		case 0xea: printf("%04X: nop",pc); break;
		case 0x48: printf("%04X: pha",pc); break;
		case 0x08: printf("%04X: php",pc); break;
		case 0x68: printf("%04X: pla",pc); break;
		case 0x28: printf("%04X: plp",pc); break;
		case 0x40: printf("%04X: rti",pc); break;
		case 0x60: printf("%04X: rts",pc); break;
		case 0x38: printf("%04X: sec",pc); break;
		case 0xf8: printf("%04X: sed",pc); break;
		case 0x78: printf("%04X: sei",pc); break;
		case 0xaa: printf("%04X: tax",pc); break;
		case 0xa8: printf("%04X: tay",pc); break;
		case 0xba: printf("%04X: tsx",pc); break;
		case 0x8a: printf("%04X: txa",pc); break;
		case 0x9a: printf("%04X: txs",pc); break;
		case 0x98: printf("%04X: tya",pc); break;
	};
}

accum()
{
}

immed()
{
}

zpg()
{
}

zpx()
{
}

zpy()
{
}

abs()
{
}

absx()
{
}

absy()
{
}

ind()
{
}

indx()
{
}

indy()
{
}

relv()
{
}


void decode(void)
{
	char * p;

	if(1 == bCode1[pc]) {
//		printf("\n%04X: Code %02X        ",pc,prom[pc]);
		impl();
		return;
	}
	if(1 == bCode2[pc]) {
		printf("\n%04X: Code %02X %02X     ",pc,prom[pc],prom[pc+1]);
		impl();
		pc += 1;
		return;
	}
	if(1 == bCode3[pc]) {
		printf("\n%04X: Code %02X %02X %02X  ",
			pc,prom[pc],prom[pc+1],prom[pc+2]);
		impl();
		pc += 2;
		return;
	}

	if(1 == bData1[pc]) {
		printf("\n%04X: Data %02X         ",pc,prom[pc]);
		pc += 1;
		return;
	}
	if(1 == bData2[pc]) {
		printf("\n%04X: Data %02X %02X      ",pc,prom[pc],prom[pc+1]);
		pc += 2;
		return;
	}
	if(1 == bData4[pc]) {
		printf("\n%04X: Data %02X %02X %02X  ",
			pc,prom[pc],prom[pc+1],prom[pc+2]);
		pc += 3;
		return;
	}

	impl();
	return;

/*
	switch(prom[pc]) {
		case 0xb9:
			printf("lda [$%02X]	; Abs,y\n",prom[pc+1]);
			pc += 2;
			break;
		case 0xc3:
			printf("cmp $%02X	; Stack Relative\n",prom[pc+1]);
			pc += 2;
			break;
		case 0xf0:
			printf("beq $%02X	; Stack Relative\n",prom[pc+1]);
			pc += 2;
			break;
		case 0xf2:
			printf("sbc ($%02X)	; Direct Indirect\n",prom[pc+1]);
			pc += 2;
			break;
		case 0xf4:
			printf("pea ($%02X)	; \n",prom[pc+1]);
			pc += 3;
			break;
		default:
			impl();			printf("UNK $%02X	; unknown opcode\n",prom[pc]);
			pc += 1;
			break;
	};
*/

}

int main(int argc,char **argv)
{
	char * p;

	int code1_count;
	int code2_count;
	int code3_count;

	int data1_count;
	int data2_count;
	int data4_count;

	int i,j,k;

	memset(bCode1,0,sizeof(bCode1));
	memset(bCode2,0,sizeof(bCode2));
	memset(bCode3,0,sizeof(bCode3));
	memset(bData1,0,sizeof(bData1));
	memset(bData2,0,sizeof(bData2));
	memset(bData4,0,sizeof(bData4));
	memset(prom,0,sizeof(prom));

	code1_count = sizeof(code1)/2;
	code2_count = sizeof(code2)/2;
	code3_count = sizeof(code3)/2;
	data1_count = sizeof(data1)/2;
	data2_count = sizeof(data2)/2;
	data4_count = sizeof(data4)/2;

	if(0 < code1_count) {
		for(i=0;i<code1_count;i++) {
			bCode1[code1[i]] = 1;
		}	
	}
	if(0 < code2_count) {
		for(i=0;i<code2_count;i++) {
			bCode2[code2[i]] = 1;
		}	
	}
	if(0 < code3_count) {
		for(i=0;i<code3_count;i++) {
			bCode3[code3[i]] = 1;
		}	
	}
	if(0 < data1_count) {
		for(i=0;i<data1_count;i++) {
			bData1[data1[i]] = 1;
		}	
	}
	if(0 < data2_count) {
		for(i=0;i<data2_count;i++) {
			bData2[data2[i]] = 1;
		}	
	}
	if(0 < data4_count) {
		for(i=0;i<data4_count;i++) {
			bData4[data4[i]] = 1;
		}	
	}

	fp = fopen("sider22.bin","rb");
	if(NULL == fp) {
		printf("Sorry, could not open sider22.bin\n");
		exit(EXIT_FAILURE);
	}
	fread(prom,PROMSIZE,1,fp);
	fclose(fp);

	bRunning = 1;
	pc = 0;
	while(pc < PROMSIZE) {
		p = decode();
//		if(NULL != p) {
//			printf("%04X: %s",pc,p);
//		}
	}
	exit(EXIT_SUCCESS);
}
