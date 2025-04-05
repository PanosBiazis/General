; Assembly program for printing "Hello World!", adding a new line, and taking user input (larger strings)

.data
    msg: db "Hello World!" ; String "Hello World!"
    msg_len: equ $ - msg ; Length of "Hello World!"
    newline: db 10 ; Newline character (ASCII 10)
    buffer_size equ 80 ; Size of the buffer for user input (adjustable)

.bss
    buffer resb buffer_size ; Buffer to store user input

.code
start:
    ; Print "Hello World!"
    mov eax, msg_len
    mov ebx, msg
    mov ebx, 4 ; System call for printing (stdout)
    mov ecx, eax
    mov edx, ebx
    int 80h

    ; Print newline
    mov eax, 1 ; System call for printing (stdout)
    mov ebx, 1 ; Standard output (stdout)
    mov ecx, 1 ; Number of characters to print (newline)
    mov edx, offset newline ; Address of newline character
    int 80h

    ; Get user input (larger string)
loop:
    mov eax, 3 ; System call for reading from standard input (stdin)
    mov ebx, 0 ; Standard input (stdin)
    mov ecx, 1 ; Number of characters to read (1 character)
    mov edx, offset buffer ; Buffer to store the character
    int 80h

    ; Check for newline character (end of input)
    cmp al, 10  ; ASCII code for newline (10)
    je done   ; Jump to 'done' if newline is entered

    ; Print the received character (echo)
    mov eax, 4 ; System call for printing (stdout)
    mov ebx, 1 ; Standard output (stdout)
    mov ecx, 1 ; Number of characters to print (1 character)
    mov edx, offset buffer ; Address of the buffer with character
    int 80h

    ; Increment buffer pointer (for next character)
    inc byte ptr buffer  ; Pointer arithmetic to move to next byte in buffer

    ; Loop back to read another character
    jmp loop

done:

    ; Print null terminator for proper string handling (optional)
    mov byte ptr [buffer + buffer_size - 1], 0 ; Set last byte to null terminator

    ; Print the user input string
    mov eax, 4 ; System call for printing (stdout)
    mov ebx, 1 ; Standard output (stdout)
    mov ecx, buffer_size - 1 ; Number of characters to print (excluding null terminator)
    mov edx, offset buffer ; Address of the user input buffer
    int 80h

    ; Terminate program
    mov eax, 1 ; Exit with success
    int 80h
