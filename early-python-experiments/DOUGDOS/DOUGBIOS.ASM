	title	dougbios 
	subttl	copyright (c) douglas goodall
	
;DEBUG	equ	1

	.8086

	include dougdos.equ
	
	ASSUME	cs:cseg,ds:cseg,ss:cseg
cseg	SEGMENT	word public

	org	LOADSIZE

	jmp	coldstart
	nop
	jmp	warmstart
	nop
	jmp	const
	nop
	jmp	conin
	nop
	jmp	conout
	nop
	jmp	msgout
	nop
	jmp	loadngo
	nop
	jmp	term
	nop
					
coldstart:
	mov	cs:entryax,ax
	mov	cs:entrybx,bx
	mov	cs:entrycx,cx
	mov	cs:entrydx,dx
	mov	cs:entrybp,bp
	mov	cs:entrysi,si
	mov	cs:entrydi,di
	mov	cs:entryds,ds
	mov	cs:entryes,es
	mov	cs:entryss,ss
	mov	cs:entrysp,sp
	
	mov	ax,cs
	mov	ds,ax
	mov	ss,ax
	mov	es,ax
	mov	sp,offset stktop

warmstart:	
	mov	ah,9
	mov	dx,offset sine
	int	21h
	jmp	dos
		

const:
	mov	al,0
	ret
	
conin:
	mov	al,0
	ret
	
conout:
	mov	ah,14
	mov	bh,0
	mov	bl,0
	int	10h
	ret

msgout:
	mov	ah,9
	int	21h
	ret

; dx ==> filename of xeq file
loadngo:
	mov	ah,61		; Open file
	mov	al,0		; read only
	int	21h
	jnc	load_open_ok
	mov	ah,9
	mov	dx,offset prog_open_err
	int	21h
	mov	ah,4ch
	int	21h
load_open_ok:
	mov	load_file_handle,ax
	mov	ah,66		; Move file pointer
	mov	al,0		; start of file
	mov	bx,load_file_handle
	mov	cx,0
	mov	dx,TPA
	int	21H
	jnc	load_ptr_ok
	mov	ah,9
	mov	dx,offset prog_ptr_err
	int	21h
	mov	ah,4ch
	int	21h
load_ptr_ok:
	mov	ah,63		; Read file		
	mov	bx,load_file_handle
	mov	cx,2318
	mov	dx,TPA
	push	ds
	push	cs
	pop	ds
	int	21h
	pop	ds
	jnc	prog_read_ok
	mov	ah,9
	mov	dx,offset prog_read_err
	int	21h
	mov	ah,4ch
	int	21h
prog_read_ok:
	mov	ah,62		; Close file
	mov	bx,load_file_handle
	int	21h
	jnc	prog_close_ok
	mov	ah,9
	mov	dx,offset prog_close_err
	int	21h
prog_close_ok:
	ret
	

term:
	mov	ah,4ch
	int	21h

load_file_handle	dw	0

prog_open_err	db	'Sorry, program open failed',0dh,0ah,'$'
prog_ptr_err    db      'Sorry, program  ptr  failed',0dh,0ah,'$'
prog_read_err	db	'Sorry, program read failed',0dh,0ah,'$'
prog_close_err	db	'Sorry, program close failed',0dh,0ah,'$'
			
entryax	dw	0
entrybx	dw	0
entrycx	dw	0
entrydx	dw	0
entrybp	dw	0
entrysi	dw	0
entrydi	dw	0	
entryds	dw	0
entryes	dw	0
entryss	dw	0
entrysp	dw	0

sine	db '--------------------------------------------------',0dh,0ah
	db 'Virtual Protocol Adapter Doug''s BIOS  Version 1.4a',0dh,0ah
	db 'Serial No. XXXX-0000-654321    All Rights Reserved',0dh,0ah
	db 'Copyright (C) 1991-2010 6/4/2010 Douglas W Goodall',0dh,0ah
	db '--------------------------------------------------',0dh,0ah
	db '$'

	dw	32 DUP (?)
stktop	dw	0

	org	LOADSIZE+BIOSSIZE
dos:

cseg	ENDS

	end
