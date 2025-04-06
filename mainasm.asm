; section .data
;     welcome db 'Welcome to assembly world!!!', 0  ; null-terminated string
;     welcomeLen equ $ - welcome                       ; Calculate the length of the string

; section .text
;     global main
;     extern ExitProcess
;     extern GetStdHandle
;     extern WriteConsoleA

; main:
;     ; Get a handle to the standard output
;     mov rax, -11                        ; STD_OUTPUT_HANDLE
;     call GetStdHandle                   ; rax = handle

;     ; Check if the handle is valid
;     test rax, rax                       ; Check if handle is NULL
;     jz .exit                            ; If NULL, exit

;     ; Prepare the parameters for WriteConsoleA
;     mov rcx, rax                        ; Handle to the console
;     mov rdx, welcome                    ; Pointer to the string
;     mov r8, welcomeLen                  ; Length of the string
;     xor r9, r9                          ; Pointer to number of characters written

;     ; Call WriteConsoleA
;     call WriteConsoleA

; .exit:
;     xor rcx, rcx                        ; Exit code 0
;     call ExitProcess

;for linux


; section .bss
;     ;variables

; section .data
;     ;constants
;     hello:  db  "Hello Assembly World!!!", 30 ;string to print
;     helloLen: equ $-hello ;length  of string

; section .text
;     global _start ;entry point for linker

;     _start: ;start here
;         mov rax, 1 ;system call for write
;         mov rdi, 1 ;file descriptor 1 (stdout)
;         mov rsi, hello ;pointer to string
;         mov rdx, helloLen ;length of string
;         syscall ;write to stdout

;         ;end program
;         mov rax,60 ;sys_exit
;         mov rdi,0 ;error code 0 (success)
;         syscall ;call kernel


global  _main
        extern  _printf
        section .text
  _main:
        push    message
        call    _printf
        add     esp, 4
        ret
   message:
        db      "Hello Assembly World!!!", 0