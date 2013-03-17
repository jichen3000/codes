(defmacro backwards (expr)
    (reverse expr))

(backwards ("hello, world" t format))
(backwards ((list 1 2 3) print))


(defun get-index (lst value)
    (cond
        ((null lst) 0)
        ((equal (car lst) value) 0)
        (t (+ 1 (get-index (cdr lst) value)))))
(defun get-cd-attr-fn (attr-name)
    (nth 
        (get-index '(:title :artist :rating :ripped) attr-name) 
        '(first second third fourth)))
(defmacro get-cd-attr (cd attr-name)
    `(,(get-cd-attr-fn attr-name) ,cd))


(defun make-comparison-expr1 (field value)
    (list 'equal (list 'get-cd-attr 'cd field) value))
(defun make-comparison-expr (field value)
  `(equal (get-cd-attr cd ,field) ,value))
(print (make-comparison-expr :rating (+ 2 3)))
(print (make-comparison-expr1 :rating (+ 2 3)))

(defun make-comparisons-list (fields)
  (loop while fields
     collecting (make-comparison-expr 
        (pop fields) (pop fields))))

(print (make-comparisons-list (list :artist "jc" :rating 2 :ripped t)))
(print "ok")