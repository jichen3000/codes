(defparameter *fn* 
    (let ((count 0)) 
        #'(lambda () (setf count (1+ count)))))

(print (funcall *fn*))
(print (funcall *fn*))
(print (funcall *fn*))

(defun judge (n)
    (cond
        ((> n 1) (print "1"))
        ((> n 2) (print "2"))
        (T (print "t"))
        ))

(judge 2)
(judge 3)
(judge 1)