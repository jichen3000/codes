(module list-helper racket
  (provide intersect-ordered-lists
           fold-two-layers
           any-member two-map)
  
  (define (intersect-ordered-lists lat1 lat2)
    (if
     (or (null? lat1) (null? lat2)) 
     '()
     (let ([car1 (car lat1)]
           [car2 (car lat2)])
       (cond
         [(=  car1 car2) 
          (cons car1 
                (intersect-ordered-lists (cdr lat1) (cdr lat2)))]
         [(< car1 car2)
          (intersect-ordered-lists (cdr lat1) lat2)]
         [(> car1 car2)
          (intersect-ordered-lists lat1 (cdr lat2))]))))  

  (define (fold-two-layers fn init-value outer-l inner-l)
    (foldl (lambda (outer-v outer-result)
             (foldl (lambda (inner-v inner-result)
                      (fn outer-v inner-v inner-result)
                      ) outer-result inner-l)
             ) init-value outer-l)) 
  (define (any-member lst full-l  
st)
    (ormap (lambda (v)
              (member v full-lst))
            lst))
  
  (define (two-map1 fn lst1 lst2)
    (append-map append (map (lambda (x)
           (map (lambda (y)
                  (fn x y))
                lst2)
           ) lst1)))
  
  (define (two-map fn lst1 lst2)
    (for*/list ([i lst1]
                 [j lst2])
       (fn i j)))
  (module+ main
    (two-map (lambda (row-index col-index)
           (list row-index col-index))
         (range 9) (range 9)))
           

)