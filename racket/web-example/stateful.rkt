#lang racket
(require web-server/http
         web-server/managers/none
         web-server/servlet
         web-server/servlet-env)
(provide interface-version manager colin-app)
 
(define interface-version 'v2)
(define manager
  (create-none-manager
   (lambda (req)
     (response/xexpr
      `(html (head (title "No Continuations Here!"))
             (body (h1 "No Continuations Here!")))))))
(define (colin-app req)
(send/suspend
 (lambda (k-url)
   (response/xexpr
    `(html (head (title "Enter a number"))
           (body
            (form ([action ,k-url])
                  "Enter a number: "
                  (input ([name "number"]))
                  (input ([type "submit"])))))))))



(serve/servlet colin-app
               #:quit? #f
               #:listen-ip #f
               #:port 9999)