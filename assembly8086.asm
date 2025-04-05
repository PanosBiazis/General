; ;An assembly program can be categorized under three 
; ;sub-parts — 

; ;* The data section, 

; ;* The bss section, and 

; ;* The text section.


; ;The ‘DATA’ Section 
; ;The syntax for declaring data section is — 
; ;section.data 

; ;The ‘DATA’ section is utilized for announcing instated data or 
; ;constants. 

; ;This data doesn't change at runtime. 

; ;You can announce various constant values, file names, or 
; ;buffer sizes, etc., in this area.

; ;The bss Section 

; ;This section is used for announcing variables. 

; ;The syntax for declaring bss section is — 

; ;Section.bss



; ;The Text Section 

; ;global _start. 

; ;The syntax for announcing text section is — 

; ;section.text 
; ;global _start 
; ;_start: 

; ;The text section is utilized for keeping the genuine code. 
; ;This section must start with the declaration global _start. 

; ;This tells the kernel where the program execution starts.


; ;Comments 
; ;Low-level computing Comments start with a semicolon (;). 
; ;It might contain any printable character including clear. 

; ;; This program shows a message on the screen


; ;Memory Segments 

; ;A segmented memory model partitions the framework 
; ;memory into gatherings of free portions referenced by 
; ;pointers situated in the section registers. 

; ;Each fragment is utilized to contain a particular kind of data. 

; ;One fragment is utilized to contain guidance codes, another 
; ;portion stores the data components, and a third section 
; ;keeps the program stack.


; ;In light of the above discussion, we can specify various 
; ;memory segments as — 

; ;* Data segment — 

; ;It is spoken to by the .data section and the .bss. 
; ;The .data section is utilized to pronounce the memory locale. 
; ;Here data components are stored for the program. 

; ;This section can't be extended after the data components 
; ;are pronounced. 

; ;The .bss section is additionally a static memory section 
; ;that contains buffers for data to be proclaimed later in the 
; ;program. 

; ;This buffer memory is zero-filled.


; ;* Code portion - 

; ;It is spoken to by the .text section. 

; ;This characterizes a zone in memory that stores the 
; ;instruction codes. 

; ;This is likewise a fixed territory. 

; ;+ Stack - 

; ;This portion contains data values went to capacities and 
; ;techniques inside the program


; ; Processor operations, for the most part, include preparing 
; ; information. 

; ; This information can be put away in memory and got to 
; ; from consequently. 

; ; Notwithstanding, perusing information from and putting 
; ; away information into memory hinders the processor. 

; ; To accelerate the processor operations, the processor 
; ; incorporates some inside memory stockpiling areas, called 
; ; registers. 

; ; The registers store information components for handling 
; ; without getting to the memory. 

; ; A set number of registers are incorporated with the 
; ; processor chip.


; ; Data Registers 

  

; ; Four 32-bit data registers are used for arithmetic, logical, 
; ; and other operations. 

; ; These 32-bit registers can be used in three ways — 

; ; ¢ As complete 32-bit data registers: EAX, EBX, ECX, EDX. 

; ; Lower halves of the 32-bit registers can be used as four 
; ; 16-bit data registers: AX, BX, CX, and DX. 

; ; ¢Lower and higher halves of the above-mentioned 
; ;  four 16-bit registers can be used as eight 8-bit data 
; ; registers: AH, AL, BH, BL, CH, CL, DH, and DL. 

; ; AX is the primary accumulator; it is used in input/output 
; ; and most arithmetic instructions. 

; ; BX is known as the base register, as it could be used in 
; ; indexed addressing. 

; ; * CX is known as the count register.

; ; +DX is known as the data register. It is also used in input/ 
; ; output operations. 

; ;Pointer Registers


; ; The pointer registers are 32-bit EIP, ESP, and EBP registers. 
; ; Corresponding 16-bit right portions IP, SP, and BP. 

; ; There are three categories of pointer registers — 

