#lang racket
(require web-server/http
         web-server/managers/none
         web-server/servlet
         web-server/servlet-env
         web-server/templates
         mzlib/etc
         json)

(require "point-format-translate.rkt"
         "sudoku.rkt")



(define-values (sudoku-dispatch blog-url)
    (dispatch-rules
     [("") sudoku-main]
     [("sudoku" "sudokuresult") sudoku-result]
     ))

(define (sudoku-main req)
  (response/full
   200 #"Okay"
   (current-seconds) TEXT/HTML-MIME-TYPE
   empty
   (list (string->bytes/utf-8 
          (include-template "views/main.rhtml")))))

(define (perform-sudoku req)
  (let* [(receive-points (extract-binding/single 
                           (string->symbol "fix_values")
                           (request-bindings req)))
         (known-points (point-hash->point-list 
                        (string->jsexpr receive-points)))
         (computed-points (answer-sudoku known-points))
         ]
    (printf "receive-points : ~s \n" receive-points)
    (printf "known-points : ~s \n" known-points)
    (printf "computed-points : ~s \n" computed-points)
    (if computed-points
        (jsexpr->string (point-list->point-hash computed-points))
        (jsexpr->string #f))))
                        

(define (sudoku-result req)
  (response/xexpr 
   (perform-sudoku req)))


(define (start request)
  (sudoku-dispatch request))


;http://planet.plt-scheme.org/package-source/ryanc/scriblogify.plt/1/0/
;(printf "dir: ~s \n" (build-path (this-expression-source-directory) "public")) 
(serve/servlet start
               #:launch-browser? #t
               #:servlet-path "" 
               #:servlet-regexp #rx""
               #:stateless? #t
               #:quit? #f
               #:banner? #f
               #:listen-ip #f
               #:port 9999
               #:extra-files-paths
               (list (build-path (this-expression-source-directory) "public")))