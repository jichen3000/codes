#lang racket
(define (f x)
  (define (in-f y)
    y)
  (in-f x))

;;it will report a error say that in-f is undefined.
;(in-f 5)