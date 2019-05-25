; loader.asm 6/2/2010 dwg - 
; copyright (c) 2010 douglas goodall. all rights reserved. 

; This is a DOS program and it uses calls to Int 21H
; to request input/output services.

; The function of this program is to load subsequent
; binary modules and get them started.

; first it loads the bios services called dougbios.sys

; second it loads the dos services called dougdos.sys

; third it loads an application program called appl.xeq

; fourth it runs the application program (appl.xeq)


	include	dougdos.equ
	
	.8086

	ASSUME	cs:cseg,ds:dseg,ss:sseg

cseg	SEGMENT	para public 'CODE'

start:	mov	ax,seg dseg
	mov	ds,ax
	mov	ax,seg eseg
	mov	es,ax
	mov	ax,seg sseg
	mov	ss,ax
	ifdef	DEBUG
	nop
	endif
	mov	sp,offset stacktop

	mov	ah,9
	mov	dx,offset sine
	int	21h

	mov	ah,61		; Open file
	mov	al,0		; read only
	mov	dx,offset bios_filename
	int	21h
	jnc	bios_open_ok
	mov	ah,9
	mov	dx,offset bios_open_err
	int	21h
	mov	ah,4ch
	int	21h
bios_open_ok:
	mov	bios_file_handle,ax

	mov	bx,ax
	mov	ah,66		; Move file pointer
	mov	al,2		; end of file
	mov	cx,0
	mov	dx,0
	int	21h
	mov	bios_size_lsw,ax
	mov	bios_size_msw,dx
	mov	ah,66		; Move file pointer
	mov	al,0		; start of file
	mov	bx,bios_file_handle
	mov	cx,0
	mov	dx,LOADSIZE
	int	21H

	mov	ah,63		; Read file		
	mov	bx,bios_file_handle
	mov	cx,bios_size_lsw
	mov	dx,offset bios
	push	ds
	push	cs
	pop	ds
	int	21h
	pop	ds
	jnc	bios_read_ok
	mov	ah,9
	mov	dx,offset bios_read_err
	int	21h
	mov	ah,4ch
	int	21h
bios_read_ok:
	
	mov	ah,62		; Close file
	mov	bx,bios_file_handle
	int	21h
	jnc	bios_close_ok
	mov	ah,9
	mov	dx,offset bios_close_err
	int	21h
	mov	ah,4ch
	int	21h
bios_close_ok:

	mov	ah,61		; Open file
	mov	al,0		; read only
	mov	dx,offset dos_filename
	int	21h
	jnc	dos_open_ok
	mov	ah,9
	mov	dx,offset dos_open_err
	int	21h
	mov	ah,4ch
	int	21h
dos_open_ok:
	mov	dos_file_handle,ax

	mov	bx,ax
	mov	ah,66		; Move file pointer
	mov	al,2		; end of file
	mov	cx,0
	mov	dx,0
	int	21h
	mov	dos_size_lsw,ax
	mov	dos_size_msw,dx
	mov	ah,66		; Move file pointer
	mov	al,0		; start of file
	mov	bx,dos_file_handle
	mov	cx,0
	mov	dx,LOADSIZE+BIOSSIZE
	int	21H

	mov	ah,63		; Read file		
	mov	bx,dos_file_handle
	mov	cx,dos_size_lsw
	mov	dx,offset dos
	push	ds
	push	cs
	pop	ds
	int	21h
	pop	ds
	jnc	dos_read_ok
	mov	ah,9
	mov	dx,offset dos_read_err
	int	21h
	mov	ah,4ch
	int	21h
dos_read_ok:
	
	mov	ah,62		; Close file
	mov	bx,bios_file_handle
	int	21h
	jnc	dos_close_ok
	mov	ah,9
	mov	dx,offset dos_close_err
	int	21h
	mov	ah,4ch
	int	21h
dos_close_ok:


bios:
	db	BIOSSIZE DUP (?)
dos:
	db	DOSSIZE  DUP (?)

cseg	ENDS

dseg	SEGMENT	para public 'DATA'
	org	100h

sine	db '--------------------------------------------------',0dh,0ah
	db 'Virtual Protocol Adapter DougDOS LDR  Version 1.4a',0dh,0ah
	db 'Serial No. XXXX-0000-654321    All Rights Reserved',0dh,0ah
	db 'Copyright (C) 1991-2010 6/4/2010 Douglas W Goodall',0dh,0ah
	db '--------------------------------------------------',0dh,0ah
	db '$'
	
bios_filename	db	'dougbios.sys',0
bios_open_err	db	'Sorry, error opening bios file',0dh,0H,'$'
bios_read_err	db	'Sorry, error reading bios file',0dh,0H,'$'
bios_close_err	db	'Sorry, error closing bios file',0dh,0H,'$'
bios_file_handle	dw	0
bios_size_lsw		dw	0
bios_size_msw		dw	0

dos_filename	db	'dougdos.sys',0
dos_open_err	db	'Sorry, error opening dos file',0dh,0H,'$'
dos_read_err	db	'Sorry, error reading dos file',0dh,0H,'$'
dos_close_err	db	'Sorry, error closing dos file',0dh,0H,'$'
dos_file_handle	dw	0
dos_size_lsw	dw	0
dos_size_msw	dw	0

dseg	ENDS

eseg	SEGMENT	word public
	db 	0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
eseg	ENDS

sseg	SEGMENT	para stack 'STACK'
	dw	STK DUP (?)
stacktop:
sseg	ENDS

	end
