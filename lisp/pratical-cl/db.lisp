(defun pp (msg)
    (write-line (string msg)))
(defun range (end)
    (loop for i from 0 below end collect i))

(defun rep-nth (lst n value)
    (cond 
        ((not lst) lst)
        ((equal n 0) (cons value (cdr lst)))
        (t (cons (car lst) (rep-nth (cdr lst) (- n 1) value)))))


(defun make-cd (title artist rating ripped)
    (list title artist rating ripped))

(defvar *db* nil)

(defun add-record (cd)
    (push cd *db*))

(defun dump-db ()
    (format t "~{~{:~a ~10t~}:~%~}" *db*))

(defun prompt-read (prompt)
    (format *query-io* "~a: " prompt)
    (force-output *query-io* )
    (read-line *query-io*))

(defun get-input-int (value)
    (or (parse-integer value :junk-allowed t) 
        0))
(defun prompt-for-cd ()
    (make-cd
        (prompt-read "Title")
        (prompt-read "Artist")
        (get-input-int (prompt-read "Rating"))
        (y-or-n-p (prompt-read "Ripped [y/n]"))))
(defun add-cds ()
    (loop (add-record (prompt-for-cd))
        (if (not (y-or-n-p "Another? [y/n]: "))
            (return))))

(defun save-db (filename)
    (with-open-file 
        (out filename
            :direction :output
            :if-exists :supersede)
        (with-standard-io-syntax
            (print *db* out))))

(defun load-db (filename)
    (with-open-file
        (in filename)
        (with-standard-io-syntax
            (setf *db* (read in)))))

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


(defun make-comparison-expr (field value)
  `(equal (get-cd-attr cd ,field) ,value))

(defun make-comparisons-list (fields)
  (loop while fields
     collecting (make-comparison-expr 
        (pop fields) (pop fields))))

; (defvar mm #'list)
; (print (#'mm 1 2))
; (add-record (make-cd "Roses" "Kathy Matty" 7 t))
; (add-record (make-cd "Skyfall" "Adele" 12 t))
; (add-record (make-cd "CC" "cc" 3 t))
; (add-record (make-cd "ll" "mm" 4 t))
; (add-cds)
; (save-db "./my-cds.db")
; (print (cadr (make-cd "Roses" "Kathy Matty" 7 t)))

; (defun select-by-artist (artist)
;     (remove-if-not 
;         #'(lambda (cd)
;             (equal (cadr cd) artist)) 
;         *db*))
(defun select (selector-fn)
    (remove-if-not selector-fn *db*))
(defun artist-selector (artist)
    #'(lambda (cd)
        (equal (cadr cd) artist)))
; TODO: I can use the andmap in this method
; (defun where (&key title artist rate (ripped nil ripped-p))
;     #'(lambda (cd)
;         (and
;             (if title (equal (first cd) title) t)
;             (if artist (equal (second cd) artist) t)
;             (if rate (equal (fourth cd) rate) t)
;             (if ripped-p (equal (fifth cd) ripped) t)
;             )))
(defmacro where (&rest clauses)
    `#'(lambda (cd) (and ,@(make-comparisons-list clauses))))
(defun update (selector-fn &key title artist rating (ripped nil ripped-p))
    (setf *db*
        (mapcar
            #'(lambda (row)
                (if (funcall selector-fn row)
                    (list 
                        (if title title (first row))
                        (if artist artist (second row))
                        (if rating rating (third row))
                        (if ripped-p ripped (fourth row))
                        )
                    row)
                    ) 
            *db*)))
(defun delete-rows (selector-fn)
    (setf *db* (remove-if selector-fn *db*)))
(load-db "./my-cds.db")
(print (select (where :artist "Kathy Matty")))
(print "db:")
(dump-db)
(update (where :artist "mm") :rating 2)
(print "updated db:")
(dump-db)
(delete-rows (where :artist "mm"))
(print "deleted db:")
(dump-db)
(pp "ok")