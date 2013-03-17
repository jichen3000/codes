; (let ((in (open "D:\\work\\notes\\codes\\lisp\\pratical-cl\\help-test.lisp" :if-does-not-exist nil)))
;   (when in
;     (loop for line = (read-line in nil)
;          while line do (format t "~a~%" line))
;         (close in)))

; should use this type
; (with-open-file (stream "D:\\work\\notes\\codes\\lisp\\pratical-cl\\help-test.lisp")
;     (loop for line = (read-line stream nil)
;          while line do (format t "~a~%" line)))
(with-open-file (stream (pathname "./lisp/pratical-cl/help-test.lisp"))
    (loop for line = (read-line stream nil)
         while line do (format t "~a~%" line)))

; (pathname-directory (pathname "./help-test.lisp"))

;:relative.
(print (make-pathname
    :directory '(:absolute "foo" "bar") :name "baz"
    :type "txt"))

(print *default-pathname-defaults*)

(defparameter *help-test-path* 
    (pathname "./lisp/pratical-cl/help-test.lisp"))
(print (pathname-name *help-test-path*))
(print (pathname-type *help-test-path*))
(print (pathname-name *default-pathname-defaults*))
