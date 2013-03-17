#lang racket
(define f-in #f)
(define (f return)
  (set! f-in return)
  (return 2)
  3)

(f (lambda (x) x))
(for-each
 (lambda (item)
   
   (call/cc f)
   (print item))
 '(1 2 3))

(f-in 5)
(f-in 5)
(f-in 5)