; dougdos.asm dwg - 
; This module contains the higher level functions of
; DougDOS. When it needs things done, it calls the
; dougbios functions.

;DEBUG	equ	1

	.8086

	ASSUME	cs:cseg

cseg	SEGMENT	word public

	include dougbios.equ
	include	dougdos.equ
		
	org	LOADSIZE+BIOSSIZE
	
main:
	jmp	dos_init
	nop
	jmp	dos_func
	nop
	
dos_init:
	mov	ax,cs
	mov	ds,ax
	
	mov	dx,offset sine
	call	msgout

;	mov	al,DOSVER
;	call	dos_func
	
	mov	al,RUNXEQ
	mov	dx,offset xeqfilename
	call	dos_func
	
	jmp	term

dos_func:
	mov	bl,al
	mov	bh,0
	shl	bx,1
	jmp	cs:functab[bx]

functab	dw	dos00	; version
	dw	dos01	; loadngo
	dw	dos02	; mmsgout
	dw	dos03
	dw	dos04
	dw	dos05
	dw	dos06
	dw	dos07

dos00:
	; version
	mov	dx,offset func00sine
	call	msgout
	ret

dos01:
	; loadngo
	call loadngo
	call tpa
	ret

dos02:
	call	msgout
	ret

dos03:
	ret

dos04:
	ret

dos05:
	ret

dos06:
	ret

dos07:
	ret

	
sine	db '--------------------------------------------------',0dh,0ah
	db 'Virtual Protocol Adapter Doug''s DOS   Version 1.4a',0dh,0ah
	db 'Serial No. XXXX-0000-654321    All Rights Reserved',0dh,0ah
	db 'Copyright (C) 1991-2010 6/4/2010 Douglas W Goodall',0dh,0ah
	db '--------------------------------------------------',0dh,0ah
	db '$'

xeqfilename	db	'appl.xeq',0

func00sine	db	'dougdos version 1.0.0',0dh,0ah,'$'
func01sine	db	'func01 loadngo running',0dh,0ah,'$'

	org	TPA
tpa:

cseg	ENDS

	end
