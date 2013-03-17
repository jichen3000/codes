(defun jc ()
    "Thie is a example for function"
    (print "jc"))

(jc)
(print (documentation 'jc 'function))

(defun foo (a b &optional c d)
    (list a b c d))
(defun foo1 (a b &optional c (d 5))
    (list a b c d))
(defun foo2 (a b &optional c (d (* a 2)))
    (list a b c d))
(defun foo3 (a b &optional c (d (* a 2) d-supplied-p))
    (list a b c d d-supplied-p))
(print (foo 1 2))
(print (foo 1 2 3))
(print (foo 1 2 3 4))
(print (foo1 1 2))
(print (foo2 1 2))
(print (foo3 1 2))
(print (foo3 1 2 3 4))

(defun jc+ (&rest numbers)
    numbers)

(print (jc+))
(print (jc+ 1))
(print (jc+ 1 2))

(defun jc-key (&key a b c)
    (list a b c))

(print (jc-key))
(print (jc-key :a 1))
;(print (jc-key 1))
(print (jc-key :c 5 :b 3))

(defun jc-key-symbol (&key 
    ((:apple a)) 
    ((:box b) 10) 
    ((:charlie c) 5 c-supplied-p))
    (list a b c c-supplied-p))

(print (jc-key-symbol :apple 100))
;(print (jc-key-symbol :c 100))

(defun jc-return (n)
    (dotimes (i 10)
        (dotimes (j 10)
            (when (> (* i j) n)
                (return-from jc-return (list i j n))))))

(print (jc-return 25))

(print (function jc-return))
(print #'jc-return)

(print (funcall #'jc-return 25))
(print (apply #'jc-return (list 25)))
(defun jc-x (&rest args)
    args)
(print (apply #'jc-x (list 25)))
(print (apply #'jc-x #'jc-x 0 (list 25)))

(apply 'jc-x (list 25))
(print (apply (defun jcmm (x y) (+ x y) ) (list 2 3)))
(print (jcmm 2 3))
((lambda (x y) (+ x y)) 2 3)
(print (lambda (x y) (+ x y)))

(defvar jc-x-fun #'jc-x)
(print (funcall jc-x-fun 25))

(print 'whole)
(defmacro test-whole (&whole ww a b)
    `(list ,ww ,a))
; (print (test-whole 123 45))
(print (macroexpand-1 '(test-whole 123 45)))
