(defun hello-world ()
    (let ((msg "hw"))
	(format t msg)))

(hello-world)

(defmacro middle+ (form)
    `(,(second form) ,(first form) ,(third form) ))
(defmacro middle1+ (form)
    (list (second form) (first form) (third form) ))
(print (middle+ (2 + 3)))
(print (middle1+ (2 + 3)))


(print "ok")