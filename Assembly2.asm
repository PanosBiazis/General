section .data
    msg db "Hello World!", 0          ; String "Hello World!"
    newline db 10, 0                  ; Newline character with null terminator
    buffer_size_format db "%79s", 0   ; Format for scanf to read up to 79 characters

section .bss
    buffer resb 80                    ; Buffer to store user input

section .text
    extern printf, scanf, ExitProcess
    global main

main:
    ; Print "Hello World!"
    mov rdx, msg                      ; Load address of msg into rdx (1st argument to printf)
    mov rcx, rdx                      ; Move rdx to rcx because printf uses rcx for the 1st argument
    call printf                       ; Call printf to print the string

    ; Print newline
    mov rdx, newline                  ; Load address of newline into rdx (1st argument to printf)
    mov rcx, rdx                      ; Move rdx to rcx
    call printf                       ; Call printf to print the newline

    ; Get user input
    mov rdx, buffer_size_format       ; Load address of buffer size format into rdx (2nd argument to scanf)
    mov rcx, buffer                   ; Load address of buffer into rcx (1st argument to scanf)
    call scanf                        ; Call scanf to read user input

    ; Print the user input string
    mov rdx, buffer                   ; Load address of buffer into rdx (1st argument to printf)
    mov rcx, rdx                      ; Move rdx to rcx
    call printf                       ; Call printf to print the user input

    ; Exit the program
    xor rcx, rcx                      ; Set exit code to 0 (1st argument to ExitProcess)
    call ExitProcess                  ; Exit the process
