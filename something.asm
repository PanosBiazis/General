section .data
    hello db "Hi! Mom!", 10  ; string to print
    helloLen equ $ - hello   ; length of the string

section .text
    global main              ; standard entry point for C programs
    extern printf            ; declare external printf function
    extern ExitProcess       ; declare external ExitProcess function

main:
    ; Print the string
    mov rdi, hello           ; argument 1: pointer to the string
    call printf              ; call printf to print the string

    ; Exit the program
    xor rdi, rdi             ; return code 0 (success)
    call ExitProcess         ; exit the process