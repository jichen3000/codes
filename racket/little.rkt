#lang racket
(define (atom? x)
  (and (not (pair? x)) (not (null? x))))

(define (lat? l)
  (cond
    [(null? l) #t]
    [(atom? (car l)) (lat? (cdr l))]
    [else #f]))

(define (member? m l)
  (cond
    [(null? l) #f]
    [else (or (eq? (car l) m) (member? m (cdr l)))]))

(define (remove-member m l)
  (cond
    [(null? l) l]
    [(eq? m (car l)) (cdr l)]
    [else (cons (car l) (remove-member m (cdr l)))]))

(define (multi-remove-member m l)
  (cond
    [(null? l) l]
    [(eq? m (car l)) (multi-remove-member m (cdr l))]
    [else (cons (car l) (multi-remove-member m (cdr l)))]))

(define (firsts l)
  (cond
    [(null? l) l]
    [else (cons (caar l) (firsts (cdr l)))]))

(define (seconds l)
  (cond
    [(null? l) l]
    [else (cons (cadar l) (seconds (cdr l)))]))

(define (insert-after insert-m hook-m l)
  (cond
    [(null? l) '()]
    [(eq? hook-m (car l)) 
     (cons hook-m (cons insert-m (cdr l)))]
    [else (cons (car l) (insert-after insert-m hook-m (cdr l)))]))
(define (insert-before insert-m hook-m l)
  (cond
    [(null? l) '()]
    [(eq? hook-m (car l)) 
     (cons insert-m (cons hook-m (cdr l)))]
    [else (cons (car l) (insert-before insert-m hook-m (cdr l)))]))

(define (multi-insert-after insert-m hook-m l)
  (cond
    [(null? l) '()]
    [(eq? hook-m (car l)) 
     (cons 
      hook-m 
      (cons insert-m (multi-insert-after insert-m hook-m (cdr l))))]
    [else (cons (car l) (multi-insert-after insert-m hook-m (cdr l)))]))

(define (substitute new old l)
  (cond
    [(null? l) '()]
    [(eq? old (car l)) (cons new (cdr l))]
    [else (cons (car l) (substitute new old (cdr l)))]))

(define (multi-substitute new old l)
  (cond
    [(null? l) '()]
    [(eq? old (car l)) (cons new (multi-substitute new old (cdr l)))]
    [else (cons (car l) (multi-substitute new old (cdr l)))]))

(define (multi-substitute2 new old1 old2 l)
  (cond
    [(null? l) '()]
    [(or (eq? old1 (car l)) (eq? old2 (car l))) 
     (cons new (multi-substitute2 new old1 old2 (cdr l)))]
    [else (cons (car l) (multi-substitute2 new old1 old2 (cdr l)))]))

;It is a bad method as m cannot be the negative.
(define (new+ n m)
  (cond
    [(zero? m) n]
    [else (add1 (new+ n (sub1 m)))]))

(define (new- n m)
  (cond
    [(zero? m) n]
    [else (sub1 (new- n (sub1 m)))]))

(define (addtup tup)
  (cond
    [(null? tup) 0]
    [else (new+ (car tup) (addtup (cdr tup)))]))

(define (new* n m)
  (cond
   [(zero? m) 0]
   [else (new+ n (new* (sub1 m) n))])) 

(define (tup+ tup1 tup2)
  (cond 
    [(null? tup1) tup2]
    [(null? tup2) tup1]
    [else (cons (new+ (car tup1) (car tup2))
                (tup+ (cdr tup1) (cdr tup2)))]))

(define (new> n m)
  (cond
    [(zero? n) #f]
    [(zero? m) #t]
    [else (new> (sub1 n) (sub1 m))]))

(define (new< n m)
  (cond
    [(zero? m) #f]
    [(zero? n) #t]
    [else (new< (sub1 n) (sub1 m))]))


(define (new= n m)
  (cond
    [(and (zero? m) (zero? n))]
    [(zero? m) #f]
    [(zero? n) #f]
    [else (new= (sub1 n) (sub1 m))]))

(define (new-power n m)
  (cond
    [(zero? m) 1]
    [else (new* n (new-power n (sub1 m)))]))

(define (new/ n m)
  (cond 
    [(new< n m) 0]
    [else (add1 (new/ (new- n m) m))]))

(define (new-length lat)
  (cond
    [(null? lat) 0]
    [else (add1 (new-length (cdr lat)))]))

(define (pick n lat)
  (cond
    [(new> n (new-length lat)) '()]
    [(zero? (sub1 n)) (car lat)]
    [else (pick (sub1 n) (cdr lat))]))


(define (remove-pick n lat)
  (cond
    [(new> n (new-length lat)) lat]
    [(zero? (sub1 n)) (cdr lat)]
    [else (cons (car lat) (remove-pick (sub1 n) (cdr lat)))]))

(define (remove-number lat)
  (cond 
    [(null? lat) '()]
    [(number? (car lat)) (remove-number (cdr lat))]
    [else (cons (car lat) (remove-number (cdr lat)))]))

(define (select-nums lat)
  (cond
    [(null? lat) '()]
    [(number? (car lat)) (cons (car lat) (select-nums (cdr lat)))]
    [else (select-nums (cdr lat))]))

(define (occur a lat)
  (cond
    [(null? lat) 0]
    [(eq? a (car lat)) (add1 (occur a (cdr lat)))]
    [else (occur a (cdr lat))]))

(define (exclude n lat)
  (cond 
    [(null? lat) '()]
    [(new< n 1) lat]
    [(= n 1) (cdr lat)]
    [else (cons (car lat) (exclude (sub1 n) (cdr lat)))]))

(define (remove-member* m l)
  (cond 
    [(null? l) '()]
    [(eq? m (car l)) (remove-member* m (cdr l))] 
    [(pair? (car l)) (cons (remove-member* m (car l)) (remove-member* m (cdr l)))]
    [else (cons (car l) (remove-member* m (cdr l)))]))
;it's different when you enter (remove-member2* 'a 'b)
(define (remove-member2* m l)
  (cond 
    [(null? l) '()]
    [(-> not pair? l) l]
    [(eq? m (car l)) (remove-member* m (cdr l))]
    [else (cons (remove-member* m (car l)) (remove-member* m (cdr l)))]))

(define (insert-before* new-m hook l)
  (cond
    [(null? l) '()]
    [(eq? hook (car l)) (cons new-m (cons hook (insert-before* new-m hook (cdr l))))]
    [(pair? (car l))
     (cons (insert-before* new-m hook (car l)) (insert-before* new-m hook (cdr l)))]
    [else (cons (car l) (insert-before* new-m hook (cdr l)))]))

(define (insert-after* new-m hook l)
  (cond 
    [(null? l) '()]
    [(eq? hook (car l)) (cons hook (cons new-m (insert-after* new-m hook (cdr l))))]
    [(pair? (car l))
     (cons (insert-after* new-m hook (car l)) (insert-after* new-m hook (cdr l)))]
    [else (cons (car l) (insert-after* new-m hook (cdr l)))]))

(define (occur* a l)
  (cond
    [(null? l) 0]
    [(eq? a (car l)) (add1 (occur* a (cdr l)))]
    [(pair? (car l))
     (+ (occur* a (car l)) (occur* a (cdr l)))]
    [else (occur* a (cdr l))]))

(define (substitute* new old l)
   (cond 
     [(null? l) '()]
     [(eq? old (car l)) (cons new (substitute* new old (cdr l)))]
     [(pair? (car l))
      (cons (substitute* new old (car l)) (substitute* new old (cdr l)))]
     [else  (cons (car l) (substitute* new old (cdr l)))]))

(define (member* a l)
  (cond
    [(null? l) '()]
    [(eq? a (car l)) #t]
    [(pair? (car l))
     (or (member* a (car l)) (member* a (cdr l)))]
    [else (member* a (cdr l))]))

(define (leftmost l)
  (cond 
    [(null? l) '()]
    [(pair? (car l)) (leftmost (car l))]
    [else (car l)]))

(define (numbered? l)
  (cond
    [(null? l) #f]
    [(atom? l) (number? l)]
    [(and (numbered? (car l))
          (or (eq? (cadr l) '+)
              (eq? (cadr l) '*)))
     (numbered? (caddr l))]
    [else #f]))
 
(define (arith-value l)
  (cond
    [(number? l) l]
    [(null? (cdr l)) (arith-value (car l))]
    [(eq? (cadr l) '+) (+ (arith-value (car l)) (arith-value (cddr l)))]
    [(eq? (cadr l) '*) (* (arith-value (car l)) (arith-value (cddr l)))]))

(define (value l)
  (cond
    [(number? l) l]
    ;[(null? (cdr l)) (value (car l))]
    [(eq? (car l) '+) (+ (value (cadr l)) (value (caddr l)))]
    [(eq? (car l) '*) (* (value (cadr l)) (value (caddr l)))]))


;chapter 7
(define (set? lat)
  (cond
    [(null? lat) #t]
    [(member? (car lat) (cdr lat)) #f]
    [else (set? (cdr lat))])) 

(define (make-set lat)
  (cond
    [(null? lat) '()]
    [(cons (car lat) (make-set (multi-remove-member (car lat) (cdr lat))))]))
    
(define (subset? sub-set all-set)
  (cond
    [(null? sub-set) #t]
    [(member? (car sub-set) all-set) (subset? (cdr sub-set) all-set)]
    [else #f]))

(define (intersect set1 set2)
  (cond
    [(or (null? set1) (null? set2)) '()]
    [(member? (car set1) set2) (cons (car set1) (intersect (cdr set1) set2))]
    [else (intersect (cdr set1) set2)]))

(define (union set1 set2)
  (cond
    [(null? set1) set2]
    [else (cons (car set1) (union (cdr set1) (remove-member (car set1) set2)))]))

(define (intersectall l-set)
  (cond
    [(null? (cdr l-set)) (car l-set)]
    [else (intersect (car l-set) (intersectall (cdr l-set)))]))

(define (a-pair? lat)
  (cond
    [(or (atom? lat) (null? lat) (null? (cdr lat))) #f]
    [(null? (cddr lat)) #t]
    [else #f]))

(define (first lat)
  (car lat))

(define (second lat)
  (cadr lat))

(define (third lat)
  (caddr lat))

(define (fourth lat)
  (cadddr lat))

;relation is a set of pair.

(define (fun? rel)
  (set? (firsts rel)))

(define (reverse-pair pair)
  (list (second pair) (first pair)))

(define (reverse-rel rel)
  (cond
    [(null? rel) '()]
    [else (cons (reverse-pair (car rel)) (reverse-rel (cdr rel)))]))

(define (fullfun? rel)
  (and (set? (firsts rel)) (set? (seconds rel))))

(define (eq?-c a)
  (lambda (x)
    (eq? x a)))
;chapter 8
(define (remove-member-fn fn)
  (lambda (a lat)
    (cond 
      [(null? lat) '()]
      [(fn a (car lat)) ((remove-member-fn fn) a (cdr lat))]
      [(cons (car lat) ((remove-member-fn fn) a (cdr lat)))])))

(define (insert-after-fn test-fn?)
  (lambda (insert-m hook-m l)
    (cond
      [(null? l) '()]
      [(test-fn? hook-m (car l)) 
       (cons hook-m (cons insert-m (cdr l)))]
      [else (cons (car l) 
                  ((insert-after-fn test-fn?) 
                   insert-m hook-m (cdr l)))])))
(define (insert-before-fn test-fn?)
  (lambda (insert-m hook-m l)
    (cond
      [(null? l) '()]
      [(eq? hook-m (car l)) 
       (cons insert-m (cons hook-m (cdr l)))]
      [else (cons (car l) 
                ((insert-before-fn test-fn?) 
                 insert-m hook-m (cdr l)))])))

(define (insert-testfn-buildfn build-fn)
  (lambda (test-fn?)
    (lambda (insert-m hook-m l)
      (cond
        [(null? l) '()]
        [(eq? hook-m (car l))
         (build-fn insert-m hook-m (cdr l))]
        [else (cons (car l) 
                    (((insert-testfn-buildfn 
                     build-fn) test-fn?) insert-m hook-m (cdr l)))]))))
(define (build-left insert-m hook-m cdr-l)
  (cons insert-m (cons hook-m cdr-l)))
(define (insertL insert-m hook-m l)
    (((insert-testfn-buildfn build-left) eq?) insert-m hook-m l))

(define (insert-testfn-buildfn2 build-fn test-fn? insert-m hook-m l)
  (cond
    [(null? l) '()]
    [(eq? hook-m (car l))
         (build-fn insert-m hook-m (cdr l))]
    [else (cons (car l) 
                    (insert-testfn-buildfn2 
                     build-fn test-fn? insert-m hook-m (cdr l)))]))
(define (insertL2 insert-m hook-m l)
   (insert-testfn-buildfn2 build-left eq? insert-m hook-m l))

(define (value-s l)
  (cond
    [(number? l) l]
    ;[(null? (cdr l)) (value (car l))]
    [else (atom-to-fn 
           (operator l)
           (value-s (cadr l)) (value-s (caddr l)))]))
(define (operator l)
  (print 'todo))
(define (atom-to-fn op v1 v2)
  (print 'todo))

(define (multi-remove-member-fn test-fn?)
  (lambda (m l)
    (cond
      [(null? l) l]
      [(test-fn? m (car l)) ((multi-remove-member-fn test-fn?) m (cdr l))]
      [else (cons (car l) ((multi-remove-member-fn test-fn?) m (cdr l)))])))

(define (multi-remove-member-co a lat col)
  (cond
    [(null? lat) (col '() '())]
    [(eq? (car lat) a)
     (multi-remove-member-co a (cdr lat)
                             (lambda (newlat seen)
                               (col newlat
                                    (cons (car lat) seen))))]
    [else (multi-remove-member-co a (cdr lat)
                                  (lambda (newlat seen)
                                    (col (cons (car lat) newlat) seen)))]))
(define (a-friend x y)
  (null? y))
;(define col a-friend)
;(define lats '(a b c d))
;(define (col-eq-1 newlat seen)
;  (col newlat (cons (first lats) seen)))
;(define (col-neq-1 newlat seen)
;  (col (cons (first lats) newlat) seen))
;
;(define (col-neq-2 newlat seen)
;  (col-neq-1 (cons (second lats) newlat) seen))
;(define (col-neq-2s newlat seen)
;  (col (cons (car lats) (cons (second lats) newlat)) seen))
;
;(define (col-neq-2-eq-3 newlat seen)
;  (col-neq-2s newlat (cons (third lats) seen)))
;(define (col-neq-2-eq-3s newlat seen)
;  (col (cons (first lats) (cons (second lats) newlat)) 
;       (cons (third lats) seen)))
;(define (col-neq-2-eq-3-neq-4s newlat seen)
;  (col (cons (first lats) (cons (second lats) (cons (fourth lats) newlat))) 
;       (cons (third lats) seen)))

(define (new-istuna newlat seen)
  (length newlat))

(define (multi-insert-LR m hook-L hook-R lat)
  (cond
    [(null? lat) '()]
    [(eq? (car lat) hook-L)
     (cons m (cons hook-L 
                   (multi-insert-LR m hook-L hook-R (cdr lat))))]
    [(eq? (car lat) hook-R)
     (cons hook-R (cons m 
                   (multi-insert-LR m hook-L hook-R (cdr lat))))]
    [else (cons (car lat) 
                (multi-insert-LR m hook-L hook-R (cdr lat)))]))

(define (multi-insert-LR&co m hook-L hook-R lat col)
  (cond
    [(null? lat) (col '() 0 0)]
    [(eq? (car lat) hook-L)
     (multi-insert-LR&co m hook-L hook-R (cdr lat)
                         (lambda(newlat countL countR)
                           (col (cons m (cons hook-L newlat))
                                (add1 countL) countR)))]
    [(eq? (car lat) hook-R)
     (multi-insert-LR&co m hook-L hook-R (cdr lat)
                         (lambda(newlat countL countR)
                           (col (cons hook-R (cons m newlat))
                                countL (add1 countR))))]
    [else
     (multi-insert-LR&co m hook-L hook-R (cdr lat)
                         (lambda(newlat countL countR)
                           (col (cons m  newlat)
                                countL countR)))]))
                                                               
(define (evens-only* l)
  (cond
    [(null? l) '()]
    [(pair? (car l)) (cons (evens-only* (car l)) (evens-only* (cdr l)))]
    [(and (number? (car l)) (even? (car l))) 
     (cons (car l) (evens-only* (cdr l)))]
    [else (evens-only* (cdr l))]))

(define (evens-only*&co l col)
  (cond
    [(null? l) (col '() '())]
    [(pair? (car l)) 
     (evens-only*&co (car l) 
                    (lambda (car-even-l car-odd-l)
                      (evens-only*&co 
                       (cdr l)
                       (lambda (cdr-even-l cdr-odd-l)
                         (col (cons car-even-l cdr-even-l) 
                              (cons car-odd-l cdr-odd-l))))))]
    [(even? (car l))
     (evens-only*&co (cdr l) 
                    (lambda (even-l odd-l)
                      (col (cons (car l) even-l) odd-l)))]
    [else (evens-only*&co (cdr l) 
                         (lambda (even-l odd-l)
                           (col even-l (cons (car l) odd-l))))]))

;(evens-only*&co '(2 (4 9) 7 6) 
;                  (lambda (even-l odd-l)
;                    (print 'colin)(print even-l)(print odd-l)))

;chapter 9
(define (looking a lat)
  (keep-looking a (pick 1 lat) lat))
(define (keep-looking a sorn lat)
  (cond 
    [(number? sorn)
     (keep-looking a (pick sorn lat) lat)]
    [else (eq? sorn a)]))

(define (shift l)
  (list (first (first l))
        (list (second (first l)) (second l))))
(define (weight*  pora)
  (cond
    [(atom? pora) 1]
    [else (+ (* (weight* (first pora)) 2)
             (weight* (second pora)))]))
(define (align pora)
  (cond
    [(atom? pora) pora]
    [(pair? (first pora)) (align (shift pora))]
    [else (list (first pora) (align (second pora)))]))

(define shuffle 
  (lambda  (pora) 
    (cond 
      ( ( atom? pora) pora) 
      ( ( a-pair? (first pora)) 
        ( shuffle ( reverse-pair pora))) 
      (else  ( list  (first pora) 
                     ( shuffle ( second pora))))))) 


(define (will-stop? fn)
  (#f))
(define (eternity x)
  (eternity x))
(define (last-try x)
  (and (will-stop? last-try)
       (eternity x)))

(define (collatz-conjecture n)
  (cond
    [(= 1 n) 1]
    [(even? n)(collatz-conjecture (/ n 2))]
    [else (collatz-conjecture (add1 (* 3 n)))]))

(define (ackermann-function m n)
  (cond
    [(= m 0) (+ n 1)]
    [(and (= n 0) (> m 0)) (ackermann-function (- m 1) 1)]
    [(and (> n 0) (> m 0)) (ackermann-function 
                            (- m 1) (ackermann-function m (- n 1)))]))

(define length0
  (lambda (l)
    (cond
      [(null? l) 0]
      [else (add1 (eternity (cdr l)))])))
(define length0-lambda
  ((lambda (length-fn)
     (lambda (l)
       (cond
         [(null? l) 0]
         [else (add1 (length-fn (cdr l)))])))
   eternity))
(define length0-mk
  ((lambda (mk-length)
     (mk-length eternity))
     (lambda (length-fn)
       (lambda (l)
         (cond
           [(null? l) 0]
           [else (add1 (length-fn (cdr l)))])))
     ))
(define length0-mks
  ((lambda (mk-length)
     (mk-length mk-length))
     (lambda (mk-length)
       (lambda (l)
         (cond
           [(null? l) 0]
           [else (add1 (mk-length (cdr l)))])))
     ))
(define length1-mks
  ((lambda (mk-length)
     (mk-length mk-length))
     (lambda (mk-length)
       (lambda (l)
         (cond
           [(null? l) 0]
           [else (add1 ((mk-length mk-length) (cdr l)))])))
     ))

(define length1-mks2
  ((lambda (mk-length)
     (mk-length mk-length))
     (lambda (mk-length)
       ((lambda (length)
         (lambda (l)
           (cond
             [(null? l) 0]
             [else (add1 (length (cdr l)))])))
        (lambda (x)
          ((mk-length mk-length) x))))
     ))
(define length1-mks3
  ((lambda (le)
     ((lambda (mk-length)
        (mk-length mk-length))
      (lambda (mk-length)
        (le
         (lambda (x)
           ((mk-length mk-length) x))))
      ))
   (lambda (length)
     (lambda (l)
       (cond
         [(null? l) 0]
         [else (add1 (length (cdr l)))])))))
(define f
  (lambda (x)
    (f x)))
(define length1-mk
  ((lambda (mk-length)
     (mk-length 
      (mk-length eternity)))
     (lambda (length-fn)
       (lambda (l)
         (cond
           [(null? l) 0]
           [else (add1 (length-fn (cdr l)))])))
     ))
(define length2-mk
  ((lambda (mk-length)
     (mk-length 
      (mk-length 
       (mk-length eternity))))
     (lambda (length-fn)
       (lambda (l)
         (cond
           [(null? l) 0]
           [else (add1 (length-fn (cdr l)))])))
     ))
(define length1-lambda
  ((lambda (length-fn)
     (lambda (l)
       (cond
         [(null? l) 0]
         [else (add1 (length-fn (cdr l)))])))
   ((lambda (length-fn)
     (lambda (l)
       (cond
         [(null? l) 0]
         [else (add1 (length-fn (cdr l)))])))
   eternity)))
(define length2-lambda
  ((lambda (length-fn)
     (lambda (l)
       (cond
         [(null? l) 0]
         [else (add1 (length-fn (cdr l)))])))
   ((lambda (length-fn)
     (lambda (l)
       (cond
         [(null? l) 0]
         [else (add1 (length-fn (cdr l)))])))
   ((lambda (length-fn)
     (lambda (l)
       (cond
         [(null? l) 0]
         [else (add1 (length-fn (cdr l)))])))
   eternity))))


(define (length1d l)
  (cond
    [(null? l) 0]
    [else (add1 (length0 (cdr l)))]))
(define (length1 l)
  (cond
    [(null? l) 0]
    [else (add1 ((lambda (l)
                   (cond
                     [(null? l) 0]
                     [else (add1 (eternity (cdr l)))]))
                 (cdr l)))]))

(define (length2d l)
  (cond
    [(null? l) 0]
    [else (add1 (length1 (cdr l)))]))
(define length2
  (lambda (l)
    (cond
      [(null? l) 0]
      [else (add1 ((lambda (l)
                     (cond
                       [(null? l) 0]
                       [else (add1 ((lambda (l)
                                      (cond
                                        [(null? l) 0]
                                        [else (add1 (eternity (cdr l)))]))
                                    (cdr l)))])) 
                  (cdr l)))])))

;chapter 10
(define (I x)
  x)
(define lookup-in-entry
  (lambda (name entry default-f)
    (lookup-in-entry-help 
     name
     (first entry)
     (second entry)
     default-f)))
(define lookup-in-entry-help
  (lambda (name names values default-f)
    (cond
      [(null? names) (default-f name)]
      [(eq? name (car names)) (car values)]
      [else (lookup-in-entry-help
             name (cdr names) (cdr values) default-f)])))
(define lookup-in-table
  (lambda (name table default-f)
    (cond
      [(null? table) (default-f name)]
      [else (lookup-in-entry
             name 
             (car table) 
             (lambda (name)
               (lookup-in-table 
                name
                (cdr table)
                default-f))
             )])))

(define *const
  (lambda (e table)
    (cond
      [(number? e) e]
      [(eq? e #t) #t]
      [(eq? e #f) #f]
      [else (list (quote primitive) e)])))
(define initial-table
  (lambda (name)
    (car '())))
(define *identifier
  (lambda (e table)
    (lookup-in-table e table initial-table)))
(define *quote
  (lambda (e table)
    (second e)))
(define table-of first)
(define formals-of second)
(define body-of third)
(define *lambda 
  (lambda (e table)
    (list 'non-primitive 
          (cons table (cdr e)))))
(define else?
  (lambda (x)
    [cond
      [(atom? x) (eq? x 'else)]
      [else #f]]))
(define question-of first)
(define answer-of second)
(define evcon
  (lambda (lines table)
    (cond
      [(else? (question-of (car lines))) 
       (meaning (question-of (car lines)) table)]
      [(meaning (question-of (car lines)) table)
       (meaning (answer-of (car lines)) table)]
      [else (evcon (cdr lines) table)])))
(define cond-lines-of cdr)
(define *cond 
  (lambda (e table)
    (evcon (cond-lines-of e) table)))
(define evlis
  (lambda (args table)
    (cond
      [(null? args) '()]
      [else 
       (cons (meaning (car args) table)
             (evlis (cdr args) table))])))
(define function-of car)
(define arguments-of cdr)
(define (primitive? l)
  (eq? (first l) 'primitive))
(define (non-primitive? l)
  (eq? (first l) 'non-primitive))
(define :atom?
  (lambda (x) 
    (cond
      ((atom? x) #t)
      ((null? x) #f)
      ((eq? (car x) (quote primitive)) #t)
      ((eq? (car x) (quote non-primitive)) #t)
      (else #f))))
(define apply-primitive 
  (lambda (name vals)
    (cond
      ((eq? name 'cons)
       (cons (first vals) (second vals))) 
      ((eq? name (quote car))
       (car (first vals)))
      ((eq? name (quote cdr))
       (cdr (first vals))) 
      ((eq? name (quote null?))
       (null? (first vals))) 
      ((eq? name (quote eq?))
       (eq? (first vals) (second vals)))
      ((eq? name (quote atom?))
       (:atom? (first vals))) 
      ((eq? name (quote zero?))
       (zero? (first vals)))
      ((eq? name (quote add1))
       (add1 (first vals)))
      ((eq? name (quote sub1))
       (sub1 (first vals)))
      ((eq? name (quote number?))
       (number? (first vals))))))
(define extend-table cons)
(define new-entry list)
(define apply-closure 
  (lambda (closure vals)
    (meaning (body-of closure) 
             (extend-table
              (new-entry (formals-of closure) vals )
              (table-of closure)))))
(define (napply fun vals)
  (cond
    [(primitive? fun)
     (apply-primitive
      (second fun) vals)]
    [(non-primitive? fun)
     (apply-closure
      (second fun) vals)]))

(define *application 
  (lambda (e table)
    (napply
     (meaning (function-of e) table)
     (evlis (arguments-of e) table))))
(define list-to-action 
  (lambda (e) 
    (cond
      [(atom? (car e))
       (cond
         [(eq? (car e) (quote quote)) *quote]
         [(eq? (car e) (quote lambda)) *lambda]
         [(eq? (car e) (quote cond)) *cond]
         [else *application])]
      [else *application])))
(define atom-to-action
  (lambda (e)
    (cond
      [(number? e) *const]
      [(eq? e #t) *const]
      [(eq? e #f) *const]
      [(eq? e (quote cons)) *const]
      [(eq? e (quote car)) *const]
      [(eq? e (quote cdr)) *const]
      [(eq? e (quote null?)) *const]
      [(eq? e (quote eq?)) *const]
      [(eq? e (quote atom?)) *const]
      [(eq? e (quote zero?)) *const]
      [(eq? e (quote add1)) *const]
      [(eq? e (quote sub1)) *const]
      [(eq? e (quote number?)) *const]
      [else *identifier]))) 
(define expression-to-action
  (lambda (e)
    (cond
      [(atom? e) (atom-to-action e)]
      [else (list-to-action e)])))

(define meaning
  (lambda (e table)
    ((expression-to-action e) e table)))

; This function equals the eval
(define nvalue
  (lambda (e)
    (meaning e (quote ()))))

(define (curry fun . args)
  (lambda x
    (apply fun (append args x))))
(define double (curry * 2))

(define (-> . args)
  (cond 
    [(null? args) '()]
    [(= (length args) 1) args]
    [(= (length args) 2) ((car args) (cadr args))]
    [else ((car args) (apply -> (cdr args)))]))