; ; „ nstruction Pointer (IP) - The 16-bit IP register stores the 
; ; offset address of the next instruction to be executed 

; ; „ Stack Pointer (SP) - The 16-bit SP register provides the 
; ; offset value within the program stack. 

; ; Base Pointer (BP) - The 16-bit BP register mainly helps 
; ; * in referencing the parameter variables passed to a 
; ; subroutine.

; ; Index Registers 

  

; ; The 32-bit index registers, ESI and EDI, and their 16-bit 
; ; rightmost portions. 

; ; SI and DI, are used for indexed addressing and sometimes 
; ; used in addition and subtraction. 

; ; There are two sets of index pointers - 

; ; „ Source Index (SI) - It is used as a source index for string 
; ; operations. 

; ; „ Destination Index (DI) - It is used as the destination 
; ; index for string operations.

; ; Segment Registers 

; ; Recalling main concepts 

; ; | Stack Segment 
; ; | Data Segment 
; ; Code segment 

; ; Segment 
; ; Registers 

  

; ; Segments are specific areas defined in a program for 
; ; containing data, code, and stack. 

; ; There are three main segments - 

; ; „ Code Segment - It contains all the instructions to be 
; ; executed. 

; ; Data Segment - It contains data, constants and work 
; ; areas. 

; ; 2 

; ; „ Stack Segment - It contains data and returns addresses 
; ; of procedures or subroutines.


; Addressing mode 

; Instruction 

  

; Most assembly language instructions expect operands to be 
; prepared. 

; An operand address gives the area, where the information 
; to be prepared is put away. 

; A few instructions don't require an operand. 

; Some different instructions may require one, two, or three 
; operands. 

; The three fundamental methods of addressing are — 

; ¢ Register addressing 

; ¢ Immediate addressing 

; ¢ Memory addressing


; Register Addressing 
; In this addressing mode, a register contains the operand. 

; Depending upon the instruction, the register may be the first 
; operand, the second operand or both. 

; For example, 

; MOV DX, TAX_RATE ; Register in the first operand 
; MOV COUNT, CX; Register in the second operand 
; MOV EAX, EBX ;Boththe operands are in registers 

; As processing data between registers does not involve 
; memory, it provides the fastest processing of data.

; Immediate Addressing 

; An immediate operand has a steady worth or an 
; articulation. 

; At the point when instruction with two operands utilizes 
; immediate addressing, the main operand might be a 
; register or memory area, 

; what's more, the subsequent operand is an immediate 
; steady. 

; The principal operand characterizes the length of the 
; information. 

; For example, 

; BYTE_VALUE DB 150; A byte value is defined 
; WORD_VALUE DW 300; A word value is defined 

; ADD BYTE_VALUE, 65; An immediate operand 65 is added 

; MOV AX, 45H; Immediate constant 45H is transferred to AX


; Direct Addressing Mode 

; Direct addressing mode means that the value for a given 
; instruction is pointed to by a given value. 

; This means the value is variable, based on what is stored in 
; memory at a given address. 

; For example, 

; ADD BYTE_VALUE, DL; Adds the register in the memory 
; location 

; MOV BX, WORD_VALUE; Operand from the memory is 
; added to register

; Direct-Offset Addressing 

; This addressing mode uses the arithmetic operators to 
; modify an address. 

; For example, look at the following definitions that define 
; tables of data - 

; BYTE_TABLE DB 14, 15, 22, 45; Tables of bytes 

; WORD_TABLE DW 134, 345, 564, 123; Tables of words

; Indirect Memory Addressing 

; This addressing mode utilizes the computer's ability of 
; Segment: Offset addressing. 

; Generally, the base registers EBX, EBP (or BX, BP) and the 
; index registers (Dl, Sl), coded within square brackets for 
; memory references, are used for this purpose.

; Now we shall see a few arithmetic instructions that are used 
; in a low-level language. To start with the first instruction is 
; INC. 

