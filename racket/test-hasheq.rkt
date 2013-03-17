#lang racket
(require "point.rkt")
(define (gen-point-key-list row-col-symbol)
  (map string->number
       (string-split
        (symbol->string row-col-symbol) "_")))
;(gen-point-key-list '1_0)
(define (point-hash->point-list point-hash)
  (hash-map 
   point-hash 
   (lambda (key value)
     (let [(point-indexs (gen-point-key-list key))]
     (gen-point (first point-indexs)
                (second point-indexs)
             value)))))

(define mhash #hasheq((0_0 . 5) (1_4 . 3) (8_8 . 6)))
(point-hash->point-list mhash)

(define mlist '((8 7 8 0) (7 8 8 0)))

(define (gen-point-key-symbol point)
  (string->symbol 
   (string-append (number->string (get-row-index point))
                  "_"
                  (number->string (get-col-index point)))))
;(gen-point-key-symbol 1 0)

(define (point-list->point-hash point-list)
  (foldl (lambda (point result)
           (hash-set result 
                     (gen-point-key-symbol point)
                     (get-value point)))
         (hash) point-list))
(point-list->point-hash mlist)