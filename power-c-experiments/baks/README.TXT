About Douglas Goodall's Power C Utilities

After acquiring some vintage equipment, specifically
an AST Premium 386/25, I decided to load my favorite
DOS C compiler. It is called Power C and may be bought
from Mix Software at a reasonable price of $19 (disk/doc).

After thinking about how I would share my work, I decided
that it would be convenient to have the ability to save
floppy images including boot disks as disk files that
could be emailed or posted on the web. And of course the
need to be able to copy the files back onto floppy disks.

The get720.c program was my first effort at reading
the floppy and storing the data in a file. 

To start with I wanted to read the 3-1/2" floppies to 
establish I could read the sectors. The diska.c program
reads nine sectors into a buffer and display some data.
The program diskb.c reads a sector from a 5-1/4" floppy
and displays some data.

Once I could read the sectors, I wanted to be able to
save the contents in a disk file for later use. The
dska2img.c program reads the 3-1/2" floppy in the a: 
drive and places the data in a file. As you might
expect, dskb2img.c reads a 5-1/4" floppy from the b:
drive and places the data in a file.

Once I could read and save both diskette formats,
I wanted to write them back out. The img2dska.c
program takes a 3-1/2" floppy image file and writes
it back to the a: floppy, which must have been
previously formatted. The img2dskb.c program takes
the 5-1/4" floppy image file and writes it back to
the b: drive, which must have been previously 
formatted.

Then I became discontent that I had to previously 
format floppies and wrote the formata.c program,
which was a little tricky. formata.c does a 
low-level format on the floppy in the a: drive
but does not initialize and fats or directories.

Then I folded the formatting code into the img2dska.c
program to create producea.c. As you might expect,
this program takes a 3-1/2" floppy image and writes
it to the a: drive, formatting as it goes. A nice
progress display shows the head and cylinder as the
process goes on.

I wanted to be able to examine the image files so I
wrote the dump.c program which reads a file and 
displays the data in binary and ascii.

Also I wrote the qsector.c program which reads a
specified drive,track,head, and sector and displays it.

Once I could do that, I wanted to convert physical sectors
into C header files containing the data. The sec2hdr.c
program does that. Just like the qsector.c program, it reads
the specified sector and writes a header file for later
inclusion in a C program. It would be trivial to change the
program to output assembler source files instead.

Having done that I got out the EPROM programmer I bought on
eBay. It is a Data I/O 280 Set Programmer, and a very complete
manual was included. A search of the web resulting in no
hits for software interfacing to the programmer, and a search
of Data I/O's web site didn't help either.

So I wrote the readprom.c program which communicates with the
Data I/O 280 Set Programmer, tells it that it is reading
an Intel 2716, and reads the image which is then saved as
a binary disk file on the PC. To make this work, you turn on
the 280, let it self-test. Then set the RS-232 port for 
1200/8/1/N and initiate Computer Control Mode.

Then you run the program and voila, prom image in a file.
Still to be written is code to do the reverse, but I will
do that when the need arises and add it to the powerc
directory on the server.

These programs are compiled using the make.bat script.

If you have questions beyond this, email me douglas_goodall@mac.com

Have Fun :-)
