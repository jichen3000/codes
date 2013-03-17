#lang racket
(define (foo x y)
  (for/list ([i y])
    (for/list ([j x])
      (list (add1 i) (add1 j)))))  
(define (foo2 . xs)
  (let loop ([xs (reverse xs)] [r '()])
    (if (null? xs)
      (reverse r)
      (for/list ([i (car xs)])
        (loop (cdr xs) (cons (add1 i) r))))))
(define map-two
  (lambda (fn lat)
    (map (lambda (out) 
           (map fn out)) lat)))

(define (gen-square-list n)
  (letrec
      ([G (lambda (index)
            (if (< index 1) '()
            (cons n (G (sub1 index)))))])
    (G n)))

(define (gen-square n)
  (map gen-number-list (gen-square-list n)))

(define (count-time fn n)
  (time
   (for ([i n])
     (fn))))

(define (gen-reverse-number-list n)
  (if (< n 1) '()
      (cons (sub1 n) (gen-reverse-number-list (sub1 n)))))