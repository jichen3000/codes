#lang racket
(require json)
(define (test-json)
  (jsexpr->string #hasheq((0_0 . 5) (1_0 . 3) (0_1 . 6))))

(test-json)