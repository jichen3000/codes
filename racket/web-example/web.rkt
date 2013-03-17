#lang racket
(require web-server/servlet
         web-server/servlet-env)

(define (colin-app request)
  (response/xexpr
   `(html (head (title "Hello world!"))
          (body (p "Hey out there!")))))
 
;(define (colin-app req)
;  (start
;   (send/suspend
;    (lambda (k-url)
;      (response/xexpr
;       `(html (body (a ([href ,k-url]) "Hello world!"))))))))
 
;(serve/servlet start #:stateless? #t)
(serve/servlet colin-app
               #:quit? #f
               #:listen-ip #f
               #:stateless? #t
               #:port 9999)
