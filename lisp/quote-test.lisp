(defun make-comparison-expr1 (field value)
    (list 'equal (list 'get-cd-attr 'cd field) value))
(defun make-comparison-expr (field value)
  `(equal (get-cd-attr cd ,field) ,value))
(print (make-comparison-expr :rating (+ 2 3)))
(print (make-comparison-expr1 :rating (+ 2 3)))

; The feature of @
(print `(and ,(list 1 2 3)))
(print `(and ,@(list 1 2 3)))
