#lang racket
(require db)
(struct blog (db))
(struct post (blog id))

(define (initialize-blog! home)
  (let* ([db (sqlite3-connect #:database home #:mode 'create)]
         [the-blog (blog db)])
    (unless (table-exists? db "posts")
      (query-exec 
       db
       (string-append
        "CREATE TABLE posts "
        "(id INTEGER PRIMARY KEY, title TEXT, body TEXT)"))
      (blog-insert-post!
       the-blog "First post!" "This is a first post.")
      (blog-insert-post!
       the-blog "Second post!" "This is a second post."))
    (unless (table-exists? db "comments")
      (query-exec 
       db
       (string-append
        "CREATE TABLE comments "
        "(pid INTEGER, content TEXT)"))
      (post-insert-comment!
       the-blog (first (blog-posts the-blog))
       "It's good!")
      (post-insert-comment!
       the-blog (first (blog-posts the-blog))
       "I don't think so"))
    the-blog))     

(define (blog-insert-post! a-blog title body)
  (query-exec
   (blog-db a-blog)
   "INSERT INTO posts (title, body) VALUES (?, ?)"
   title body))

(define (post-insert-comment! a-blog a-post a-comment)
  (query-exec
   (blog-db a-blog)
   "INSERT INTO comments (pid, content) VALUES (?, ?)"
   (post-id a-post) a-comment))

(define (blog-posts a-blog)
  (local [(define (id->post an-id)
            (post a-blog an-id))]
    (map id->post
         (query-list
          (blog-db a-blog)
          "SELECT id FROM  posts"))))

(define (post-title a-post)
  (query-value
   (blog-db (post-blog a-post))
   "SELECT title FROM posts WHERE id = ?"
   (post-id a-post)))

(define (post-body a-post)
  (query-value
   (blog-db (post-blog a-post))
   "SELECT body FROM posts WHERE id = ?"
   (post-id a-post)))

(define (post-comments a-post)
  (query-list
   (blog-db (post-blog a-post))
            "SELECT content FROM  comments where pid = ?"
            (post-id a-post)))

(provide (all-defined-out))