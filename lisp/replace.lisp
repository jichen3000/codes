; this function will have side effect
(defun rep1 (lst n value) (setf (nth n lst) value))

; this function will have side effect
(defun rep2 (lst n value) 
	(replace lst (list value) :start1 n :end1 (+ n 1)))

(defun rep-nth (lst n value)
    (cond 
        ((not lst) lst)
        ((equal n 0) (cons value (cdr lst)))
        (t (cons (car lst) (rep-nth (cdr lst) (- n 1) value)))))

(defvar x '(a b c d))

(print x)
(print (rep-nth x 6 '4))
(print (rep-nth x 2 '4))
(print x)

(REP-NTH (list "tt" "mm" 3 T) 2 2)

(print "rep1")
(defvar x '(a b c d))

(print x)
; (print (rep1 x 6 '4))
(print (rep1 x 2 '4))
(print x)

; (defun test-cond (n)
;     (cond 
;         ((equal n 1) (print '1))
;         (t (print 'a))
;         ))
; (test-cond 1)
; (test-cond 2)
