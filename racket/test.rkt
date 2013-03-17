#lang racket
(define eternity
  (lambda (x)
    (eternity x)))
(define len1-v2
  ((lambda (length)
     (lambda (l)
       (cond 
         [(null? l) 0]
         [else
          (add1
           (length (cdr l)))])))
   ((lambda (length)
      (lambda (l)
        (cond
          [(null? l) 0]
          [else
           (add1
            (length (cdr l)))])))
    eternity)))
(define len1-v3
  ((lambda (mk-len)
    (mk-len 
     (mk-len mk-len)))
   (lambda (length)
     (lambda (l)
       (cond 
         [(null? l) 0]
         [else
          (add1
           (length (cdr l)))])))))
(define len-v4
  ((lambda (mk-len)
    (mk-len mk-len))
   (lambda (length)
     (lambda (l)
       (cond 
         [(null? l) 0]
         [else
          (add1
           ((length length) (cdr l)))])))))
(define len-v5
  ((lambda (mk-len)
    (mk-len mk-len))
   (lambda (length)
     (lambda (l)
       (cond 
         [(null? l) 0]
         [else
          (add1
           ((lambda (x)
              ((length length) x)) 
            (cdr l)))])))))
(define len-v6
  ((lambda (mk-len)
    (mk-len mk-len))
   (lambda (mk-len)
     ((lambda (length)
        (lambda (l)
          (cond 
            [(null? l) 0]
            [else
             (add1
              (length 
               (cdr l)))])))
      (lambda (x)
        ((mk-len mk-len) x))))))
(define len-v7
  ((lambda (le)
     ((lambda (mk-len)
        (mk-len mk-len))
      (lambda (mk-len)
        (le
         (lambda (x)
           ((mk-len mk-len) x))))))
   (lambda (length)
     (lambda (l)
       (cond 
         [(null? l) 0]
         [else (add1 (length (cdr l)))])))))
(define Y
  (lambda (f)
    ((lambda (x) (x x))
     (lambda (x) (f (lambda (v) ((x x) v)))))))
(define len-v8
  (Y
   (lambda (length)
     (lambda (l)
       (cond 
         [(null? l) 0]
         [else (add1 (length (cdr l)))])))))

;(define (fn f)
;  (fn f))
;(fn (fn f))

(define (testcc lat)
  (let/cc hop                             
   (foldl (lambda (m result)
           (if (null? m)
               (hop #f)
               (cons m result)))
          '() lat)))


(define testcc1
  (lambda (lat)
    (let/cc hop                             
      (cond
        [(null? lat) '()]
        [(eq? (car lat) 2) (hop #t)]
        [else (cons (car lat) (testcc1 (cdr lat)))]))))

(define (testcc2)
  (let/cc hop                             
   (display 'jc)
    (hop #t)
    (display 'mm)))
    
  (define (any-member lst full-lst)
    (ormap (lambda (v)
              (member v full-lst))
            lst))
  
  (define (test-para p)
    (printf "befre p ~s" p)
    (let* ([p 4])
      (printf "after p ~s" p)))
  (define test-predefine
    (letrec ([p '()])
      (lambda ()
        (cond 
          [(null? p)
            (let ([p 1])
              (test-predefine))]
          [(< p 5) (printf "p: ~s \n" p) (add1 p) (test-predefine)]
          [else p]))))
  
 
    
 