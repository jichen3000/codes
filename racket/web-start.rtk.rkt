#lang web-server/insta
(struct post (title body))
(define post-1 (post "First post!" "This is a first post."))
(struct blog (posts) #:mutable)
(define BLOG (blog
              (list post-1
                        (post "Second post!" "test post"))))

(define (blog-insert-post! blog post)
  (set-blog-posts! blog
                   (cons post (blog-posts blog))))
;(define (start request)
;  (response/xexpr
;   '(html
;     (head (title "Colin's Blog"))
;     (body (h1 "Under construction")))))
(define (start request)
  (render-blog-page request))

(define (can-parse-post? bindings)
  (and (exists-binding? 'title bindings)
       (exists-binding? 'body bindings)))

(define (parse-post bindings)
  (post (extract-binding/single 'title bindings)
        (extract-binding/single 'body bindings)))


(define (render-posts)
  `(div ((class "posts"))
        ,@(map render-post (blog-posts BLOG))))
(define (render-blog-page request)
  (local [(define (response-generator embed/url)
            (response/xexpr
             `(html (head (title "My Blog"))
                    (body
                     (h1 "My Blog")
                     ,(render-posts)
                     (form ((action
                             ,(embed/url insert-post-handler)))
                           (input ((name "title")))
                           (input ((name "body")))
                           (input ((type "submit"))))))))
 
          (define (insert-post-handler request)
            (blog-insert-post! BLOG (parse-post (request-bindings request)))
            (render-blog-page request))]
 
    (send/suspend/dispatch response-generator)))
           
(define (render-post post)
  `(div ((class "post")) ,(post-title post) (p ,(post-body post))))