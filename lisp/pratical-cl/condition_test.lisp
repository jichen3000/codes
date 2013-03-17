(define-condition malformed-log-entry-error (error)
    ((text 
        :initarg :text 
        :reader text)))

(defun parse-log-entry (text)
    (if (well-formed-log-entry-p text)
        (make-instance 'log-entry "do something")
        (error 'malformed-log-entry-error)))

; (handler-case expression 
;     error-clause*)

; error-clause:
; (condition-type ([var]) code)

(defun parse-log-file (file)
  (with-open-file (in file :direction :input)
    (loop for text = (read-line in nil nil) while text
       for entry = (handler-case (parse-log-entry text)
                     (malformed-log-entry-error () nil))
       when entry collect it)))
; use restart instead of handler
(defun parse-log-file (file)
    (with-open-file (in file :direction :input)
        (loop for text = (read-line in nil nil) while text
            for entry = (restart-case (parse-log-entry text)
                            (skip-log-entry () nil))
            when entry collect it)))

(defun log-analyzer ()
    (dolist (log (find-all-logs))
        (analyze-log log)))
(defun log-analyzer ()
  (handler-bind ((malformed-log-entry-error
                  #'(lambda (c)
                      (invoke-restart 'skip-log-entry))))
    (dolist (log (find-all-logs))
      (analyze-log log))))
(defun analyze-log (log)
    (dolist (entry (parse-log-file log))
        (analyze-entry entry)))

; my example:
(define-condition not-int-error (error)
    ((text 
        :initarg :text 
        :reader not-int-error-text)))
(defun get-int-str (int)
    (if (numberp int)
        (format nil "int value: ~a" int)
        (error 'not-int-error :text "not int")))
; (defun get-int-str-list (int-lst)
;     (map 'list #'get-int-str int-lst))
; handler-case version
; (defun get-int-str-list (int-lst)
;     (loop for int in int-lst
;         for int-str = 
;             (handler-case (get-int-str int)
;                 (not-int-error () "not int value"))
;         when int-str collect it))
;restart-case version
(defun get-int-str-list (int-lst)
    (loop for int in int-lst
        for int-str = 
            (restart-case (get-int-str int)
                (skip-int (&optional v) v))
        when int-str collect it))
(defun get-int-str-list-upper (int-lst)
    (handler-bind ((not-int-error 
                        #'(lambda (c)
                            (print (not-int-error-text c))
                            (invoke-restart 'skip-int "not int !!")
                            )))
    (get-int-str-list int-lst)))
; (print (numberp 'ss))
; (format t "int value: ~d~%" 5)

(print (get-int-str-list '(1 2 3)))
(print (get-int-str-list-upper '(1 ss 3)))