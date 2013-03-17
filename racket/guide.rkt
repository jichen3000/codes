#lang racket
(define (extract str)
  (substring str 4 7))
(define (double v)
  ((if (string? v) string-append +) v v))
(define (xo-game)
  (let* ([game-range 20]
         [x (random game-range)]
         [o (random game-range)]
         [diff (number->string (abs (- x o)))])
    (cond
     [(> x o) (string-append "X wins by " diff)]
     [(> o x) (string-append "O wins by " diff)]
     [else "cat's game"])))
(define (atom? x)
  (and (not (pair? x)) (not (null? x))))
(define square
  (lambda (n)
    (* n n)
    )
  )
(define (fibo n)
  (cond 
    [(= n 0) 0]
    [(= n 1) 1]
    [else (+ (fibo (- n 1))
             (fibo (- n 2)))]
    ))
