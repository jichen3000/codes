(defun primep (number)
    (when (> number 1)
        (loop for fac from 2 to (isqrt number)
            never (zerop (mod number fac)))))

; (print (primep 13))
; (print (primep 10))

(defun next-prime (number)
    (loop for n from number when (primep n) return n))

; (print (next-prime 13))
; (print (next-prime 144444))

(defun gen-names (para-names)
    (map 'list #'(lambda (x) `(,x (gensym))) para-names))
(print (gen-names '(a b c)))
(defmacro with-gensyms-1 (para-names &body body)
    `(let ,(gen-names para-names)
        ,@body))
(defmacro with-gensyms (para-names &body body)
    `(let ,(loop for x in para-names collect `(,x (gensym)))
        ,@body))
(print  (macroexpand-1 
    '(with-gensyms (ending-value-name) (print "mm"))))
; (defmacro when (condition &rest body)
;   `(if ,condition (progn ,@body)))

; (defmacro do-primes (vars &rest body)
;     (let ((iter (first vars))
;         (start (second vars))
;         (end (third vars)))
;         `(do ((,iter (next-prime ,start) (next-prime (1+ ,iter))))
;             ((> ,iter ,end))
;             ,@body))
;     )
; (defmacro do-primes ((iter start end) &body body)
;     (let ((ending-value-name (gensym)))
;     `(do ((,iter (next-prime ,start) (next-prime (1+ ,iter)))
;         (,ending-value-name ,end))
;         ((> ,iter ,ending-value-name))
;         ,@body)))
(defmacro do-primes ((iter start end) &body body)
    (with-gensyms (ending-value-name)
    `(do ((,iter (next-prime ,start) (next-prime (1+ ,iter)))
        (,ending-value-name ,end))
        ((> ,iter ,ending-value-name))
        ,@body)))

(do-primes (p 0 19)
   (format t "~d " p))
(print "\n")
(do ((p (next-prime 0) (next-prime (1+ p))))
    ((> p 19))
    (format t "~d " p))

(print  (macroexpand-1 
    '(do-primes (ending-value-name 0 (random 100)) (format t "~d " p))))


