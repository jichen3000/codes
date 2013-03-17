#lang web-server/insta
(struct post (title body comments) #:mutable)

(define (post-insert-comment! post comment)
  (set-post-comments! 
   post
   (cons comment (post-comments post))))

(struct blog (posts) #:mutable)

(define BLOG (blog
              (list (post "First post!" "This is a first post."
                          (list "It's good!" "I don't think so" "dislike"))
                    (post "Second post!" "test post"
                          (list "bad")))))

(define (blog-insert-post! blog post)
  (set-blog-posts! blog
                   (cons post (blog-posts blog))))


(define (start request)
  (render-blog-page request))





(define (render-blog-page request)
  (local [(define (response-generator embed/url)
            (response/xexpr
             `(html (head (title "My Blog"))
                    (body
                     (h1 "My Blog")
                     ,(render-posts embed/url)
                     (form ((action
                             ,(embed/url insert-post-handler)))
                           (input ((name "title")))
                           (input ((name "body")))
                           (input ((type "submit"))))))))
          (define (parse-post bindings)
            (post (extract-binding/single 'title bindings)
                  (extract-binding/single 'body bindings) 
                  (list)))
          (define (insert-post-handler request)
            (blog-insert-post! BLOG (parse-post (request-bindings request)))
            (render-blog-page (redirect/get)))] 
    (send/suspend/dispatch response-generator)))

(define (render-post-detail-page a-post request)
  (local [(define (response-generator embed/url)
            (response/xexpr
             `(html (head (title "Post Details"))
                    (body
                     (h1 "Post Details")
                     (h2 ,(post-title a-post))
                     (p ,(post-body a-post))
                     ,(render-as-itemized-list
                       (post-comments a-post))
                     (form ((action
                             ,(embed/url insert-comment-handler)))
                           (input ((name "comment")))
                           (input ((type "submit")))
                           (a ((href ,(embed/url render-blog-page))) "back")
                           )))))
 
          (define (parse-comment bindings)
            (extract-binding/single 'comment bindings))
 
          (define (insert-comment-handler request)
            (render-confirm-add-comment-page
             (parse-comment (request-bindings request))
             a-post
             request))]
 
 
    (send/suspend/dispatch response-generator)))
(define (render-confirm-add-comment-page a-comment a-post request)
  (local [(define (response-generator embed/url)
            (response/xexpr
             `(html (head (title "Add a Comment"))
                    (body
                     (h1 "Add a Comment")
                     "The comment: " (div (p ,a-comment))
                     "will be added to "
                     (div ,(post-title a-post))
 
                     (p (a ((href ,(embed/url yes-handler)))
                           "Yes, add the comment."))
                     (p (a ((href ,(embed/url cancel-handler)))
                           "No, I changed my mind!"))))))
 
          (define (yes-handler request)
            (post-insert-comment! a-post a-comment)
            (render-post-detail-page a-post request))
 
          (define (cancel-handler request)
            (render-post-detail-page a-post request))]
 
    (send/suspend/dispatch response-generator)))
(define (render-posts embed/url)
  (local [(define (render-post/embed/url a-post)
            (render-post a-post embed/url))]
    `(div ((class "posts"))
          ,@(map render-post/embed/url (blog-posts BLOG)))))

(define (render-post a-post embed/url)
  (local [(define (view-post-handler request)
            (render-post-detail-page a-post request))]
    `(div ((class "post"))
          (a ((href ,(embed/url view-post-handler)))
             ,(post-title a-post))
          (p ,(post-body a-post))
          (div ,(number->string (length (post-comments a-post)))
               " comment(s)"))))

(define (render-as-itemized-list fragments)
  `(ul ,@(map render-as-item fragments)))

(define (render-as-item a-fragment)
  `(li ,a-fragment))