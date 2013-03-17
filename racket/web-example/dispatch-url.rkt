#lang racket
(require web-server/http
         web-server/managers/none
         web-server/servlet
         web-server/servlet-env)

(provide blog-dispatch) 

(define-values (blog-dispatch blog-url)
    (dispatch-rules
     [("") list-posts]
     [("posts" "create") #:method "post" create-post]
     [("posts" (string-arg)) review-post]
     [("archive" (integer-arg) (integer-arg)) review-archive]
     [else list-posts]))


(define (review-archive req y m) `(review-archive ,y ,m))

(define (create-post req)
  (printf "create-post \n")
  (redirect-to 
   (string-append 
    "/posts/" 
    (extract-binding/single 
     'title 
     (request-bindings req))) permanently))

(define (review-post req tt)
  (printf "review-post \n")
  (response/xexpr
   `(html (head (title "Review a post"))
          (body
           (p "this is a post! about")
           (p ,tt)))))

(define (list-posts req)
     (response/xexpr
      `(html (head (title "Create a post"))
             (body
              (form ([action ,"/posts/create"] [method "post"])
                    "Enter a title: "
                    (input ([name "title"] [value "pp"]))
                    (p (a ([href "/quit"]) "Quit the setup servlet."))
                    (input ([type "submit"])))))))

(define (start request)
  (blog-dispatch request))

  
(serve/servlet start
               #:launch-browser? #t
               #:servlet-path "" 
               #:servlet-regexp #rx""
               #:quit? #f
               #:listen-ip #f
               #:port 9999)