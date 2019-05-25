; appl.asm dwg - 

; This module is an example application program written
; to run under dougdos. It uses bios calls.

	.8086
	ASSUME	cs:cseg
cseg	SEGMENT	word public
	include dougbios.equ
	include	dougdos.equ
	include appl.equ
	org	TPA
	
main:	

;       Using BIOS calls
;	mov	dx,offset sine
;	call	msgout
	
;	Using DOS calls
	mov	al,2
	mov	dx,offset sine
	call	dos_func	
	
	jmp	term

sine	db '--------------------------------------------------',0dh,0ah
	db 'Virtual Protocol Adapter Doug''s APPL  Version 1.4a',0dh,0ah
	db 'Serial No. XXXX-0000-654321    All Rights Reserved',0dh,0ah
	db 'Copyright (C) 1991-2010 6/4/2010 Douglas W Goodall',0dh,0ah
	db '--------------------------------------------------',0dh,0ah
	db '$'

cseg	ENDS

	end