; @ The INC Instruction 

; The INC instruction is used for incrementing an operand by 
; one. 

; It works on a single operand that can be either in a register 
; or in memory. 

; The INC instruction has the following syntax — 

; INC destination


; ¢ The DEC Instruction 

; The DEC instruction is used for decrementing an operand by 
; one. 

; It works on a single operand that can be either in a register 
; or in memory. 

; The DEC instruction has the following syntax — 

; DEC destination

; * ADD and SUB Instructions 

; The ADD and SUB instructions are used for performing 
; simple addition/subtraction of binary data in byte, word and 
; doubleword size, i.e., for adding or subtracting 8-bit, 16-bit 
; or 32-bit operands, respectively. 

; The ADD and SUB instructions have the following syntax — 

; ADD/SUB _destination, source

; ¢ The MUL/IMUL Instruction 

; There are two instructions for multiplying binary data. The 
; MUL (Multiply) instruction handles unsigned data and the 
; IMUL (Integer Multiply) handles signed data. 

; Both instructions affect the Carry and Overflow flag. 

; The syntax for the MUL/IMUL instructions is as follows — 

; MUL/IMUL multiplier


; ¢* The DIV/IDIV Instructions 

; The division operation generates two elements - a quotient 
; and a remainder. 

; In the case of multiplication, overflow does not occur 
; because double-length registers are used to keep the 
; product. 

; However, in case of division, overflow may occur. The 
; processor generates an interrupt if an overflow occurs. 

; The DIV (Divide) instruction is used for unsigned data and 
; the IDIV (Integer Divide) is used for signed data. 

; The format for the DIV/IDIV instruction - 

; DIV/IDIV divisor


; The processor instruction set provides the instructions AND, 
; OR, XOR, TEST, and NOT Boolean logic. 

; This tests , sets and clears the bits according to the need of 
; the program. 

; The first operand in all the cases could be either in the 
; register or in memory. 

; The second operand could be either in register/memory or an 
; immediate (constant) value. 

; However, memory-to-memory operations are not possible.


; The AND Instruction 

  

; The AND instruction is used for supporting logical 
; expressions by performing bitwise AND operation. 

; The bitwise AND operation returns 1 if the matching bits 
; from both the operands are 1, otherwise, it returns 0. 

; For example — 

; Operand1: 0101 

; Operand2: 0011 

; After AND -> Operand1: 0001 

; The AND operation can be used for clearing one or more 
; bits. For example, say the BL register contains 0011 1010. 

; If you need to clear the high-order bits to zero, you AND it 
; with 0FH

; AND BL, OFH; This sets BL to 0000 1010


; The OR Instruction

  

; The OR instruction is used for supporting logical expression 
; by performing bitwise OR operation. 

; The bitwise OR operator returns 1. 

; if the matching bits from either or both operands are one. 
; It returns 0, if both the bits are zero. 

; For example, 

; Operandi1: 0101 

; Operand2: 0011 

; After OR -> Operandi: 0111 

; The OR operation can be used for setting one or more bits. 

; For example, let us assume the AL register contains 0011 
; 1010, you need to set the four low-order bits, you can OR it 
; with a value 0000 1111, i.e., FH. 

; OR BL, OFH ‚ This sets BLto 0011 1111



; The XOR Instruction 

  

; The XOR instruction implements the bitwise XOR operation. 

; he XOR operation sets the resultant bit to 1, if and only ifthe 
; bits from the operands are different. 

; If the bits from the operands are the same (both O or both 1), 
; the resultant bit is cleared to O. 

; For example, 

; Operandi1: 0101 
; Operand2: 0011 

; After XOR -> Operand1: 0110 

; XORing an operand with itself changes the operand to 0. 
; This is used to clear a register. XOR EAX, EAX


; The TEST Instruction 

  

; The TEST instruction works same as the AND operation, but 
; unlike AND instruction, it does not change the first operand. 

