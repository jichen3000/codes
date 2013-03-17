; (do ((n 0 (1+ n))
;      (cur 0 next)
;      (next 1 (+ cur next)))
;     ((= 10 n) cur))

(do ((n 1 (1+ n)))
    ((= n 3) 100)
    (print n))