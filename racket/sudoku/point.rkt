(module point racket
  (provide gen-point get-names
           gen-points
           get-row-index get-col-index 
           get-ragion-index get-value
           add-value get-indexs 
           remove-point remove-points
           gen-point-index-with-value-list
           validate-points-duplicated)
  
  (define get-row-index first)
  (define get-col-index second)
  (define get-ragion-index third)
  (define get-value fourth)  
  
  (define ROW 'row)
  (define COL 'col)
  (define RAGION 'ragion)
  (define get-names (list ROW COL RAGION)) 
  
  (define (remove-point point points)
    (remove point points (lambda (x y) (equal? (take x 3) y))))
  (define (remove-points sub-points points)
    (foldl (lambda (item result)
             (remove-point item result))
           points sub-points))
  
  (define (gen-point row-index col-index [value '()])
    (if (null? value)
        (list row-index col-index 
              (compute-ragion-index row-index col-index))
        (list row-index col-index 
              (compute-ragion-index row-index col-index)
              value)))  
  (define (gen-points point values)
    (map (lambda (cur-value)
           (add-value point cur-value))
         values))
           
  (define (compute-ragion-index row-index col-index)
    (+ (* (quotient row-index 3) 3) (quotient col-index 3)))
  
  (define (add-value point value)
    (append point (cons value '())))
    
  (define (get-indexs point)
    (take point 3))
  
 
  (define (gen-point-index-with-value-list point)
    (foldl (lambda (index-name index-value result)
             (cons (list index-name index-value (get-value point)) 
                   result))
           '() get-names (get-indexs point)))
  
  (define (validate-points-duplicated points)
    (let/cc hop
      (let* ([showed-numbers (hash)])
        (foldl (lambda (point result)
               (let* ([value (get-value point)])
                 (foldl (lambda (index-name index-value inresult)
                        (let* ([key (list index-name index-value value)]
                               [pre-point (hash-ref inresult key 'no-point)])
                          (if (eq? pre-point 'no-point)
                              (hash-set inresult key point)
                              (hop (list pre-point point)))))
                      result get-names (get-indexs point))))
             showed-numbers points)
        #f)))
  (module+ main
      (printf "validate-points-duplicated ~s \n" (validate-points-duplicated (list '(0 6 1 5) '(1 5 1 4))))
    )
               
)