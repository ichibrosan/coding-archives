// opcodes.h 2010/02/16 1600 dwg - fix _ansi.h _AND redef problem (CYGWIN) 
// copyright (c) 2010 Douglas Goodall, All Rights Reserved.

// Addressing modes
#define immediate 0x01
#define zeropage  0x02
#define zeropagex 0x03
#define zeropagey 0x04
#define absolute  0x05
#define absolutex 0x06
#define absolutey 0x07
#define indirect  0x08
#define indirectx 0x09
#define indirecty 0x0A
#define accum     0x0B
#define relative  0x0C
#define implied   0x0D

// Processor family color
#define green     0x0e
#define yellow    0x0f
#define red       0x10

// Generic operating codes without addressing modes
// Used in verbose mode
#ifdef VERBOSE
	#define _ADC "ADd with Carry"
	#define _AND_ "memory with A"
	#define _ASL "Arithmetic Shift Left one bit"
	#define _BCC "Branch Carry Clear"
	#define _BCS "Branch Carry Set"
	#define _BEQ "Branch Equals"
	#define _BIT "test BITs in memory with A"
	#define _BMI "Branch MInus"
	#define _BNE "Branch Not Equals"
	#define _BPL "Branch PLus"
	#define _BRK "forced BReaK"
	#define _BVC "Branch on oVerflow Clear"
	#define _BVS "Branch on oVerflow Set"
	#define _CLC "CLear Carry flag"
	#define _CLD "CLear Decimal flag"
	#define _CLI "CLear Interrupt flag"	
	#define _CLV "CLear oVerflow flag"
	#define _CMP "CoMP A with memory"
	#define _CPX "ComPare X with memory"
	#define _CPY "ComPare Y with memory"
	#define _DEC "DECrement memory by one"
	#define _DEX "DEcrement X by one"
	#define _DEY "DEcrement Y by one"
	#define _EOR "Exclusive-OR memory with A"
	#define _INC "INCrement memory by one"
	#define _INX "INcrement X by one"
	#define _INY "INcrement Y by one"
	#define _JMP "JuMP to new location"
	#define _JSR "Jump to SubRoutine"
	#define _LDA "LoaD A from memory"
	#define _LDX "LoaD X from memory"
	#define _LDY "LoaD Y from memory"
	#define _LSR "Logical Shift Right"
	#define _NOP "No OPeration"
	#define _ORA "OR A with memory"
	#define _PHA "PusH Accumulator onto stack"
	#define _PHP "PusH P register onto stack"
	#define _PLA "PulL A from stack"
	#define _PLP "PulL P from stack"
	#define _ROL "ROtate Left one bit"
	#define _ROR "ROtate Right one bit"
	#define _RTI "ReTurn from Interrupt"
	#define _RTS "ReTurn from Subroutine"
	#define _SBC "SuBtract with borrow"
	#define _SEC "SEt Carry flag"
	#define _SED "SEt Decimal flag"
	#define _SEI "SEt Interrupt flag"
	#define _STA "STore A into memory"
	#define _STX "STore X into memory"
	#define _STY "STore Y into memory"
	#define _TAX "Transfer A to X"
	#define _TAY "Trabsfer A to Y"
	#define _TSX "Transfer Stack pointer to X"
	#define _TXA "Transfer X to A"
	#define _TXS "Transfer X to Stack pointer"
	#define _TYA "Transfer Y to A"
	#define _UNK "UNKnown"
#else
	// no nomenclature unless in verbose mode
	#define _ADC ""
	#define _AND_ ""
	#define _ASL ""
	#define _BCC ""
	#define _BCS ""
	#define _BEQ ""
	#define _BIT ""
	#define _BMI ""
	#define _BNE ""
	#define _BPL ""
	#define _BRK ""
	#define _BVC ""
	#define _BVS ""
	#define _CLC ""
	#define _CLD ""
	#define _CLI ""
	#define _CLV ""
	#define _CMP ""
	#define _CPX ""
	#define _CPY ""
	#define _DEC ""
	#define _DEX ""
	#define _DEY ""
	#define _EOR ""
	#define _INC ""
	#define _INX ""
	#define _INY ""
	#define _JMP ""
	#define _JSR ""
	#define _LDA ""
	#define _LDX ""
	#define _LDY ""
	#define _LSR ""
	#define _NOP ""
	#define _ORA ""
	#define _PHA ""
	#define _PHP ""
	#define _PLA ""
	#define _PLP ""
	#define _ROL ""
	#define _ROR ""
	#define _RTI ""
	#define _RTS ""
	#define _SBC ""
	#define _SEC ""
	#define _SED ""
	#define _SEI ""
	#define _STA ""
	#define _STX ""
	#define _STY ""
	#define _TAX ""
	#define _TAY ""
	#define _TSX ""
	#define _TXA ""
	#define _TXS ""
	#define _TYA ""
	#define _UNK ""
