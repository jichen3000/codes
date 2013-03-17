#lang racket
(require web-server/http
         web-server/managers/none
         web-server/servlet
         web-server/servlet-env
         web-server/templates
         mzlib/etc
         json)

(define-values (understanding-dispatch blog-url)
    (dispatch-rules
     [("") main]
     [("status") #:method "post" post-status]
     ))

(define (main req)
  (response/full
   200 #"Okay"
   (current-seconds) TEXT/HTML-MIME-TYPE
   empty
   (list (string->bytes/utf-8 
          (include-template "main.html")))))

(define (extract-jsexpr req)
  (string->jsexpr (bytes->string/utf-8 (request-post-data/raw req))))

(define (extract-value req para-name)
  (let* [(bindings (request-bindings req))]
    (if (exists-binding? para-name bindings)
        (extract-binding/single para-name bindings)
        (hash-ref (extract-jsexpr req) para-name))))
  

(define (gen-status req para-name)
  (let* [(received-value (extract-value req para-name))
         (result (hash para-name received-value))]
    ;(printf " : ~s \n" result)
    (jsexpr->string result)))
    
(define (post-status req)
  (response/xexpr 
   (gen-status req 'text)))


(define (start request)
  (understanding-dispatch request))


;https://github.com/kjbekkelund/writings/blob/master/published/understanding-backbone.md/
;(printf "dir: ~s \n" (build-path (this-expression-source-directory) "public")) 
(serve/servlet start
               #:launch-browser? #t
               #:servlet-path "" 
               #:servlet-regexp #rx""
               #:stateless? #t
               #:quit? #f
               #:banner? #f
               #:listen-ip #f
               #:port 9998
               #:extra-files-paths
               (list (build-path (this-expression-source-directory) ".")))