; So, if we need to check whether a number in a register is 
; even or odd, we can also do this using the TEST instruction 
; without changing the original number. 

; TEST AL,01H 

; JZ EVEN_NUMBER


; The NOT Instruction 

  

; The NOT instruction implements the bitwise NOT operation. 

; NOT operation reverses the bits in an operand. The operand 
; could be either in a register or in the memory. 

; For example, 
; Operandi1: 01010011 

; After NOT -> Operand1: 1010 1100

; 8086 Microprocessor Overview


; 8086 Microprocessor is an improved adaptation of 8085 
; Microprocessor. 

; It was planned by Intel in 1976. 

; It is a 16-bit Microprocessor having 20 address lines and16 
; data lines that give up to 1MB stockpiling. 

; It comprises of a ground-breaking guidance set, which gives 
; activities like augmentation and division effectively. 

; It underpins two methods of activity, for example, the Most 
; extreme mode and Minimum mode. 

; The most extreme mode is appropriate for a framework 
; having numerous processors and Minimum mode is 
; reasonable for a framework having a solitary processor.

; Features of 8086 Microprocessor 

  

; The most conspicuous highlights of an 8086 microprocessor 
; are as per the following — 

; It has a guidance line, which is equipped for putting 
; * away six guidance bytes from the memory bringing 
; about quicker handling. 

; It was the initial 16-bit processor having 16-bit ALU, 
; ¢ 16-bit registers, inside data transport, and 16-bit outer 
; data transport bringing about quicker preparation. 

; It is accessible in 3 variants depending on the recurrence 
; of activity — 



; 8086 — 5MHz 8086-2 — 8MHz 8086-1 — 10 MHz 

;  |t utilizes two phases of pipelining, for example, Get 
; Stage and Execute Stage, which improves execution. 

; Bring stage can prefetch up to 6 bytes of directions and 
; stores them in the line. 

; * Execute organize executes these guidelines. 

; ¢ It has 256 vectored interferes. 

; ¢ It comprises of 29,000 transistors.


; Comparison between 8085 and 8086 

; Size — 8085 is the 8-bit microprocessor, while 8086 is a 
; 16-bit microprocessor. 

; Address Bus — 8085 has a 16-bit address transport while 
; 8086 has a 20-bit address transport. 

; Memory — 8085 can access up to 64Kb, while 8086 can 
; access up to 1 Mb of memory. 

; Guidance — 8085 doesn't have a guidance line, while 8086 
; has a guidance line. 

; Pipelining — 8085 doesn't bolster a pipelined engineering 
; while 8086 backings a pipelined design. 

; I/O — 8085 can address 248 = 256 I/O's, while 8086 can get 
; to 2416 = 65,536 I/O's. 

; Cost — The expense of 8085 is low while that of 8086 is high.


; Architecture of 8086 

  

; A Microprocessor is an Integrated Circuit with every one 
; of the elements of a CPU in any case, it can't be utilized 
; stand-alone since not at all like a microcontroller it has no 
; memory or peripherals. 

; 8086 doesn't have a RAM or ROM inside it. 

; Nonetheless, it has inside registers for putting away middle 
; of the road and conclusive outcomes and interfaces with 
; memory situated outside it through the System Bus. 

; 8086 provides the programmer with 14 internal registers, 
; every 16 bits or 2 bytes wide.


; The internal architecture of Intel 8086 is divided into 2 units: 

; * The Bus Interface Unit (BIU) 

; * The Execution Unit (EU). 

; These are explained as following below.

; Bus Interface Unit plays out the accompanying capacities 

; It produces the 20-bit physical address for memory to 
; get to. 

; ¢ It brings guidelines from the memory. 
; * It moves data to and from the memory and |/O. 

; ¢ Keeps up the 6-byte prefetch guidance queue(supports 
; pipelining). 

; BIU mainly contains the 4 Segment registers, the Instruction 
; Pointer, a prefetch queue and an Address Generation Circuit.



