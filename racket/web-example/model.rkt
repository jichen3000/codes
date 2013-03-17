#lang racket
(struct blog (home posts) #:mutable #:prefab)
(struct post (title body comments) #:mutable #:prefab)

(define (initialize-blog! home)
  (local [(define (log-missing-exn-handler exn)
            (blog
             (path->string home)
             (list (post "First post!" 
                         "This is a first post."
                         (list "It's good!" 
                               "I don't think so" 
                               "dislike"))
                   (post "Second post!" 
                         "test post"
                         (list "bad")))))
          (define the-blog
            (with-handlers ([exn? log-missing-exn-handler])
              (with-input-from-file home read)))]
    (set-blog-home! the-blog (path->string home))
    the-blog))

(define (save-blog! a-blog)
  (local [(define (write-to-blog)
            (write a-blog))]
    (with-output-to-file (blog-home a-blog)
      write-to-blog
      #:exists 'replace)))

(define (blog-insert-post! a-blog title body)
  (set-blog-posts!
   a-blog
   (cons (post title body empty)
         (blog-posts a-blog)))
  (save-blog! a-blog))

(define (post-insert-comment! a-blog a-post a-comment)
  (set-post-comments!
   a-post
   (cons a-comment
         (post-comments a-post)))
  (save-blog! a-blog))

(provide (all-defined-out))