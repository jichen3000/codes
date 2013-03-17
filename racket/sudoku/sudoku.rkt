(module sudoku racket
  (provide answer-sudoku)

  (require "point.rkt")
  (require "list-helper.rkt")
  
  
  
  (define N 9)
  
  (define (gen-unknow-points1 known-points n)
    (remove-points known-points (reverse (two-map (lambda (row-index col-index)
           (gen-point row-index col-index))
         (range n) (range n)))))

  (define gen-unknow-points
    (lambda (known-points n)
      (letrec 
          ([check-end? 
            (lambda (point)
              (and (< (get-row-index point) 0) 
                   (= (get-col-index point) (sub1 n))))]
           [check-same-point? 
            (lambda (point other)
              (and (= (get-row-index point) (get-row-index other))
                   (= (get-col-index point) (get-col-index other))))]
           [U (lambda (cur-point points)
                (let ([next-point 
                       (if (= (get-col-index cur-point) 0)
                           (gen-point (sub1 (get-row-index cur-point)) 
                                      (sub1 n))
                           (gen-point (get-row-index cur-point) 
                                      (sub1 (get-col-index cur-point))))])
                  (cond
                    [(check-end? cur-point) '()]
                    [(null? points) 
                     (cons cur-point (U next-point points)) ]
                    [(check-same-point? (car points) cur-point)
                     (U next-point (cdr points))]
                    [else 
                     (cons cur-point (U next-point points))])))])
        (U (gen-point (sub1 n) (sub1 n)) known-points))))
  
  
  (define gen-known-points-from-sample
    (lambda (s n)
      (foldl (lambda (row-index row-s result) 
               (foldl (lambda (col-index s in-result)
                        (if (not (eq? s 0))
                            (cons 
                             (gen-point row-index col-index s)
                             in-result)
                            in-result))
                      result (range n) row-s)) 
             '() (range n) s)))
  
  
  (define (gen-unshow-numbers known-points n)
    (letrec 
        ([init-unshow-numbers
          (lambda ()
            (fold-two-layers 
             (lambda (name index result)
               (hash-set result (list name index) (range 1 (add1 n)))) 
             (hash) get-names (range n)))])
      (remove-numbers known-points (init-unshow-numbers))))
  
  (define (validate-right-square know-points)
    (let/cc hop
      (foldl (lambda (point result)
               (let ([point-index-with-value-list 
                      (gen-point-index-with-value-list point)])
                 (if (any-member point-index-with-value-list result)
                     (hop #t)
                     (append result point-index-with-value-list)))) 
             '() know-points)
      #f))
  
  (define (not-zero? v)
    (not (zero? v)))
  
  (define (get-intersect-values point unshow-numbers n)
    (foldl (lambda (name index result)
             (intersect-ordered-lists 
              result 
              (hash-ref unshow-numbers (list name index))))
           (range 1 (add1 n)) get-names point))
  
  (define (validate-exists-remove v lst)
    (if (member v lst)
        (remove v lst)
        (let () (pt "wrong" (list v lst) (remove v lst)))))
  
  (define (remove-number point unshow-numbers)
    ;(pt "before:" point)
    (foldl (lambda (name index result)             
             (hash-set result (list name index) 
                       (remove (get-value point)
                               (hash-ref unshow-numbers (list name index)))))
           unshow-numbers get-names (get-indexs point)))
  
  (define (remove-numbers points unshow-numbers)
    (foldl remove-number unshow-numbers points))
  
  (define (exclude-compute* unknow-points unshow-numbers n)
    (let* ([computed-points 
            (exclude-compute-once unknow-points unshow-numbers n)]
           [remain-unknow-points (remove-points computed-points unknow-points)]
           [remain-unshow-numbers (remove-numbers computed-points unshow-numbers)])
      (cond 
        [(null? computed-points) '()]
        [else (append computed-points 
                      (exclude-compute* 
                       remain-unknow-points remain-unshow-numbers n))])))
  
  (define (exclude-compute-once unknow-points unshow-numbers n)
    (foldl (lambda (cur-point result)             
             (let* ([values (get-intersect-values cur-point (remove-numbers result unshow-numbers) n)])
               (if (= (length values) 1)
                   (let* ([cur-valued-point (add-value cur-point (car values))])
                     (cons cur-valued-point result))
                   result)))
           '() unknow-points))
  
  ; compute
  ; refresh points
  ; validate points (it could be delete, due to never being used.)
  ; return false, if validate failed.
  ; return computed points, if all points have been computed.
  ; find a guess point
  ; do all guess point values
  ; return guess point plus computed points, if guess successed.
  ; return false, if cannot find any guess point.
  (define (answer known-points unknow-points unshow-numbers n)
    (let* ([computed-points 
            (exclude-compute* unknow-points unshow-numbers n)]
           [new-unknow-points (remove-points computed-points unknow-points)]
           [new-unshow-numbers (remove-numbers computed-points unshow-numbers)]
           [I (lambda (guess-point)
                (let ([answer-result (answer known-points
                                      (remove-point guess-point new-unknow-points)
                                      (remove-number guess-point new-unshow-numbers)
                                      n)])
                  (if answer-result
                      (append computed-points (cons guess-point answer-result))
                      #f)))])
      (cond
        ; no need to validate here, it could not be wrong.
        ;[(validate-right-square (append computed-points known-points)) #f]
        [(null? new-unknow-points) computed-points]
        ; this is the real point which will return false. (ormap fn '()) = false
        ; when you choose a point, and its possible values is null, 
        ; which means last time guess point is wrong
        [else (ormap I (choose-guess-point-values new-unknow-points new-unshow-numbers n))])))
         
  
  (define (choose-guess-point-values unknow-points unshow-numbers n)
    (let* ([choosed-point (argmin (lambda (cur-point)
                                    (length (get-intersect-values cur-point unshow-numbers n))) 
                                  unknow-points)])
      (gen-points choosed-point 
                  (get-intersect-values choosed-point unshow-numbers n))))
  
  (define (print-title-msg-return-null title msg [return-value #f])
    (printf "~s : ~s \n" title msg)
    return-value)
  (define pt print-title-msg-return-null)
  

  
  (define (answer-sudoku known-points)
    (answer (gen-unknow-points known-points N) 
            (gen-unshow-numbers known-points N) N))
    
  (define (answer-sudoku-test square)
    (let* ([known-points (gen-known-points-from-sample square N)]
           [unknow-points (gen-unknow-points known-points N)]
           [unshow-numbers (gen-unshow-numbers known-points N)]
           [start-time (current-inexact-milliseconds)]
           [computed-points (answer known-points unknow-points unshow-numbers N)]
           [time-seconds (/ (- (current-inexact-milliseconds) start-time) 1000)]
           ;[computed-points (exclude-compute* unknow-points unshow-numbers N)]
           )
      (printf "known-points: ~s \n" known-points)
      (printf "unknow-points: ~s \n"  unknow-points)
      (printf "length unknow-points: ~s \n"  (length unknow-points))
      (printf "unshow-numbers: ~s \n" unshow-numbers)
      ;(printf "get-intersect-values ~s \n" (get-intersect-values '(8 4 7) #hash(((row 8) . (1 2 3 6 7 8 9)) ((col 4) . (1 2 4 5 7 9)) ((ragion 7) . (6 8 9))) N))
      (pt "time(seconds): " time-seconds)
      (printf "validate-right-square ~s \n" (validate-right-square (append computed-points known-points)))
      (printf "validate-points-duplicated ~s \n" (validate-points-duplicated (append computed-points known-points)))
      
      (printf "length computed-points: ~s \n" (length computed-points))
      (printf "computed-points: ~s \n" computed-points)      
      (display 'ok)))

  (module+ main
    (let [(excludable-sample 
           '((0 0 0 3 0 5 0 0 0)
             (0 0 2 0 9 0 3 0 0)
             (3 0 0 0 7 0 0 0 1)
             (5 0 0 0 1 0 0 0 9)
             (0 0 6 0 8 0 5 0 0)
             (0 0 0 5 0 2 0 0 0)
             (7 0 8 1 4 9 6 0 3)
             (0 9 0 0 0 0 0 2 0)
             (4 0 3 6 2 7 9 0 8)))
          (media-sample 
           '((0 0 0 0 9 8 0 2 0)
             (0 0 0 2 0 0 1 0 4)
             (0 0 0 0 0 6 5 0 0)
             (6 0 0 0 4 0 0 9 0)
             (0 0 0 8 0 3 6 0 0)
             (4 0 0 0 0 0 0 0 0)
             (7 0 9 3 2 0 0 0 5)
             (0 0 1 0 0 7 0 0 0)
             (0 2 0 0 0 0 7 0 0)))
          (complex-sample 
           '((9 0 0 0 0 0 0 0 5)
             (0 4 0 3 0 0 0 2 0)
             (0 0 8 0 0 0 1 0 0)
             (0 7 0 6 0 3 0 0 0)
             (0 0 0 0 8 0 0 0 0)
             (0 0 0 7 0 9 0 6 0)
             (0 0 1 0 0 0 9 0 0)
             (0 3 0 0 0 6 0 4 0)
             (5 0 0 0 0 0 0 0 8)))]
      (answer-sudoku-test media-sample)))
)