; The Execution Unit (EU) 


; The principle parts of the EU are General purpose registers, 
; the ALU, Special purpose registers, the Instruction Register 
; and Instruction Decoder and the Flag Register. 

; Brings instructions from the Queue in BIU, translates and 
; * executes number juggling and rational activities utilizing 
; the ALU. 

; „ Sends control signals for inward data move tasks inside 
; the microprocessor. 

; „ Sends demand signs to the BIU to get to the outside 
; module.



; EU (Execution Unit)


; The execution unit offers Instruction to BIU. 

; * expressing from where to fetch the data and, 

; * then decode and, 

; * execute those guidelines. 

; Its capacity is to control activities on data utilizing the 
; guidance decoder and ALU. 

; EU has no immediate association with system busses. 

; It performs activities over data through BIU.

; Let us now discuss the functional parts of 8086 
; microprocessors. 

; * ALU 

; It manages arithmetic and logical operations, like +, -, x, /, 
; OR, AND, NOT operations.


; ¢* General-purpose register 

; There are 8 general-purpose registers, I.e., AH, AL, BH, BL, 
; CH, CL, DH, and DL. 

; These registers can be used individually to store 8-bit data. 
; It also can be used in pairs to store 16bit data. 

; The valid register pairs are AH and AL, BH and BL, CH and 
; CL, and DH and DL. 

; It is referred to as the AX, BX, CX, and DX respectively. 

; AX register — It is also Known as the accumulator 
; ¢ register. It is used to store operands for arithmetic 
; operations. 

; BX register — It is used as a base register. It is used to 
; ¢ store the starting base address of the memory area 
; within the data segment. 

; CX register — It is referred to as counter. It is used in loop 
; instruction to store the loop counter. 

; DX register — This register is used to hold the I/O port 
; address for I/O instruction.

; 3-stack pointer register

; It is a 16-bit register 

; It holds the address from the start of the segment to the 
; memory location. 

; A word was most recently stored on the stack.


; flag register

; It is a 16-bit register that behaves like a flip-flop. 

; It changes its status according to the result stored in the 
; accumulator. 

; It has 9 flags and they are divided into 2 groups — 
; Conditional Flags and Control Flags.


; Conditional Flags 

; It represents the result of the last arithmetic or logical 
; instruction executed. 

; Following is the list of conditional flags - 

; * Carry flag 

; ¢ Auxiliary flag 
; * Parity flag 

; ¢ Zero flag 

; ¢ Sign flag 

; * Overflow flag


; Control Flags 
; Control flags control the operations of the execution unit. 

; Following is the list of control flags — 

; ¢ Trap flag 
; ¢ Interrupt flag 

; ¢ Direction flag

; BIU takes care of all data and addresses transfers on the 
; buses for the EU. 

; EU has no direct connection with System Buses so this is 
; possible with the BIU. 

; EU and BIU are connected with the Internal Bus.


; It has the following functional parts — 
; ¢ Instruction queue — 

; BIU contains the instruction queue. 

; BIU gets up to 6 bytes of the next instructions and stores 
; them in the instruction queue. 

; When the EU executes instructions and is ready for its next 
; instruction, then it simply reads the instruction from this 
; instruction queue resulting in increased execution speed.


; ¢ Pipelining- 

; Fetching the next instruction while the current instruction 
; executes is called pipelining.



; * Segment register — 

; BIU has 4 segment buses, i.e. CS, DS, SS& ES. 

; It holds the addresses of instructions and data in memory, 
; which are used by the processor to access memory 
; locations. 

; It also contains 1 pointer register IP, which holds the address 
; of the next instruction to executed by the EU. 

; CS - It stands for Code Segment. 
; DS - It stands for Data Segment. 
; SS - It stands for Stack Segment. 

; ES - It stands for Extra Segment.


; ¢ Instruction pointer — 

