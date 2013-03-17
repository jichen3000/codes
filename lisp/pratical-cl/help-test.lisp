(defun get-index (lst value)
    (cond
        ((null lst) 0)
        ((equal (car lst) value) 0)
        (t (+ 1 (get-index (cdr lst) value)))))
(defun get-cd-attr-fn (attr-name)
    (nth 
        (get-index '(:title :artist :rating) attr-name) 
        '(first second third)))
(defun get-attr1 (cd attr-name)
    (apply (get-cd-attr-fn attr-name) (list cd)))
(defmacro get-cd-attr (cd attr-name)
    `(,(get-cd-attr-fn attr-name) ,cd))

(print (get-index '(1 2 3) 1))
(print (get-index '(1 2 3) 2))
(print (get-index '(1 2 3) 3))
(print (get-index '(1 2 3) 5))

(print (get-cd-attr-fn :title))
(print (get-attr1 '("aa" "bb" 3) :title))
; (print (get-attr1 '("aa" "bb" 3) :artist))
(print (get-cd-attr '("aa" "bb" 3) :title))
; (print (get-cd-attr '("aa" "bb" 3) :rating))