#endif

// The opcodes structure contains everything we
// need to know about the 6502 instruction set
// in order to operate the 6502 disassembler.

struct OPCODES_TAG {
 int iOpcode;			// This is the numeric value of the operation code
 int iLength;			// This is the number of bytes in the instruction
 int iMode;				// This is the addressing mode for the instruction
 char szOpcode[4];		// This string contains the mnemonic operation code
 int iFamily;			// This is the processor family supporting the code
#ifdef VERBOSE 
 char szVERBOSE[32];	// This string contains the description of the code
#else
 char szVERBOSE[2];		// In non-verbose mode, it is empty to save space
#endif
} opcodes[] = {

//  Op  L  Addr Mode  Mnem.  Family  Desc       Extension nomenclature

{ 0x00, 1, implied,   "brk", green,  _BRK },
{ 0x01, 2, indirectx, "ora", green,  _ORA },
{ 0x02, 1, immediate, "UNK", red,    _UNK },	// cop b
{ 0x03, 1, immediate, "UNK", red,    _UNK },	// ora d,S
{ 0x04, 1, immediate, "UNK", yellow, _UNK },	// Tsb d
{ 0x05, 2, zeropage,  "ora", green,  _ORA },
{ 0x06, 2, zeropage,  "asl", green,  _ASL },
{ 0x07, 1, immediate, "UNK", red,    _UNK },	//ora [d]
{ 0x08, 1, implied,   "php", green,  _PHP },
{ 0x09, 2, immediate, "ora", green,  _ORA },
{ 0x0A, 1, accum,     "asl", green,  _ASL },
{ 0x0B, 1, immediate, "UNK", red,    _UNK },	// phd
{ 0x0C, 1, immediate, "UNK", yellow, _UNK },	// Tsb a
{ 0x0D, 3, absolute,  "ora", green,  _ORA },
{ 0x0E, 3, absolute,  "asl", green,  _ASL },
{ 0x0F, 1, immediate, "UNK", red,    _UNK },	// ora al

{ 0x10, 2, relative,  "bpl", green,  _BPL },
{ 0x11, 2, indirecty, "ora", green,  _ORA },
{ 0x12, 1, immediate, "UNK", yellow, _UNK },	// Ora (d)
{ 0x13, 1, immediate, "UNK", red,    _UNK },	// ora (d,S),Y
{ 0x14, 1, immediate, "UNK", yellow, _UNK },	// Trb d
{ 0x15, 2, zeropagex, "ora", green,  _ORA },
{ 0x16, 2, zeropagex, "asl", green,  _ASL },
{ 0x17, 1, immediate, "UNK", red,    _UNK },	// ora [d],Y
{ 0x18, 1, implied,   "clc", green,  _CLC },
{ 0x19, 3, absolutey, "ora", green,  _ORA },
{ 0x1A, 1, immediate, "UNK", yellow, _UNK },	// Inc A
{ 0x1B, 1, immediate, "UNK", red,    _UNK },	// tcs
{ 0x1C, 1, immediate, "UNK", yellow, _UNK },	// Trb a
{ 0x1D, 3, absolutex, "ora", green,  _ORA },
{ 0x1E, 3, absolutex, "asl", green,  _ASL },
{ 0x1F, 1, immediate, "UNK", red,    _UNK },	// ora al,X

{ 0x20, 3, absolute,  "jsr", green,  _JSR },
{ 0x21, 2, indirectx, "and", green,  _AND_ },
{ 0x22, 1, immediate, "UNK", red,    _UNK },	// jsl al
{ 0x23, 1, immediate, "UNK", red,    _UNK },	// and d,S
{ 0x24, 2, zeropage,  "bit", green,  _BIT },
{ 0x25, 2, zeropage,  "and", green,  _AND_ },
{ 0x26, 2, zeropage,  "rol", green,  _ROL },
{ 0x27, 1, immediate, "UNK", red,    _UNK },	// and [d]
{ 0x28, 1, implied,   "plp", green,  _PLP },
{ 0x29, 2, immediate, "and", green,  _AND_ },
{ 0x2A, 1, accum,     "rol", green,  _ROL },
{ 0x2B, 1, immediate, "UNK", red,    _UNK },	// pld
{ 0x2C, 3, absolute,  "bit", green,  _BIT },
{ 0x2D, 3, absolute,  "and", green,  _AND_ },
{ 0x2E, 3, absolute,  "rol", green,  _ROL },
{ 0x2F, 1, immediate, "UNK", red,    _UNK },	// and al

{ 0x30, 2, relative,  "bmi", green,  _BMI },
{ 0x31, 1, indirecty, "UNK", green,  _UNK },
{ 0x32, 1, immediate, "UNK", yellow, _UNK },	// And (d)
{ 0x33, 1, immediate, "UNK", red,    _UNK },	// and (d,S),Y
{ 0x34, 1, immediate, "UNK", yellow, _UNK },	// Bit d,X
{ 0x35, 2, zeropagex, "and", green,  _AND_ },	
{ 0x36, 2, zeropagex, "rol", green,  _ROL },
{ 0x37, 1, immediate, "UNK", red,    _UNK },	// and [d],Y
{ 0x38, 1, implied,   "sec", green,  _SEC },
{ 0x39, 3, absolutey, "and", green,  _AND_ },
{ 0x3A, 1, immediate, "UNK", yellow, _UNK },	// Dec A
{ 0x3B, 1, immediate, "UNK", red,    _UNK },	// tsc
{ 0x3C, 1, immediate, "UNK", yellow, _UNK },	// Bit a,X
{ 0x3D, 3, absolutex, "and", green,  _AND_ },
{ 0x3E, 3, absolutex, "rol", green,  _ROL },
{ 0x3F, 1, immediate, "UNK", red,    _UNK },	// and al,X
{ 0x40, 1, implied,   "rti", green,  _RTI },
{ 0x41, 2, indirectx, "eor", green,  _EOR },
{ 0x42, 1, immediate, "UNK", red,    _UNK },	// wdm
{ 0x43, 1, immediate, "UNK", red,    _UNK },	// eor d,S
{ 0x44, 1, immediate, "UNK", red,    _UNK },	// mvp s,d
{ 0x45, 2, zeropage,  "eor", green,  _EOR },
{ 0x46, 2, zeropage,  "lsr", green,  _LSR },
{ 0x47, 1, immediate, "UNK", red,    _UNK },	// eor [dl]
{ 0x48, 1, implied,   "pha", green,  _PHA },
{ 0x49, 2, immediate, "eor", green,  _EOR },
{ 0x4A, 1, accum,     "lsr", green,  _LSR },
{ 0x4B, 1, immediate, "UNK", red,    _UNK },	// phk
{ 0x4C, 3, absolute,  "jmp", green,  _JMP },
{ 0x4D, 3, absolute,  "eor", green,  _EOR },
{ 0x4E, 3, absolute,  "lsr", green,  _LSR },
{ 0x4F, 1, immediate, "UNK", red,    _UNK },	// eor al

{ 0x50, 2, relative,  "bvc", green,  _BVC },
{ 0x51, 2, indirecty, "eor", green,  _EOR },
{ 0x52, 1, immediate, "UNK", yellow, _UNK },	// Eor (d)
{ 0x53, 1, immediate, "UNK", red,    _UNK },	// eor (d,S),Y
{ 0x54, 1, immediate, "UNK", red,    _UNK },	// mvn s,d
{ 0x55, 2, zeropagex, "eor", green,  _EOR },	
{ 0x56, 2, zeropagex, "lsr", green,  _LSR },
{ 0x57, 1, immediate, "UNK", red,    _UNK },	// eor [d],Y
{ 0x58, 1, implied,   "cli", green,  _CLI },
{ 0x59, 3, absolutey, "eor", green,  _EOR },
{ 0x5A, 1, immediate, "UNK", yellow, _UNK },	// Phy
{ 0x5B, 1, immediate, "UNK", red,    _UNK },	// tcd
{ 0x5C, 1, immediate, "UNK", red,    _UNK },	// jmp al
{ 0x5D, 3, absolutex, "eor", green,  _EOR },
{ 0x5E, 3, absolutex, "lsr", green,  _LSR },
{ 0x5F, 1, immediate, "UNK", red,    _UNK },	// eor al,X

{ 0x60, 1, implied,   "rts", green,  _RTS },	
{ 0x61, 2, indirectx, "adc", green,  _ADC },
{ 0x62, 1, immediate, "UNK", red,    _UNK },	// per rl
{ 0x63, 1, immediate, "UNK", red,    _UNK },	// adc d,S
{ 0x64, 1, immediate, "UNK", yellow, _UNK },	// Stz d
{ 0x65, 2, zeropage,  "adc", green,  _ADC },
{ 0x66, 2, zeropage,  "ror", green,  _ROR },
{ 0x67, 1, immediate, "UNK", red,    _UNK },	// adc [d]
{ 0x68, 1, implied,   "pla", green,  _PLA },
{ 0x69, 2, immediate, "adc", green,  _ADC },
{ 0x6A, 1, accum,     "ror", green,  _ROR },
{ 0x6B, 1, immediate, "UNK", red,    _UNK },	// rtl
{ 0x6C, 3, indirect,  "jmp", green,  _JMP },
{ 0x6D, 3, absolute,  "adc", green,  _ADC },
{ 0x6E, 3, absolute,  "ror", green,  _ROR },
{ 0x6F, 1, immediate, "UNK", red,    _UNK },	// adc al

{ 0x70, 2, relative,  "bvs", green,  _BVS },
{ 0x71, 2, indirecty, "adc", green,  _ADC },
{ 0x72, 1, immediate, "UNK", yellow, _UNK },	// Adc (d)
{ 0x73, 1, immediate, "UNK", red,    _UNK },	// adc (d,S),Y
{ 0x74, 1, immediate, "UNK", yellow, _UNK },	// Stz d,X
{ 0x75, 2, zeropagex, "adc", green,  _ADC },
{ 0x76, 2, zeropagex, "ror", green,  _ROR },
{ 0x77, 1, immediate, "UNK", red,    _UNK },	// adc [d],Y
{ 0x78, 1, implied,   "sei", green,  _SEI },	
{ 0x79, 3, absolutey, "adc", green,  _ADC },
{ 0x7A, 1, immediate, "UNK", yellow, _UNK },	// Ply
{ 0x7B, 1, immediate, "UNK", red,    _UNK },	// tdc
{ 0x7C, 1, immediate, "UNK", yellow, _UNK },	// Jmp (a,X)
{ 0x7D, 3, absolutex, "adc", green,  _ADC },
{ 0x7E, 3, absolutex, "ror", green,  _ROR },
{ 0x7F, 1, immediate, "UNK", red,    _UNK },	// adc al,X

{ 0x80, 1, immediate, "UNK", yellow, _UNK },	// Bra r
{ 0x81, 2, indirectx, "sta", green,  _STA },
{ 0x82, 1, immediate, "UNK", red,    _UNK },	// brl rl
{ 0x83, 1, immediate, "UNK", red,    _UNK },	// sta d,S
{ 0x84, 2, zeropage,  "sty", green,  _STY },
{ 0x85, 2, zeropage,  "sta", green,  _STA },
{ 0x86, 2, zeropage,  "stx", green,  _STX },
{ 0x87, 1, immediate, "UNK", red,    _UNK },	// sta [d]
{ 0x88, 1, implied,   "dey", green,  _DEY },
{ 0x89, 1, immediate, "UNK", yellow, _UNK },	// Bit #
{ 0x8A, 1, implied,   "txa", green,  _TXA },
{ 0x8B, 1, immediate, "UNK", red,    _UNK },	// phb
{ 0x8C, 3, absolute,  "sty", green,  _STY },
{ 0x8D, 3, absolute,  "sta", green,  _STA },
{ 0x8E, 3, absolute,  "stx", green,  _STX },
{ 0x8F, 1, immediate, "UNK", red,    _UNK },	// sta al

{ 0x90, 2, relative,  "bcc", green,  _BCC },
{ 0x91, 2, indirecty, "sta", green,  _STA },
{ 0x92, 1, immediate, "UNK", yellow, _UNK },	// Sta (d)
{ 0x93, 1, immediate, "UNK", red,    _UNK },	// sta (d,S),Y
{ 0x94, 2, zeropagex, "sty", green,  _STY },
{ 0x95, 2, zeropagex, "sta", green,  _STA },
{ 0x96, 2, zeropagex, "stx", green,  _STX },
{ 0x97, 1, immediate, "UNK", red,    _UNK },	// sta [d],Y
{ 0x98, 1, implied,   "tya", green,  _TYA },
{ 0x99, 3, absolutey, "sta", green,  _STA },
{ 0x9A, 2, implied,   "txs", green,  _TXS },
{ 0x9B, 1, immediate, "UNK", red,    _UNK },	// txy
{ 0x9C, 1, immediate, "UNK", yellow, _UNK },	// Stzz a
{ 0x9D, 3, absolutex, "sta", green,  _STA },
{ 0x9E, 1, immediate, "UNK", yellow, _UNK },	// Stz a,X
{ 0x9F, 1, immediate, "UNK", red,    _UNK },	// sta al,X

{ 0xA0, 2, immediate, "ldy", green,  _LDY },
{ 0xA1, 2, indirectx, "lda", green,  _LDA },
{ 0xA2, 2, immediate, "ldx", green,  _LDX },
{ 0xA3, 1, immediate, "UNK", red,    _UNK },	// lda d,S
{ 0xA4, 2, zeropage,  "ldy", green,  _LDY },
{ 0xA5, 2, zeropage,  "lda", green,  _LDA },
{ 0xA6, 2, zeropage,  "ldx", green,  _LDX },
{ 0xA7, 1, immediate, "UNK", red,    _UNK },	// lda [d]
{ 0xA8, 1, implied,   "tay", green,  _TAY },
{ 0xA9, 2, immediate, "lda", green,  _LDA },
{ 0xAA, 1, implied,   "tax", green,  _TAX },
{ 0xAB, 1, immediate, "UNK", red,    _UNK },	// plb
{ 0xAC, 3, absolute,  "ldy", green,  _LDY },
{ 0xAD, 3, absolute,  "lda", green,  _LDA },
{ 0xAE, 3, absolute,  "ldx", green,  _LDX },
{ 0xAF, 1, immediate, "UNK", red,    _UNK },	// lda al

{ 0xB0, 2, relative,  "bcs", green,  _BCS },
{ 0xB1, 2, indirecty, "lda", green,  _LDA },
{ 0xB2, 1, immediate, "UNK", yellow, _UNK },	// Lda (d)
{ 0xB3, 1, immediate, "UNK", red,    _UNK },	// lda (d,S),Y
{ 0xB4, 2, zeropagex, "ldy", green,  _LDY },
{ 0xB5, 2, zeropagex, "lda", green,  _LDA },
{ 0xB6, 2, zeropagey, "ldx", green,  _LDX },
{ 0xB7, 1, immediate, "UNK", red,    _UNK },	// lda [d],Y
{ 0xB8, 1, implied,   "clv", green,  _CLV },
{ 0xB9, 3, absolutex, "lda", green,  _LDA },
{ 0xBA, 2, implied,   "tsx", green,  _TSX },
{ 0xBB, 1, immediate, "UNK", red,    _UNK },	// tyx
{ 0xBC, 3, absolutex, "ldy", green,  _LDY },
{ 0xBD, 3, absolutex, "lda", green,  _LDA },
{ 0xBE, 3, absolutey, "ldx", green,  _LDX },
{ 0xBF, 1, immediate, "UNK", red,    _UNK },	// lda al,X

{ 0xC0, 2, immediate, "cpy", green,  _CPY },	
{ 0xC1, 2, indirectx, "cmp", green,  _CMP },
{ 0xC2, 1, immediate, "UNK", red,    _UNK },	// rep #
{ 0xC3, 2, immediate, "UNK", red,    _UNK },	// cmp d,S
{ 0xC4, 2, zeropage,  "cpy", green,  _CPY },
{ 0xC5, 2, zeropage,  "cmp", green,  _CMP },
{ 0xC6, 2, zeropage,  "dec", green,  _DEC },
{ 0xC7, 1, immediate, "UNK", red,    _UNK },	// cmp [d]
{ 0xC8, 1, implied,   "iny", green,  _INY },
{ 0xC9, 2, immediate, "cmp", green,  _CMP },
{ 0xCA, 1, implied,   "dex", green,  _DEX },
{ 0xCB, 1, immediate, "UNK", red,    _UNK },	// wai
{ 0xCC, 3, absolute,  "cpy", green,  _CPY },
{ 0xCD, 3, absolute,  "cmp", green,  _CMP },
{ 0xCE, 3, absolute,  "dec", green,  _DEC },
{ 0xCF, 1, immediate, "UNK", red,    _UNK },	// cmp al

{ 0xD0, 2, relative,  "bne", green,  _BNE },
{ 0xD1, 2, indirecty, "cmp", green,  _CMP },
{ 0xD2, 1, immediate, "UNK", yellow, _UNK },	// Cmp (d)
{ 0xD3, 1, immediate, "UNK", red,    _UNK },	// cmp (d,S),Y
{ 0xD4, 1, immediate, "UNK", red,    _UNK },	// pei d
{ 0xD5, 2, zeropagex, "cmp", green,  _CMP },
{ 0xD6, 2, zeropagex, "dec", green,  _DEC },
{ 0xD7, 1, immediate, "UNK", red,    _UNK },	// cmp [d],Y
{ 0xD8, 1, implied,   "cld", green,  _CLD },
{ 0xD9, 3, absolutex, "cmp", green,  _CMP },
{ 0xDA, 1, immediate, "UNK", yellow, _UNK },	// Phx
{ 0xDB, 1, immediate, "UNK", red,    _UNK },	// stp
{ 0xDC, 1, immediate, "UNK", red,    _UNK },	// jml (a)
{ 0xDD, 3, absolutex, "cmp", green,  _CMP },
{ 0xDE, 3, absolutex, "dec", green,  _DEC },
{ 0xDF, 1, immediate, "UNK", red,    _UNK },	// cmp al,X

{ 0xE0, 2, immediate, "cpx", green,  _CPX },
{ 0xE1, 2, indirectx, "sbc", green,  _SBC },
{ 0xE2, 1, immediate, "UNK", red,    _UNK },	// sep #
{ 0xE3, 1, immediate, "UNK", red,    _UNK },	// sbc d,S
{ 0xE4, 2, zeropage,  "cpx", green,  _CPX },
{ 0xE5, 2, zeropage,  "sbc", green,  _SBC },
{ 0xE6, 2, zeropage,  "inc", green,  _INC },
{ 0xE7, 1, immediate, "UNK", red,    _UNK },	// sbc [d]
{ 0xE8, 1, implied,   "inx", green,  _INX },
{ 0xE9, 2, immediate, "sbc", green,  _SBC },
{ 0xEA, 1, implied,   "nop", green,  _NOP },
{ 0xEB, 1, immediate, "UNK", red,    _UNK },	// xba
{ 0xEC, 3, absolute,  "cpx", green,  _CPX },
{ 0xED, 3, absolute,  "sbc", green,  _SBC },
{ 0xEE, 3, absolute,  "inc", green,  _INC },
{ 0xEF, 1, immediate, "UNK", red,    _UNK },	// sbc al

{ 0xF0, 2, relative,  "beq", green,  _BEQ },
{ 0xF1, 2, indirecty, "sbc", green,  _SBC },
{ 0xF2, 1, immediate, "UNK", yellow, _UNK },	// Sbc (d)
{ 0xF3, 1, immediate, "UNK", red,    _UNK },	// sbc (d,S),Y
{ 0xF4, 1, immediate, "UNK", red,    _UNK },	// pea a
{ 0xF5, 2, zeropagex, "sbc", green,  _SBC },
{ 0xF6, 2, zeropagex, "inc", green,  _INC },
{ 0xF7, 1, immediate, "UNK", red,    _UNK },	// sbc [d],Y
{ 0xF8, 1, implied,   "sed", green,  _SED },
{ 0xF9, 3, absolutey, "sbc", green,  _SBC },
{ 0xFA, 1, immediate, "UNK", yellow, _UNK },	// Plx
{ 0xFB, 1, immediate, "UNK", red,    _UNK },	// xce
{ 0xFC, 1, immediate, "UNK", red,    _UNK },	// jsr (a,X)
{ 0xFD, 3, absolutex, "sbc", green,  _SBC },
{ 0xFE, 3, absolutex, "inc", green,  _INC },
{ 0xFF, 1, immediate, "UNK", red,    _UNK }		// sbc al,X
};

// eof