; It is a 16-bit register used to hold the address of the next 
; instruction to be executed.

; The 8086 microprocessor supports 8 types of instructions — 

; * Data Transfer Instructions 

; * Arithmetic Instructions 

; * Bit Manipulation Instructions 

; + String Instructions 

; Program Execution Transfer Instructions (Branch & Loop 
; Instructions) 

; * Processor Control Instructions 

; * |teration Control Instructions 

; * Interrupt Instructions


; These instructions are used to transfer the data from source 
; operand to the destination operand. 

; Following are the list of instructions under this group 

; Instruction to transfer a word 

; MOV - Used to copy the byte or word from the provided 
; source to the provided destination. 

; * PPUSH - Used to put a word atthe top oftthe stack. 

; POP - Used to get a word from the top of the stack to 
; the provided location. 

; * PUSHA - Used to put all the registers into the stack. 
; * POPA - Used to get words from the stack to all registers. 
; * XCHG - Used to exchange the data from two locations. 

; XLAT - Used to translate a byte in AL using a table in 
; the memory.


; Instructions for input and output port transfer 

; „ IN- Used to read a byte or word from the provided port 
; to the accumulator. 

; „ OUT - Used to send out a byte or word from the 
; accumulator to the provided port. 

; Instructions to transfer the address 

; „ LEA - Used to load the address of operand into the 
; provided register. 

; LDS - Used to load DS register and other provided 
; register from the memory 


; LES - Used to load ES register and other provided 
; register from the memory. 


; Instructions to transfer flag registers 

; ¢ LAHF - Used to load AH with the low byte of the flag 
; register. 

; ¢ AHF - Used to store AH register to the low byte of the 
; flag register. 

; PUSHF -— Used to copy the flag register at the top of the 
; stack. 



; POPF - Used to copy a word at the top of the stack to 
; the flag register. 


; These instructions are used to perform arithmetic operations 
; like addition, subtraction, multiplication, division, etc.


; Instructions to perform addition 

  

; ADD - Used to add the provided byte to byte/word to 
; word. 

; ADC - Used to add with carry. 

; INC - Used to increment the provided byte/word by 1. 

; AAA - Used to adjust ASCII after addition. 

; DAA - Used to adjust the decimal after the addition/ 
; subtraction operation.



; Instructions to perform subtraction 

  

; SUB - Used to subtract the byte from byte/word from 
; word. 

; SBB - Used to perform subtraction with borrow. 

; DEC - Used to decrement the provided byte/word by 1. 

; NPG - Used to negate each bit of the provided byte/ 
; word and add 1/2’s complement. 

; CMP - Used to compare 2 provided byte/word. 

; AAS - Used to adjust ASCII codes after subtraction. 

; DAS - Used to adjust decimal after subtraction.

; Instruction to perform multiplication 

  

; MUL - Used to multiply unsigned byte by byte/word by 
; word. 



; IMUL - Used to multiply signed byte by byte/word by 
; word. 

; * AAM - Used to adjust ASCII codes after multiplication.



; Instructions to perform division 

  

; DIV - Used to divide the unsigned word by byte or 
; unsigned double word by word. 

; IDIV — Used to divide the signed word by byte or signed 
; double word by word. 

; AAD - Used to adjust ASCII codes after division. 

; CBW - Used to fill the upper byte of the word with the 
; copies of sign bit of the lower byte. 

; CWD - Used to fill the upper word of the double word 
; with the sign bit of the lower word.


; These instructions are used to perform operations where 
; data bits are involved, i.e. operations like logical, shift, etc.



; Instructions to perform a logical operation 

  

; NOT - Used to invert each bit of a byte or word. 

; AND - Used for adding each bit in a byte/word with the 
; corresponding bit in another byte/word. 

; OR - Used to multiply each bit in a byte/word with the 
; corresponding bit in another byte/word. 

; XOR - Used to perform Exclusive-OR operation over 
; each bit in a byte/word with the corresponding bit in 
; another byte/word. 

