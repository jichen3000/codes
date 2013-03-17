(defpackage :com.gigamonkeys.text-db
    (:use :common-lisp)
    (:export :open-db
           :save
           :store))
; just import one method
(defpackage :com.gigamonkeys.email-db
  (:use :common-lisp :com.gigamonkeys.text-db)
  (:import-from :com.acme.email :parse-email-address))

; don't import the one method from all packages
(defpackage :com.gigamonkeys.email-db
  (:use
   :common-lisp
   :com.gigamonkeys.text-db
   :com.acme.text)
  (:import-from :com.acme.email :parse-email-address)
  (:shadow :build-index))

(in-package :com.gigamonkeys.text-db)

; don't import the one method from a specail package
(defpackage :com.gigamonkeys.email-db
  (:use
   :common-lisp
   :com.gigamonkeys.text-db
   :com.acme.text)
  (:import-from :com.acme.email :parse-email-address)
  (:shadow :build-index)
  (:shadowing-import-from :com.gigamonkeys.text-db :save)) 
; (in-package :cl-user)


 (foo)
 (use-package :foolib)
 ; in this case, lisp will report error