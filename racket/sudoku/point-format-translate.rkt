(module point-format-translate racket
  (provide point-list->point-hash
           point-hash->point-list)
  (require "point.rkt")
  (define (gen-point-key-list row-col-symbol)
    (map string->number
         (string-split
          (symbol->string row-col-symbol) "_")))
  (define (point-large? pre-point next-point)
    (if(= (get-row-index pre-point) (get-row-index next-point))
       (> (get-col-index pre-point) (get-col-index next-point))
       (> (get-row-index pre-point) (get-row-index next-point))))
  (define (point-hash->point-list point-hash)
    (sort (hash-map 
     point-hash 
     (lambda (key value)
       (let [(point-indexs (gen-point-key-list key))]
         (gen-point (first point-indexs)
                    (second point-indexs)
                    value)))) point-large?))

  

  (define (gen-point-key-symbol point)
    (string->symbol 
     (string-append (number->string (get-row-index point))
                    "_"
                    (number->string (get-col-index point)))))


  (define (point-list->point-hash point-list)
    (foldl (lambda (point result)
             (hash-set result 
                       (gen-point-key-symbol point)
                       (get-value point)))
           (hash) point-list))
  ;(gen-point-key-list '1_0)
  ;(point-hash->point-list mhash)
  
  (module+ main
    (let [(mhash #hasheq((0_0 . 5) (1_4 . 3) (8_8 . 6) (8_7 . 6)))
          (mlist '((8 7 8 0) (7 8 8 0)))]
      (printf "gen-point-key-list : ~s \n" 
              (gen-point-key-list '1_0))
      (printf "point-hash->point-list : ~s \n" 
              (point-hash->point-list mhash))
      (printf "gen-point-key-symbol : ~s \n" 
              (gen-point-key-symbol '(1 2 3 8)))
      (printf "point-list->point-hash : ~s \n"
              (point-list->point-hash mlist))))
  )