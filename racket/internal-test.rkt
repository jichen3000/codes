#lang racket
(define (change)
  (let* ([a1 '(1 2)])
    (display a1)
    (define (in-change)
      (display a1)
      (let* ([a1 '(2 3)])
        (display a1)))
    (in-change)
    (display a1)))

(change)