; TEST - Used to add operands to update flags, without 
; affecting operands.


; Instructions to perform shift operations 

  

; SHL/SAL - Used to shift bits of a byte/word towards left 
; and put zero(S) in LSBs. 

; SHR - Used to shift bits of a byte/word towards the right 
; and put zero(S) in MSBs. 

; SAR - Used to shift bits of a byte/word towards the right 
; and copy the old MSB into the new MSB.


; Instructions to perform rotate operations 

  

; ROL - Used to rotate bits of byte/word towards the left, 
; i.e. MSB to LSB and to Carry Flag [CF]. 

; ROR - Used to rotate bits of byte/word towards the 
; right, i.e. LSB to MSB and to Carry Flag [CF]. 

; RCR - Used to rotate bits of byte/word towards the 
; right, i.e. LSB to CF and CF to MSB. 

; RCL — Used to rotate bits of byte/word towards the left, 
; i.e. MSB to CF and CF to LSB.



;String Instructions

; The string is a group of bytes/words and their memory is 
; always allocated in sequential order. 

; Following is the list of instructions under this group - 

; * REP - Used to repeat the given instruction till CX #0. 

; REPE/REPZ - Used to repeat the given instruction until 
; CX=0.orzeroflagZF=1. 

; REPNE/REPNZ - Used to repeat the given instruction 
; until CX = O0 orzeroflagZF=1. 

; MOVS/MOVSB/MOVSW - Used to move the byte/word 
; from one string to another. 

; COMS/COMPSB/COMPSW - Used to compare two 
; string bytes/words. 

; INS/INSB/INSW - Used as an input string/byte/word 
; from the I/O port to the provided memory location. 

; OUTS/OUTSB/OUTSW - Used as an output string/byte/ 
; word from the provided memory location to the I/O port. 

; SCAS/SCASB/SCASW - Used to scan a string and 
; * compare its byte with a byte in AL or string word with a 
; word in AX. 

; LODS/LODSB/LODSW - Used to store the string byte 
; into AL or string word into AX.



; Processor Control Instructions 

; These instructions are used to control the processor action 
; by setting/resetting the flag values. 

; Following are the instructions under this group — 

; STC — Used to set carry flag CF to 1 

; CLC — Used to clear/reset carry flag CF to 0 

; CMC - Used to put complement at the state of carry flag 
; om 

; STD - Used to set the direction flag DF to 1 

; CLD - Used to clear/reset the direction flag DF to 0 

; STI — Used to set the interrupt to enable flag to 1, i.e., 
; enable INTR input. 

; CLI — Used to clear the interrupt enable flag to 0, i-e., 
; disable INTR input.



; Iteration Control Instructions 

  

; These instructions are used to execute the given instructions 
; for number of times. Following is the list of instructions under 
; this group - 

; LOOP - Used to loop a group of instructions until the 
; condition satisfies, i.e., CX=0 

; LOOPE/LOOPZ - Used to loop a group of instructions till 
; it satisfieszZF=1&CX=0 

; LOOPNE/LOOPNZ - Used to loop a group of instructions 
; till it satisfies ZF=0 &CX=0 

; * jCXZ - Used to jump to the provided address if CX=0


; Interrupt Instructions 

  

; These instructions are used to call the interrupt during 
; program execution. 

; INT - Used to interrupt the program during execution 
; and calling service specified. 

; INTO - Used to interrupt the program during execution if 
; OF=1 

; „ IRET - Used to return from interrupt service to the main 
; program


; The different ways in which a source operand is denoted 
; in instruction is known as addressing modes. There are 8 
; different addressing modes in 8086 programming — 

; ¢ Immediate addressing mode 

; The addressing mode in which the data operand is a part of 
; the instruction itself is known as an immediate addressing 
; mode. 

; Example 

; MOV CX, 4929 H, ADD AX, 2387 H, MOV AL, FFH



