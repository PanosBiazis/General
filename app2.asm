section .data
    hello: db "Hi! Mom!", 10 ;string to print 
    helloLen: equ  $-hello ;Length of the string



section .text


global _start ;entry point for linker


_start:    ;start here

    mov rax,1 ; sys write 
    mov rdi,1 ; file descriptor (stdout)
    mov rsi,hello ; address of string to output
    mov rdx,helloLen ; length of string
    syscall ; invoke operating system to do system call


    ;end program
    mov rax,60 ;sys_exit
    mov rdi,0  ;error code 0 (success)
    syscall ;call kernel