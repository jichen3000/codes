#lang racket
(define save-k #f)
(define (save-it!)
  (call-with-composable-continuation
   (lambda (k) ; k is the captured continuation
     (set! save-k k)
     0)))

(define save-c #f)
(define (save-itc!)
  (call-with-current-continuation
   (lambda (k) ; k is the captured continuation
     (set! save-c k)
     0)))
(define (pp str)
  (print str))