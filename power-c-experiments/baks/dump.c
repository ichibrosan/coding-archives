// dump.c(exe)

#include <stdio.h>
#include <stdlib.h>

#define BINSIZE 2048
#define COLUMNS 16
#define LINES (BINSIZE/COLUMNS)

int main(int argc,char **argv)
{
	FILE *fp;
	int i,j,k,l,m;	
	unsigned char buffer[BINSIZE];

	if(2 != argc) {
		printf("usage - dump <filespec>\n");
		exit(EXIT_FAILURE);
	}

	fp = fopen(argv[1],"rb");
	if(NULL == fp) {
		printf("Sorry, cannot open input file %s\n",argv[1]);
		exit(EXIT_FAILURE);
	}
	fread(buffer,sizeof(buffer),1,fp);
	fclose(fp);

	for(j=0;j<LINES;j++) {
		printf("\n%04X: ",j*COLUMNS);
		for(i=0;i<COLUMNS;i++) {
			printf("%02X ",buffer[(j*COLUMNS)+i]);
		}
		for(i=0;i<COLUMNS;i++) {
			k = buffer[(j*COLUMNS)+i];
			if(k > 0x1f && k < 0x7f ) {
				printf("%c",k);
			} else {
				printf(".");
			}
		}
	}

	exit(EXIT_SUCCESS);
}


