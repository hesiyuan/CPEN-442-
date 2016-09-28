#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "lib_crc.h"

#define MAX_STRING_SIZE	2048

void main( int argc, char *argv[] ) {

    char input_string[MAX_STRING_SIZE];
    char *ptr, *dest, hex_val, prev_byte;
    unsigned long crc_32;
    int a, ch;
    FILE *fp;
	int aInt = 0;
	char str[20];


    printf( "Input: " );
    fgets( input_string, MAX_STRING_SIZE-1, stdin );
   
    ptr = input_string;
    while ( *ptr  &&  *ptr != '\r'  &&  *ptr != '\n' ) ptr++;
    *ptr = 0;
   
    a = 1;

	int count = 0;
    do {

        crc_32         = 0xffffffffL;

		prev_byte = 0;

		sprintf(str, "%d", a);

		ptr = str;

			while (*ptr) {
				crc_32 = update_crc_32(crc_32, *ptr);
				prev_byte = *ptr;
				ptr++;
			}

        crc_32    ^= 0xffffffffL;

		if (a % 1000000 == 0) {
			printf(" a: %d \n", a);
		}

		if (crc_32 == 0x901c098e) {
			printf("found: %s\n", str);
			break;
		}

        a++;

    } while ( 1 );

}  /* main (tst_crc.c) */
