#lang web-server/insta
(require web-server/formlets
         "model-sql.rkt")


(define (start request)
  (printf "current-directory: ~s \n" (current-directory))
  (render-blog-page 
   (initialize-blog!
    (build-path 
     (current-directory)           
     "the-blog-data-sql.db"))
   request))

(define new-post-formlet
  (formlet
   (#%# ,((to-string
           (required
            (text-input
             #:attributes '([class "form-text"]))))
          . => . title)
        ,((to-string
           (required
            (text-input
             #:attributes '([class "form-text"]))))
          . => . body))
   (values title body)))

(define (render-blog-page a-blog request)
  (local [(define (response-generator embed/url)
            (response/xexpr
             `(html (head (title "My Blog"))
                    (body
                     (h1 "My Blog")
                     ,(render-posts a-blog embed/url)
                     (form ((action
                             ,(embed/url insert-post-handler)))
                           ,@(formlet-display new-post-formlet)
                           (input ((type "submit"))))))))
          (define (parse-post bindings)
            (post (extract-binding/single 'title bindings)
                  (extract-binding/single 'body bindings) 
                  (list)))
          (define (insert-post-handler request)
            (define-values (title body)
              (formlet-process new-post-formlet request))
            (blog-insert-post! a-blog title body)
            (render-blog-page a-blog (redirect/get)))]
    (send/suspend/dispatch response-generator)))

(define (render-post-detail-page a-blog a-post request)
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
                           (a ((href ,(embed/url back-handler))) "back")
                           )))))
 
          (define (parse-comment bindings)
            (extract-binding/single 'comment bindings))
 
          (define (insert-comment-handler request)
            (render-confirm-add-comment-page
             a-blog
             (parse-comment (request-bindings request))
             a-post
             request))
          (define (back-handler request)
            (render-blog-page a-blog request))
          ]
 
 
    (send/suspend/dispatch response-generator)))

(define (render-confirm-add-comment-page 
         a-blog a-comment a-post request)
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
            (post-insert-comment! a-blog a-post a-comment)
            (render-post-detail-page a-blog a-post (redirect/get)))
 
          (define (cancel-handler request)
            (render-post-detail-page a-post request))]
 
    (send/suspend/dispatch response-generator)))

(define (render-posts a-blog embed/url)
  (local [(define (render-post/embed/url a-post)
            (render-post a-blog a-post embed/url))]
    `(div ((class "posts"))
          ,@(map render-post/embed/url (blog-posts a-blog)))))

(define (render-post a-blog a-post embed/url)
  (local [(define (view-post-handler request)
            (render-post-detail-page a-blog a-post request))]
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