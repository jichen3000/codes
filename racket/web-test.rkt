#lang racket
(struct post (title body))
(define BLOG (list (post "First Post!"
                         "Hey, this is my first post!")))
