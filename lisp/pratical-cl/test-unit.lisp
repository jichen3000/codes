(defun report-result (result form 
    &optional test-name)
    (format t "~:[FAIL~;pass~] ... ~a: ~a~%" 
        result test-name form)
    result)

(defun test-+-0 ()
  (report-result
    (= (+ 1 2) 3) '(= (+ 1 2) 3))
  (report-result 
    (= (+ 1 2 3) 6) '(= (+ 1 2 3) 6))
  (report-result
    (= (+ -1 -3) -6) '(= (+ -1 -3) -6)))
(test-+-0)

(defun all-truep (&rest lst)
    (reduce #'equal lst :initial-value t))
; (print (all-truep t t t t))
; (print (all-truep t nil t (print "mm")))
(defmacro check (test-name &body contents)
    `(all-truep ,@(loop for content in contents collect
        `(report-result ,content ',content ,test-name))))


; (let ((*print-right-margin* 25)) 
;   (pprint (macroexpand-1 
;     '(check (= (+ 1 2) 3)
;         (= (+ 1 2 3) 6) ))))
(defmacro pprint-macroexpand-1 (content)
    `(let ((*print-right-margin* 50)) 
        (pprint (macroexpand-1 ',content))
        ))
(defmacro pprint-macroexpand (content)
    `(let ((*print-right-margin* 50)) 
        (pprint (macroexpand ',content))
        ))
; (pprint (macroexpand-1 
;   '(pprint-macroexpand-1 (check (= (+ 1 2) 3) (= (+ 1 2 3) 6)))))
; (pprint-macroexpand-1
;     (check 
;         (= (+ 1 2) 3) 
;         (= (+ 1 2 3) 6) 
;         (= (+ -1 -3) -6))
;     )
; (print "")
(defmacro def-test (test-name parameters &body methods)
    `(defun ,test-name ,(append parameters '(&optional suit-name))
        (check (remove nil (append `(,suit-name) '(,test-name)))
            ,@methods)))
; (defun test-+ ()
;     (check 'test-+
;         (= (+ 1 2) 3) 
;         (= (+ 1 2 3) 6) 
;         (= (+ -1 -3) -6)))
(pprint-macroexpand-1 (def-test test-+ ()
    (= (+ 1 2) 3) 
    (= (+ 1 2 3) 6) 
    (= (+ -1 -3) -6)))
(def-test test-+ ()
    (= (+ 1 2) 3) 
    (= (+ 1 2 3) 6) 
    (= (+ -1 -3) -6))
; (test-+ 'top)
; (test-+)
; (defun test-* ()
;     (check "test-*"
;         (= (* 2 2) 4) 
;         (= (* 5 -3) -15)))
(def-test test-* ()
    (= (* 2 2) 4) 
    (= (* 5 -3) -15))
(print (test-*))

(defmacro def-testsuit (suit-name parameters &body tests)
    `(defun ,suit-name ,(append parameters '(&optional top-suit-name))
        (all-truep
            ,@(loop for m in tests collect 
                `(,@m (remove nil (append `(,@top-suit-name) '(,suit-name))))))))

; (defun test-arithmetic ()
;     (all-truep
;         (test-+ 'test-arithmetic)
;         (test-*)))
; (print (test-arithmetic))

; (pprint-macroexpand-1 (def-testsuit test-arithmetic ()
;     (test-+)
;     (test-*)))
; (print "")
(def-testsuit testsuit-arithmetic ()
    (test-+)
    (test-*))
(print (testsuit-arithmetic))



(pprint-macroexpand-1 (def-testsuit testsuit-all ()
    (testsuit-arithmetic)))
(def-testsuit testsuit-all ()
    (testsuit-arithmetic))
(print (testsuit-all))
