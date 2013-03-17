#lang racket
(define (atom? a)
  (not (list? a)))

(define (first l)
  (car l))
(define (second l)
  (cadr l))
  
(define length*
  (lambda (pora)
    (cond
      [(atom? pora) 1]
      [else
       (+ (length* (first pora))
          (length* (second pora)))])))

(define (eternity l)
  (eternity l))
                   
(define (will-stop? fn)
  (#t))

(define (last-try x)
  (and (will-stop? last-try)
       (eternity x)))

(define true-length
  (lambda (l)
    (cond
      [(null? l) 0]
      [else (add1 (true-length (cdr l)))])))

(define len0-v1
  (lambda (l)
    (cond
      [(null? l) 0]
      [else (add1 (eternity (cdr l)))])))

(define len1-v1-0
  (lambda (l)
    (cond
      [(null? l) 0]
      [else (add1 (len0-v1 (cdr l)))])))

(define len1-v1
  (lambda (l)
    (cond
      [(null? l) 0]
      [else 
       (add1 
        ((lambda (l)
           (cond
             [(null? l) 0]
             [else (add1 (eternity (cdr l)))]))
         (cdr l)))])))

(define len2-v1
  (lambda (l)
    (cond
      [(null? l) 0]
      [else
       (add1
        ((lambda (l)
         (cond
           [(null? l) 0]
           [else
            (add1
             ((lambda (l)
                (cond
                  [(null? l) 0]
                  [else 
                   (add1
                    (eternity (cdr l)))]))
              (cdr l)))])) 
         (cdr l)))])))

(define len0-v2
  ((lambda (length-h-fn)
    (lambda (l)
      (cond
        [(null? l) 0]
        [else (add1 (length-h-fn (cdr l)))])))
   eternity))

(define len1-v2-0
  ((lambda (length-h-fn)
    (lambda (l)
      (cond
        [(null? l) 0]
        [else (add1 (length-h-fn (cdr l)))])))
   len0-v2))

(define len1-v2
  ((lambda (length-h-fn)
     (lambda (l)
       (cond
         [(null? l) 0]
         [else (add1 (length-h-fn (cdr l)))])))
   ((lambda (length-h-fn)
      (lambda (l)
        (cond
          [(null? l) 0]
          [else (add1 (length-h-fn (cdr 1)))])))
    eternity)))
   
(define len0-v3
  ((lambda (mk-len)
   (mk-len eternity))
   (lambda (length-h-fn)
     (lambda (l)
       (cond
         [(null? l) 0]
         [else (add1 (length-h-fn (cdr l)))])))
   ))

(define len1-v3-0
  ((lambda (mk-len)
   (mk-len len0-v3))
   (lambda (length-h-fn)
     (lambda (l)
       (cond
         [(null? l) 0]
         [else (add1 (length-h-fn (cdr l)))])))
   ))
(define len1-v3
  ((lambda (mk-len)
   (mk-len 
    (mk-len eternity)))
   (lambda (length-h-fn)
     (lambda (l)
       (cond
         [(null? l) 0]
         [else (add1 (length-h-fn (cdr l)))])))
   ))
(define len2-v31
  ((lambda (mk-len)
   (mk-len 
    (mk-len 
     (mk-len mk-len))))
   (lambda (length-h-fn)
     (lambda (l)
       (cond
         [(null? l) 0]
         [else (add1 (length-h-fn (cdr l)))])))
   ))

(define len0-v31
  ((lambda (mk-len)
   (mk-len mk-len))
   (lambda (length-h-fn)
     (lambda (l)
       (cond
         [(null? l) 0]
         [else (add1 (length-h-fn (cdr l)))])))
   ))

; it actually equals true-length
(define len1-v4
  ((lambda (mk-len)
   (mk-len mk-len))
   (lambda (mk-len)
     (lambda (l)
       (cond
         [(null? l) 0]
         [else (add1 ((mk-len mk-len) (cdr l)))])))
   ))

;(define len-v5-error
;  ((lambda (mk-len)
;   (mk-len mk-len))
;   (lambda (mk-len)
;     ((lambda (invoke-self-fn)
;     (lambda (l)
;       (cond
;         [(null? l) 0]
;         [else (add1 (invoke-self-fn (cdr l)))])))
;     (mk-len mk-len)))
;   ))

(define len1-v5
  ((lambda (mk-len)
   (mk-len mk-len))
   (lambda (mk-len)
     (lambda (l)
       (cond
         [(null? l) 0]
         [else (add1 ((lambda (x)
                         ((mk-len mk-len) x)) 
                      (cdr l)))])))
   ))
;extract the invoke-self-fn method
(define len1-v6
  ((lambda (mk-len)
   (mk-len mk-len))
   (lambda (mk-len)
     ((lambda (length)
        (lambda (l)
          (cond
            [(null? l) 0]
            [else (add1 (length 
                         (cdr l)))])))
      (lambda (last)
        ((mk-len mk-len) last))))
   ))

;extract the intern length method
(define len1-v7
  ((lambda (length)
     ((lambda (mk-len)
        (mk-len mk-len))
      (lambda (mk-len)
        (length
         (lambda (last)
           ((mk-len mk-len) last))))
   ))
   (lambda (length)
     (lambda (l)
       (cond
         [(null? l) 0]
         [else (add1 (length (cdr l)))])))
   ))

(define Y
  (lambda (f)
    ((lambda (x) (x x))
     (lambda (x) (f (lambda (v) ((x x) v)))))))
(define Y-v0
  (lambda (f)
    ((lambda (x) (f (lambda (v) ((x x) v))))
     (lambda (x) (f (lambda (v) ((x x) v)))))))
(define len-fn
  (lambda (length)
    (lambda (l)
      (cond
        [(null? l) 0]
        [else (add1 (length (cdr l)))])))
  )  
(define len-v8
  (Y len-fn))

(define plus
  ((lambda (fn)
     (lambda (x y)
       (fn x y)))
   +))

(define p12-v0
  ((lambda (fn12)
     ((lambda (fn)
        (lambda (x y)
          fn12))
      +))
   (+ 1 2)))
(define p12-v1
  (lambda ()
    ((lambda (x y)
       ((lambda (fn)
          (fn x y))
        +)) 1 2)))
(define fn-p12
  (lambda ()
    (lambda ()
    (p12-v1))))
(define f
  (lambda (x)
    (f x)))
 