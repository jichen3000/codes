#lang racket
(require web-server/http
         web-server/managers/none
         web-server/servlet
         web-server/servlet-env
         mzlib/etc)

(provide blog-dispatch) 

(define-values (blog-dispatch blog-url)
    (dispatch-rules
     [("") list-posts]
     [("posts" "create") #:method "post" create-post]
     [("posts" "count") count-post]
     [("posts" (string-arg)) review-post]
     [("archive" (integer-arg) (integer-arg)) review-archive]
     ))


(define (review-archive req y m) `(review-archive ,y ,m))

(define (create-post req)
  (printf "create-post \n")
  (redirect-to 
   (string-append 
    "/posts/" 
    (extract-binding/single 
     'title 
     (request-bindings req))) permanently))
(define (count-post req)
  (printf "count-post \n")
  (response/xexpr 
   (string-append 
    "11, " 
    (extract-binding/single 
     'content 
     (request-bindings req)))))

(define (review-post req tt)
  (printf "review-post \n")
  (response/xexpr
   `(html (head (title "Review a post"))
          (body
           (p "this is a post! about")
           (p ,tt)))))

(define (list-posts req)
     (response/xexpr
      `(html (head (title "Create a post")
                   (link ([rel "stylesheet"] 
                          [type "text/css"] 
                          [href "/main.css"]))
                   (script ([type "text/javascript"]
                            [src "http://code.jquery.com/jquery-latest.pack.js"]))
                   (script ([type "text/javascript"]
                            [src "main.js"]))
                   )
             (body
              (form ([action ,"/posts/create"] [method "post"])
                    "Enter a title: "
                    (input ([name "title"] [value "pp"]))
                    (p (a ([href "/quit"]) "Quit the setup servlet."))
                    (div ([class "cell answered"] )
                         (p ([id "messages"]) "show some"))
                    (button ([id "ajaxtest"]) "ajax test")
                    (input ([type "submit"])))))))

(define (start request)
  (blog-dispatch request))


;http://planet.plt-scheme.org/package-source/ryanc/scriblogify.plt/1/0/
(printf "dir: ~s \n" (build-path (this-expression-source-directory) "public")) 
(serve/servlet start
               #:launch-browser? #f
               #:servlet-path "" 
               #:servlet-regexp #rx""
               #:quit? #f
               #:banner? #f
               #:listen-ip #f
               #:port 9999
               #:extra-files-paths
               (list (build-path (this-expression-source-directory) "public")))