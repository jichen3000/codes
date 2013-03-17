#lang racket
;chapter 1
(define (atom? x)
  (not (list? x)))
(define (first lat)
  (car lat))
(define (second lat)
  (cadr lat))
(define (third lat)
  (caddr lat))
(define two-in-a-row?-my
  (lambda (lat)
    (cond 
      [(< (length lat) 2)  #f]
      [(eq? (first lat) (second lat)) #t]
      [else (two-in-a-row?-my (cdr lat))])))
(define two-in-a-row-b?
  (lambda (a lat)
    (cond
      [(null? lat) #f]
      [else (or (eq? a (car lat))
                (two-in-a-row-b? (car lat) (cdr lat)))])))
(define two-in-a-row?-v0
  (lambda (lat)
    (cond
      [(null? lat) #f]
      [else (two-in-a-row-b? (car lat) (cdr lat))])))
      
(define sum-of-prefixs-v0
  (lambda (tup)
    (cond
      [(null? tup) '()]
      [else (sum-of-prefixs-b (car tup) (cdr tup))])))
(define sum-of-prefixs-b
  (lambda (a tup)
    (cond 
      [(null? tup) (cons a '())]
      [else
       (cons a (sum-of-prefixs-b (+ a (car tup)) (cdr tup)))]))) 

(define (pick n lat)
  (cond
    ((< n 1) '())
    ((zero? (sub1 n)) (car lat))
    (else (pick (sub1 n) (cdr lat)))))

(define (scramble-b tup rev-pre)
  (cond
    [(null? tup) '()]
    [else (cons (pick (car tup)
                      (cons (car tup) rev-pre))
                (scramble-b (cdr tup)
                            (cons (car tup) rev-pre)))]))
(define (scramble-v0 tup)
  (scramble-b tup '()))

;chapter 2
(define (multi-remove-member-o a lat)
  (cond
    [(null? lat) '()]
    [(eq? a (car lat)) (multi-remove-member-o a (cdr lat))]
    [else (cons (car lat) (multi-remove-member-o a (cdr lat)))]))

(define Y
  (lambda (f)
    ((lambda (x) (x x))
     (lambda (x) (f (lambda (v) ((x x) v)))))))

(define multi-remove-member
  (lambda (a lat)
    ((Y (lambda (mr)
          (lambda (lat)
            (cond 
              [(null? lat) '()]
              [(eq? a (car lat)) (mr (cdr lat))]
              [else (cons (car lat) (mr (cdr lat)))]))))
     lat)))

(define multi-remove-member-let
  (lambda (a lat)
    (letrec
         ((mr (lambda (lat)
                (cond 
                  [(null? lat) '()]
                  [(eq? a (car lat)) (mr (cdr lat))]
                  [else (cons (car lat) (mr (cdr lat)))]))))
       (mr lat))
     ))
         
(define multi-remove-member-f-o
  (lambda (test?)
    (lambda (a lat)
      (cond
        [(null? lat) '()]
        [(test? a (car lat)) ((multi-remove-member-f-o test?) a (cdr lat))]
        [else (cons (car lat) ((multi-remove-member-f-o test?) a (cdr lat)))]))))
(define multi-remove-member-f
  (lambda (test?)
    (letrec
        ((multi-remove-member (lambda (a lat)
               (cond
                 [(null? lat) '()]
                 [(test? a (car lat)) (multi-remove-member a (cdr lat))]
                 [else (cons (car lat) (multi-remove-member a (cdr lat)))]))))
      multi-remove-member)))

(define (member?-o a lat)
  (cond
    [(null? lat) #f]
    [else (or (eq? a (car lat))
         (member?-o a (cdr lat)))]))

(define member?
  (lambda (a lat)
    (letrec
        [(member-h (lambda (l)
                     (cond
                       [(null? l) #f]
                       [else (or (eq? a (car l))
                                 (member-h (cdr l)))])))]
      (member-h lat))))

(define (union-o set1 set2)
  (cond
    [(null? set1) set2]
    [(member? (car set1) set2) (union-o (cdr set1) set2)]
    [else (cons (car set1) (union-o (cdr set1) set2))]))
(define (union-v1 set1 set2)
  (letrec
      ([fn (lambda (set)
             (cond
               [(null? set) set2]
               [(member? (car set) set2) (fn (cdr set))]
               [else (cons (car set) (fn (cdr set)))]))])
    (fn set1)))
(define (union set1 set2)
  (letrec
      ([U (lambda (set)
             (cond
               [(null? set) set2]
               [(M? (car set) set2) (U (cdr set))]
               [else (cons (car set) (U (cdr set)))]))]
       [M? (lambda (a lat)
                  (letrec
                      [(N? (lambda (l)
                                   (cond
                                     [(null? l) #f]
                                     [else (or (eq? a (car l))
                                               (N? (cdr l)))])))]
                    (N? lat)))])
    (U set1)))
(define (union1 set1 set2)
  (cond
    [(null? set2) '()]
    [(member? (car set2) set1) (union1 set1 (cdr set2) )]
    [else (list set1 (car set2) (union1 set1 (cdr set2)) )]))

(define (two-in-a-row? lat)
  (letrec
      ([T? (lambda (a lat)
             (cond
               [(null? lat) #f]
               [else (or (eq? a (car lat))
                         (T? (car lat) (cdr lat)))]))])
    (cond
      [(null? lat) #f]
      [else (T? (car lat) (cdr lat))])))

(define (sum-of-prefixs tup)
  (letrec
      ([S (lambda (a tup)
            (cond 
              [(null? tup) (cons a '())]
              [else
               (cons a (S (+ a (car tup)) (cdr tup)))]))])
    (cond
      [(null? tup) '()]
      [else (S (car tup) (cdr tup))])))

(define (scramble tup)
  (letrec
      ([S (lambda (tup rev-pre)
            (cond
              [(null? tup) '()]
              [else 
               (let 
                   ([rp (cons (car tup) rev-pre)])
               (cons (pick (car tup) rp)
                     (S (cdr tup) rp)))]))])
          (S tup '())))

;Chapter 3
(define (intersect set1 set2)
  (print set1)
  (letrec
      ([I (lambda (set)
            (cond
              [(null? set) '()]
              [(member? (car set) set2) 
               (cons (car set) (I (cdr set)))]
              [else (I (cdr set))]))])
    (cond
      [(null? set2) '()]
      [else (I set1)])))

(define (intersectall-v0 lset)
  (let/cc hop
    (letrec
        ([I (lambda (l)
              (cond
                [(null? (cdr l)) (car l)]
                [(null? (car l)) (hop '())]
                [else (intersect (car l) (I (cdr l)))]))])
      (cond
        [(null? lset) '()]
        [else (I lset)]))))
(define (intersectall-v1 lset)
  (let/cc hop
    (letrec
        ([I (lambda (l)
              (cond
                [(null? (car l)) (hop '())]
                [(null? (cdr l)) (car l)]
                [else (A (car l) (I (cdr l)))]))]
         [A (lambda (set1 set2)
              (letrec
                  ([I (lambda (set)
                        (cond
                          [(null? set) '()]
                          [(member? (car set) set2) 
                           (cons (car set) (I (cdr set)))]
                          [else (I (cdr set))]))])
                (cond
                  [(null? set2) (hop '())]
                  [else (I set1)])))]
         )
      (cond
        [(null? lset) '()]
        [else (I lset)]))))
;It is as same as the v1, but you don't involve the insertsect method.
(define (intersectall lset)
  (let/cc hop
    (letrec
        ([I (lambda (l)
              (cond
                [(null? (cdr l)) (car l)]
                [(null? (car l)) (hop '())]
                [else (intersect 
                       (car l) 
                       (letrec ([result (I (cdr l))])
                         (cond
                           [(null? result) (hop '())]
                           [else result]
                           )))]))])
      (cond
        [(null? lset) '()]
        [else (I lset)]))))

(define (remove-member-beyond-first a lat)
  (letrec
      ([R (lambda (lat)
            (cond
              [(null? lat) '()]
              [(eq? a (car lat)) '()]
              [else (cons (car lat) (R (cdr lat)))]))])
    (R lat)))

(define (remove-member-upto-list a lat)
  (let/cc skip
    (letrec
        ([R (lambda (lat)
              (cond
                [(null? lat) '()]
                [(eq? a (car lat)) (skip (R (cdr lat)))]
                [else (cons (car lat) (R (cdr lat)))]))])
      (R lat))))

;chapter 4
(define (leftmost-print l)
  (print l)
  (display "\n")
  (cond
    [(null? l) (display "0\n")'()]
    [(atom? (car l)) (display "1\n")(car l)]
    [(atom? (leftmost (car l))) (display "2\n")(leftmost (car l))]
    [else (display "3\n")(leftmost (cdr l))]))

(define (leftmost-v0 l)
  (cond
    [(null? l) '()]
    [(atom? (car l)) (car l)]
    [else (let
              ([a (leftmost-v0 (car l))])
            (cond
              [(atom? a) a]
              [else (leftmost-v0 (cdr l))]))]))

(define (leftmost l)
  (let/cc hup
    (letrec 
        ([L (lambda (l)                  
              (cond
                [(null? l) '()]
                [(atom? (car l)) (hup (car l))]
                [else (begin
                        (L (car l))
                        (L (cdr l)))]))])
      (L l))))

(define (remove-member-first*-v0 a lat)
  (letrec 
      ([R (lambda (l)
            (cond
              [(null? l) '()]
              [(eq? a (car l)) (cdr l)]
              [(list? (car l)) 
               (let 
                   ([r-car (R (car l))])
                 (if (equal? (car l) r-car)
                     (cons r-car (R (cdr l)))
                     (cons r-car (cdr l))))]
              [else (cons (car l) (R (cdr l)))]))])
    (R lat)))

(define (depth*-v0 l)
  (cond
    [(null? l) 1]
    [(atom? (car l)) (depth* (cdr l))]
    [else
     (let 
         ([d-cdr (depth* (cdr l))]
          [d-car (add1 (depth* (car l)))])
       (if (>  d-cdr d-car) d-cdr d-car))]))
(define (depth* l)
  (cond
    [(null? l) 1]
    [(atom? (car l)) (depth* (cdr l))]
    [else (max (depth* (cdr l)) (add1 (depth* (car l))))]))


(define rm
  (lambda (a l oh)
    (cond
      [(null? l) (oh 'no)]
      [(atom? (car l))
       (if (eq? (car l) a)
           (cdr l)
           (cons (car l)
                 (rm a (cdr l) oh)))]
      [else
       (if (atom?
            (let/cc oh1
              (rm a (car l) oh1)))
           (cons (car l) (rm a (cdr l) oh))
           (cons (rm a (car l) 0) (cdr l)))])))
(define (remove-member-first*-v1 a lat)
  (let ([new-l (let/cc say (rm a lat say))])
    (if (atom? new-l) lat new-l)))

; Define letcc
;
(define-syntax letcc
  (syntax-rules ()
    ((letcc var body ...)
     (call-with-current-continuation
       (lambda (var)  body ... )))))

; Define try
;
(define-syntax try 
  (syntax-rules () 
    ((try var a . b) 
     (letcc success 
       (letcc var (success a)) . b))))
(define (remove-member-first* a lat)
  (try oh (rm a lat oh) lat))
  
;chapter 5
(define (diner food)
  (list 'milkshake food))

(define omnivore
  (let ([x 'minestrone])
    (lambda (food)
      (set! x food)
      (list food x))))
;(define x '())
;(define (dinerR food)
;  (set! x food)
;  (list 'milkshake food))
(define ingredients '())
(define (sweet-toothL food)
  (set! ingredients (cons food ingredients))
  (list food 'me))

(define (deep-v1 depth)
  (cond
    [(zero? depth) 'pizza]
    [else (cons (deepM (sub1 depth)) '())]))
;(define Rs '())
;(define Ns '())
;(define (deepR n)
;  (let ([result (deep n)])
;    (set! Rs (cons result Rs))
;    (set! Ns (cons n Ns))
;    result))
(define (find n Ns Rs)
  (letrec
      ([A (lambda (ns rs)
            (cond
              [(null? ns) #f]
              [(= (car ns) n) (car rs)]
              [else (A (cdr ns) (cdr rs))]))])
    (A Ns Rs)))
(define deepM-v1
  (let ([Rs '()]
        [Ns '()])
    (lambda (n)
      (let ([exists (find n Ns Rs)])
      (if exists
          exists
          (let ([result (deep n)])
            (set! Rs (cons result Rs))
            (set! Ns (cons n Ns))
            result))))))
(define (len-v0 l)
  (print l)
  (cond
    [(null? l) 0]
    [else (add1 (len-v0 (cdr l)))]))

(define len-v1
  (let ([h 0])
    (set! h
          (lambda (l)
            (print l)
            (cond
              [(null? l) 0]
              [else (add1 (h (cdr l)))])))
    h))
(define L
  (lambda (len1)
    (lambda (l)
      (cond
        [(null? l) 0]
        [else (add1 (len1 (cdr l)))]))))
(define len-v2
  (let ([h '()])   
    (set! h
          (L (lambda (arg) (print arg) (h arg))))
    h))
(define Y!
  (lambda (L)
    (let ([h (lambda (l) '())])
      (set! h
            (L (lambda (arg) (h arg))))
      h)))
(define len-v3
  (Y! L))
(define Y-bang
  (lambda (f)
    (letrec
        ([h (f (lambda (arg) (h arg)))])
      h)))
(define len
  (Y-bang L))

(define biz
  (let ([x 0])
    (lambda (f)
      (set! x (add1 x))
      (lambda (a)
        (if (= a x) 0 (f a))))))

;chapter 7
(define counter 0)
(define set-counter 0)
(define consC
  (let ([N 0])
    (set! counter (lambda () N))
    (set! set-counter (lambda (x) (set! N x)))
    (lambda (x y)
      (set! N (add1 N))
      (cons x y))))
(define supercounter
  (lambda (f)
    (letrec
        ([S (lambda (n)
              (if (zero? n)
                  (f n)
                  (begin
                    (f n)
                    (S (sub1 n)))))])
      (S 1000)
      (counter))))
(define (deep depth)
  (if (zero? depth) 'pizza (consC (deep (sub1 depth)) '())))

(define deepM
  (let ([Rs '()]
        [Ns '()])
    (lambda (n)
      (let ([exists (find n Ns Rs)])
      (if exists
          exists
          (let ([result (if (zero? n)
                            'pizza
                            (consC (deepM (sub1 n)) '()))])
            (set! Rs (cons result Rs))
            (set! Ns (cons n Ns))
            result))))))
(define remove-member-first*-v2
  (lambda (a l)
    (letrec
        ([R (lambda (l)
              (cond
                [(null? l) '()]
                [(atom? (car l))
                 (if (eq? (car l) a)
                     (cdr l)
                     (consC (car l) (R (cdr l))))]
                [else
                 (let ([av (R (car l))])
                   (if (equal? (car l) av)
                       (consC (car l) (R (cdr l)))
                       (consC av (cdr l))))]))])
      (R l))))

;chapter 8
;(require scheme/mpair)
;(define kar mcar)
;(define kdr mcdr)
;(define kons mcons)
;(define set-kdr set-mcdr!)
(define kons1-v1
  (lambda (kar kdr)
    (lambda (selector)
      (selector kar kdr))))
(define kons
  (lambda (a d)
    (let ([c (bons a)])
      (set-kdr c d)
      c)))
(define kar1-v1
  (lambda (c)
    (c (lambda (a d) a))))
(define kdr1-v1
  (lambda (c)
    (c (lambda (a d) d))))
(define kar
  (lambda (c)
    (c (lambda (s a d) a))))
(define kdr
  (lambda (c)
    (c (lambda (s a d) d))))
(define set-kdr
  (lambda (c x)
    ((c (lambda (s a d) s)) x)))
(define bons
  (lambda (kar)
    (let ([kdr '()])
      (lambda (selector)
        (selector
         (lambda (x) (set! kdr x))
         kar kdr)))))
(define kounter 0)
(define set-kounter 0)
(define konsC
  (let ([N 0])
    (set! kounter (lambda () N))
    (set! set-kounter (lambda (x) (set! N x)))
    (lambda (x y)
      (set! N (add1 N))
      (kons x y))))
(define (lots n)
  (if (zero? n)
      '()
      (kons 'egg (lots (sub1 n)))))

(define (lenkth l)
  (if (null? l)
      0
      (add1 (lenkth (kdr l)))))

(define (add-at-end l)
  (if (null? (kdr l))
      (konsC (kar l) (kons 'egg '()))
      (konsC (kar l) (add-at-end (kdr l)))))
(define add-at-end-too
  (lambda (l)
    (letrec 
        ([A (lambda (ls)
              (if (null? (kdr ls))
                  (set-kdr ls (kons 'egg '()))
                  (A (kdr ls))))])
      (A l)
      l)))
(define dozen (lots 12))
(define bakers-dozen (add-at-end dozen))
(define bakers-dozen-too (add-at-end-too dozen))
(define bakers-dozen-again (add-at-end dozen))
(define eklist?
  (lambda (ls1 ls2)
    (cond
      [(null? ls1) (null? ls2)]
      [(null? ls2) #f]
      [else 
       (and (eq? (kar ls1) (kar ls2))
            (eklist? (kdr ls1) (kdr ls2)))])))
(define same?
  (lambda (c1 c2)
    (let ([t1 (kdr c1)]
          [t2 (kdr c2)])
      (set-kdr c1 1)
      (set-kdr c2 2)
      (let ([v (= (kdr c1) (kdr c2))])
        (set-kdr c1 t1)
        (set-kdr c2 t2)
        v))))
(define last-kons
  (lambda (ls)
    (if (null? (kdr ls))
        ls
        (last-kons (kdr ls)))))
(define long (lots 12))

(define finite-lenkth
  (lambda (p)
    (let/cc infinite
      (letrec
          ([C (lambda (p q)
                (cond
                  [(same? p q) (infinite #f)]
                  [(null? q) 0]
                  [(null? (kdr q)) 1]
                  [else
                   (+ (C (sl p) (qk q)) 2)]))]
           [qk (lambda (x) (kdr (kdr x)))]
           [sl (lambda (x) (kdr x))])
        (cond
          [(null? p) 0]
          [else
           (add1 (C p (kdr p)))])))))

(define (mycons-v1 a d)
  (lambda (selector)
    (selector a d)))
(define (mycar-v1 l)
  (l 
   (lambda (a b) a)))
(define (mycdr-v1 l)
  (l 
   (lambda (a d) d)))

(define (myonecons a)
  (let
      ([d '()])
    (lambda (selector)
      (selector 
       (lambda(x) (set! d x))
       a d))))
(define (myset-cdr l new-d)
  (l 
   (lambda (set a d) (set new-d)))) 
(define (mycons a d)
  (let ([new-pair (myonecons a)])
    (myset-cdr new-pair d)
    new-pair))
(define (mycar l)
  (l 
   (lambda (set a b) a)))
(define (mycdr l)
  (l 
   (lambda (set a d) d)))
(define mytest-pair (mycons 'a 'd))
(define (myprint-pair p)
  (print (mycar p))
  (print (mycdr p)))
;question, how could I implements a function which will judge if a cons is mycons?

;chapter 19
(define (deep19 n)
  (if (zero? n)
      'pizza19
      (cons (deep19 (sub1 n)) '())))
(define toppings 0)
(define deepB
  (lambda (m)
    (cond
      [(zero? m)
       (let/cc jump
         (set! toppings jump)
         'pizzab)]
      [else (cons (deepB (sub1 m)) '())])))

(define deep&co
  (lambda (m k)
    (cond
      [(zero? m) (k 'pizzaco)]
      [else (deep&co (sub1 m)
                     (lambda (x) (k (cons x '()))))])))
(define deep&coB
  (lambda (m k)
    (cond
      [(zero? m) 
       (begin
         (print 'k)
         (set! toppings k)
         (k 'pizzacob))]
      [else (deep&coB (sub1 m)
                     (lambda (x) (k (cons x '()))))])))
(define two-in-a-row*?-v2
  (letrec
      ([W (lambda (a lat)
            (cond
              [(null? lat) #f]
              [else 
               (let ((nxt (car lat)))
                 (or (equal? nxt a)
                     (W nxt (cdr lat))))]))])
    (lambda (lat)
      (cond
        [(null? lat) #f]
        [else (W (car lat) (cdr lat))]))))
(define leave 0)
(define walk
  (lambda (l)
    (cond
      [(null? l) '()]
      [(atom? (car l)) (leave (car l))]
      [else     
       (walk (car l))
       (walk (cdr l))])))
(define start-it
  (lambda (l)
    (let/cc here
      (set! leave here)
      (walk l))))

(define fill 0)
(define waddle
  (lambda (l)
    (print l)
    (cond
      [(null? l) '()]
      [(atom? (car l))
       (let ()
         (let/cc rest
           (set! fill rest)
           (print 'before-leave)
           (leave (car l)))
         (print 'after-leave)
         (waddle (cdr l)))]
      [else (waddle (car l)) (waddle (cdr l))])))
(define start-it2
  (lambda (l)
    (let/cc here
      (set! leave here)
      (waddle l))))
(define get-next
  (lambda (x)
    (let/cc here-again
      (set! leave here-again)
      (fill 'go))))
(define get-first
  (lambda (l)
    (let/cc here
      (set! leave here)
      (waddle l)
      (leave '()))))
(define two-in-a-row*?
  (letrec
      ([T? (lambda (a)
             (let ([n (get-next 0)])
               (if (atom? n)
                   (or (eq? n a)
                       (T? n))
                   #f)))]
       [get-next
        (lambda (x)
          (let/cc here-again
            (set! leave here-again)
            (fill 'go)))]
       [fill (lambda (x) x)]
       [waddle
        (lambda (l)
          (cond
            [(null? l) '()]
            [(atom? (car l))
             (let/cc rest
               (set! fill rest)
               (leave (car l)))
             (waddle (car l))]
            [else
             (waddle (car l))
             (waddle (cdr l))]))]
       [leave (lambda (x) x)])
    (lambda (l)
      (let ([fst (let/cc here
                   (set! leave here)
                   (waddle l)
                   (leave '()))])
        (if (atom? fst)
            (T? fst)
            #f)))))
       