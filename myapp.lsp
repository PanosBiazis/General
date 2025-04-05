;; ;;;; My lisp app
;; ;; sbcl --script myapp.lsp

;; (atom 23.5);atom is a function that creates an atom, which can hold one value at a time
;; (list 1 2 3);list is a function that creates a list of values
;; (format t "Hello World");format is a function that prints a string to the standard output (t)
;; (print "Hello World2");print is a function that prints a value to the standard output
;; ;; (let (message "Hello World3");let is a function that creates a variable and assigns it a value
;; ;;     (print message);print is a function that prints a value to the standard output
;; ;; )
;; (let ((message "Hello World3")));let is a function that creates a variable and assigns it a value
;; (defparameter *message* "Hello World4");defparameter is a function that creates a variable and assigns it a value
;; (print *message*)
;; (defvar *message2* "Hello World5");defvar is a function that creates a variable and assigns it a value in the global scope*message* is a special variable in Common Lisp
;; (defconstant PI 3.14159265358979323846);defconstant is a function that creates a constant in the global scope with the specified name and value
;; (defun; function that creates a function named defun with parameters name and body
;;     (add a b);function that creates a function named add with parameters a and b
;;     (+ a b); function that adds a and b together
;;     (- a b); function that subtracts b from a
;;     (* a b); function that multiplies a and b
;;     (/ a b); function that divides a by b
;;     (mod a b); function that returns the remainder of a divided by b
;;     (sqrt a); function that returns the square root of a
;;     (exp a); function that returns e raised to the power of a
;;     (log a); function that returns the natural logarithm of a
;;     (sin a); function that returns the sine of a
;;     (cos a); function that returns the cosine of a
;;     (tan a); function that returns the tangent of a
;;     (asin a); function that returns the arc sine of a
;;     (acos a); function that returns the arc cosine of a
;;     (atan a); function that returns the arc tangent of a
;;     (atan2 a b); function that returns the arc tangent of a and b
;; )

;;;; My lisp app
(atom 23.5)
(list 1 2 3)
(format t "Hello World")
(print "Hello World2")
(let ((message "Hello World3"))
    (print message))
(defparameter *message* "Hello World4")
(print *message*)
(defvar *message2* "Hello World5")
(defconstant MY-PI 3.14159265358979323846)
;; (print MY-PI)
(format t "~%~a~%" MY-PI)
;; (print *message2*)
(format t "~a~%" *message2*)
;; (defun add (a b)
;;     (+ a b )
;;     (- a b)
;;     (* a b)
;;     (/ a b)
;;     (mod a b)
;;     (sqrt a)
;;     (exp a)
;;     (log a)
;;     (sin a)
;;     (cos a)
;;     (tan a)
;;     (asin a)
;;     (acos a)
;;     (atan a)
;;     (atan2 a b))
(defun add (a b c)
    (let ((results (list))) ; Create a list to store results
        (push (+ a b) results) ; Store the result of addition
        (format t "~%~a~%" *results*)
        (push (- a b) results) ; Store the result of subtraction
        (format t "~%~a~%" *results*)
        (push (* a b) results) ; Store the result of multiplication
        (format t "~%~a~%" *results*)
        (push (/ a b) results) ; Store the result of division
        (format t "~%~a~%" *results*)
        (push (mod a b) results) ; Store the result of modulus
        (format t "~%~a~%" *results*)
        (push (sqrt a) results) ; Store the result of square root
        (format t "~%~a~%" *results*)
        (push (exp a) results) ; Store the result of exponentiation
        (format t "~%~a~%" *results*)
        (push (log a) results) ; Store the result of logarithm
        (format t "~%~a~%" *results*)
        (push (sin a) results) ; Store the result of sine
        (format t "~%~a~%" *results*)
        (push (cos a) results) ; Store the result of cosine
        (format t "~%~a~%" *results*)
        (push (tan a) results) ; Store the result of tangent
        (format t "~%~a~%" *results*)
        (push (asin a) results) ; Store the result of arc sine
        (format t "~%~a~%" *results*)
        (push (acos a) results) ; Store the result of arc cosine
        (format t "~%~a~%" *results*)
        (push (atan a) results) ; Store the result of arc tangent
        (format t "~%~a~%" *results*)
        (push (atan2 a b) results) ; Store the result of arc tangent of a and b
        (format t "~%~a~%" *results*)
        (push c results) ; Store the result of c
        (format t "~%~a~%" *c*)
        (nreverse results))) ; Return the results in the original order

(defun get-user-input (prompt)
    
    (let ((a (get-user-input "Enter the first number: "))
          (b (get-user-input "Enter the second number: ")))
        (let ((results (add a b))) ; Call the add function with user inputs
            (format t "Results: ~a~%" results))) ; Display the results
            (format t "~a" prompt) ; Display the prompt
            (read)) ; Read user input

;; (defun main ())
    

;; (main) ; Call the main function to start the program



