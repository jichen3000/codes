(defvar lst '(1 2 3))
(loop for cons on lst
    do (format t "~a" (car cons))
    when (cdr cons) do (format t ", "))
(format t "~%")
(defun println-fn (&optional str)
    (if str
        (format t "~a~%" str)
        (format t "~%")))
(defmacro println (&optional str)
    (if str
        `(format t "~a~%" ,str)
        `(format t "~%")))
(format t "~{~a~^, ~}" lst)
(format t "~%" "")
(println)

(format t "~$~%" pi)


(format t "~,5f~%" pi)
(format t "~f~%" pi 5)

(format t "~d~%" 1000000)
(format t "~:d~%" 1000000)
(format t "~@d~%" 1000000)

(format t "The value is: ~a~%" (list 1 2 3))
(format t "The value is: ~a~&" (list 1 2 3))
(format t "~&")

(format t "~:@d~%" 1000000)
(format t "~12d~%" 1000000)
(format t "~12,'0d~%" 1000000)
(format t "~4,'0d-~2,'0d-~2,'0d~%" 2005 6 10)

(format t "~,4f~%" pi)

(format t "~r~%" 1234)
(format t "~:r~%" 1234)

(format t "file~p~%" 1)
(format t "file~p~%" 10)
(format t "file~p~%" 0)

(format t "~r file~:p~%" 1)
(format t "~r file~:p~%" 10)
(format t "~r file~:p~%" 0)

(format t "~r famil~:@p~%" 10)

(println "ok")
