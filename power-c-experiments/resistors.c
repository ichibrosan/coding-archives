//resistors.c Wed, Feb 3, 2010 - dwg initial version
// Copyright (C) 2010 Douglas W. Goodall. All rights reserved.

#include <stdio.h>
#include <stdlib.h>

#define PHASE1
#define PHASE2
#define PHASE3
#define PHASE4

//#define VERBOSE1
//#define VERBOSE2
//#define VERBOSE3
//#define VERBOSE4

// The target array contains the values of the target resistors in ohms.
// There are exactly 28 of them in this application so loops are hard coded.


// These are the resister values you need to build a resistance substitution box

float target[] = {
	1000000.0,	100000.0,	10000.0,	1000.0,	100.0,	10.0,	1.0,
	2000000.0,	200000.0,	20000.0,	2000.0,	200.0,	20.0,	2.0,
	3000000.0,	300000.0,	30000.0,	3000.0,	300.0,	30.0,	3.0,
	4000000.0,	400000.0,	40000.0,	4000.0,	400.0,	40.0,	4.0
};

// THese are the values available at Jameco in 1% resistors

float value[] = {
	6190.0,		1820.0,		16900.0,	6340.0,	78700.0,	26100.0,	165.0,		9310.0,	50000.0,
	27000.0,	221.0,		51000.0,	33.0,	162000.0,	198.0,		316.0,		178.0,	22600.0,
	66.5,		9.8,		392000.0,	174.0,	1910.0,		57600.0,	806.0,		464.0,	37.4,
	43200.0,	100000.0,	2000.0,		160.0,	4990.0,		332000.0,	22100.0,	274.0,	20.0,
	12.1,		750.0,		3570.0,		2100.0,	3160.0,		18.7,		5110.0,		48.7,	9090.0,
	4420.0,		649.0,		75000.0,	4640.0,	8060.0,		1210.0,		130.0,		4020.0,	154.0,
	909.0,		27.4,		0
};



main(int argc,char **argv)
{

	// The found array contains a boolean for each target indicating that a solution
	// has been found.

	int bFound[] = {
		0,			0,			0,			0,		0,		0,		0,
		0,			0,			0,			0,		0,		0,		0,
		0,			0,			0,			0,		0,		0,		0,
		0,			0,			0,			0,		0,		0,		0
	};

	int i,iElements,j,k,t,v,index;
	
	float total;
	
	printf("\n%s Copyright(C) 2010 Douglas W. Goodall. All Rights Reserved.\n",argv[0]);
	
	
#ifdef PHASE1
	printf("\n");
	printf("starting phase 1\n");
	for(t=0;t<28;t++) {
		//printf("searching for target[%d] (%7.3f)\n",t,target[t]);
		if(0 == bFound[t]) {
			for(v=0;v<56;v++) {
				if(target[t] == value[v]) {
					bFound[t] = 1;
					printf("Solution found for target[%02d] (%011.3f) == value[%02d] (%011.3f)\n",
							t,target[t],v,value[v]);
					break;
				}
			}
		}
	}
	printf("phase 1 complete\n");
#endif


#ifdef PHASE2	
	printf("\n");
	printf("starting phase 2\n");
	for(t=0;t<28;t++) {
		if(0 == bFound[t]) {
			for(v=0;v<56;v++) {
				for(index=0;index<56;index++) {
					if(target[t] == value[v]+value[index]) {
						printf("Solution found for target[%02d] (%011.3f) == %011.3f + %011.3f\n",
								t,target[t],value[v],value[index]);
						bFound[t] = 1;
						break;
					}
				}
				if(1 == bFound[t]) break;
			}
		}
	}
	printf("phase 2 complete\n");
#endif


#ifdef PHASE3
	printf("\n");
	printf("starting phase 3\n");
	for(t=0;t<28;t++) {
		if(0 == bFound[t]) {		
			for(v=0;v<56;v++) {			
				for(index=0;index<56;index++) {				
					for(j=0;j<56;j++) {											
#ifdef VERBOSE3
						printf("scanning for target[%02d] (%011.3f), ",t,target[t]);	
						printf("value[%02d] (%011.3f) + ",v,value[v]);
						printf("value[%02d] (%011.3f) + ",index,value[index]);
						printf("value[%02d] (%011.3f) = ",j,value[j]);
						total = value[v] + value[index] + value[j];
						printf("%011.3f | ",total);
						//printf("%012.3f | ",total     - target[t]);
						//printf("%012.3f |", target[t] - total    );
						printf("\n");
#endif						
						if(target[t] == value[v]+value[index]+value[j]) {
							printf("Solution found for target[%02d] (%011.3f) == %011.3f + %011.3f + %011.3f\n",
								t,target[t],value[v],value[index],value[j]);
							//solution[t][1] = v;
							bFound[t] = 1;
							break;
						}					
					}
					if(1 == bFound[t]) break;
				}
				if(1 == bFound[t]) break;				
			}			
		}		
	}
	printf("phase 3 complete\n");
#endif


#ifdef PHASE4	
	printf("\n");
	printf("starting phase 4\n");
	for(t=0;t<28;t++) {	
		if(0 == bFound[t]) {		
			for(v=0;v<56;v++) {			
				for(index=0;index<56;index++) {				
					for(j=0;j<56;j++) {					
						for(k=0;k<56;k++) {
#ifdef VERBOSE4											
							printf("scanning for target[%02d] (%011.3f), ",t,target[t]);	
							printf("value[%02d] (%011.3f) + ",v,value[v]);
							printf("value[%02d] (%011.3f) + ",index,value[index]);
							printf("value[%02d] (%011.3f) + ",j,value[j]);
							printf("value[%02d] (%011.3f) = ",k,value[k]);
							total = value[v] + value[index] + value[j] + value[k];
							printf("%011.3f | ",total);
							printf("\n");
#endif
							if(target[t] == value[v]+value[index]+value[j]+value[k]) {
								printf("Solution found for target[%02d] (%011.3f) == %011.3f + %011.3f + %011.3f + %011.3f\n",
									t,target[t],value[v],value[index],value[j],value[k]);
								bFound[t] = 1;
								break;
							}
						}
						if(1 == bFound[t]) break;											
					}
					if(1 == bFound[t]) break;
				}
				if(1 == bFound[t]) break;				
			}			
		}		
	}
	printf("phase 4 complete\n");
#endif
	
	printf("\n");
	exit(EXIT_SUCCESS);
}