; ¢ Register addressing mode 

; It means that the register is the source of an operand for an 
; instruction. 

; Example 

; MOV CX, AX; copies the contents of the 16-bit AX register 
; into 

; ; the 16-bit CX register), ADD BX, AX


; * Direct addressing mode 

; The addressing mode in which the effective address of the 
; memory location is written directly in the instruction. 

; Example 

; MOV AX, [1592H], MOV AL, [0300H]



; * Register indirect addressing mode 

; This addressing mode allows data to be addressed at any 
; memory location through an offset address held in any of 
; the following registers: BP, BX, DI & Sl. 

; Example 

; MOV AX, [BX] ; Suppose the register BX contains 4895H, 
; then the contents 

; ADD CX, {BX} ; 4895H are moved to AX


; ¢* Based addressing mode 

; In this addressing mode, the offset address of the operand 
; is given by the sum of contents of the BX/BP registers and 
; 8-bit/16-bit displacement. 

; Example 

; MOV DX, [BX+04], ADD CL, [BX+08]

; * Indexed addressing mode 

; In this addressing mode, the operands offset address is 
; found by adding the contents of Sl or DI register and 8-bit/ 
; 16-bit displacements. 

; Example 

; MOV BX, [SI+16], ADD AL, [DI+16]


; ¢* Based-index addressing mode 

; In this addressing mode, the offset address of the operand is 
; computed by summing the base register to the contents of 

; an Index register. 
; Example 

; ADD CX, [AX+SI], MOV AX, [AX+DI]

; ¢* Based indexed with displacement mode 

; In this addressing mode, the operands offset is computed 
; by adding the base register contents. An Index registers 
; contents and 8 or 16-bit displacement. 

; Example 

; MOV AX, [BX+DI+08], ADD CX, [BX+Sl+16]



; repetition
; Immediate 

  

; The different ways in which a source operand is denoted in instruction is known 
; as addressing modes. There are 8 different addressing modes in 8086 
; programming — 

; Immediate addressing mode 

; The addressing mode in which the data operand is a part of the instruction itself 
; is known as an immediate addressing mode. 

; Example 

; MOV CX, 4929 H, ADD AX, 2387 H, MOV AL, FFH


; Register addressing mode 
; It means that the register is the source of an operand for an instruction. 
; Example 
; MOV CX, AX; copies the contents of the 16-bit AX register into 

; the 16-bit CX register), ADD BX, AX

; Direct addressing mode 

; The addressing mode in which the effective address of the memory location is 
; written directly in the instruction. 

; Example 

; MOV AX, [1592H], MOV AL, [0300H]


; Register indirect addressing mode 

; This addressing mode allows data to be addressed at any memory location 
; through an offset address held in any of the following registers: BP, BX, DI & SI. 

; Example 

; MOV AX, [BX] ; Suppose the register BX contains 4895H, then the contents 
; ADD CX, {BX} ; 4895H are moved to AX


; Based addressing mode 

; In this addressing mode, the offset address of the operand is given by the sum 
; of contents of the BX/BP registers and 8-bit/16-bit displacement. 

; Example 

; MOV DX, [BX+04], ADD CL, [BX+08]



; Indexed addressing mode 

; In this addressing mode, the operands offset address is found by adding the 
; contents of SI or DI register and 8-bit/16-bit displacements. 

; Example 

; MOV BX, [SI+16], ADD AL, [DI+16]

; Based-index addressing mode 

; In this addressing mode, the offset address of the operand is computed by 
; summing the base register to the contents of an Index register. 

; Example 

; ADD CX, [AX+SI], MOV AX, [AX+DI]


; Based indexed with displacement mode 

; In this addressing mode, the operands offset is computed by adding the base 
; register contents. An Index registers contents and 8 or 16-bit displacement. 

; Example 

; MOV AX, [BX+DI+08], ADD CX, [BX+SI+16]

