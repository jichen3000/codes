(defun jc ()
    (print "jc"))
(defparameter jc "jc")
; (defclass name)
(defclass bank-account ()
    (customer-name
    balance))
(defparameter *account* 
    (make-instance 'bank-account)) 
(setf (slot-value *account* 'customer-name) "John Doe") 
(setf (slot-value *account* 'balance) 1000)
(print *account*)
(print (slot-value *account* 'customer-name))

(defclass bank-account ()
  ((customer-name
    :initarg :customer-name)
   (balance
    :initarg :balance
    :initform 0)))
(defparameter *account*
  (make-instance 'bank-account :customer-name "John Berry"))
(print (slot-value *account* 'customer-name))
(print (slot-value *account* 'balance))
; it will reprot error
; (slot-value (make-instance 'bank-account) 'customer-name)

(defvar *account-numbers* 0)
(defclass bank-account ()
  ((customer-name
    :initarg :customer-name
    ; :writer (setf customer-name)
    ; :reader customer-name
    :accessor customer-name
    :initform (error "Must supply a customer name."))
   (balance
    :initarg :balance
    :initform 0
    :writer (setf balance)
    :reader balance)
   (account-number
    :initform (incf *account-numbers*))))
; (slot-value (make-instance 'bank-account) 'customer-name)

; initial method
(defmethod initialize-instance :after 
    ((account bank-account) &key opening-bonus-percentage)
    (when opening-bonus-percentage
        (incf (slot-value account 'balance)
            (* (slot-value account 'balance) 
                (/ opening-bonus-percentage 100)))))

(defparameter *acct* 
    (make-instance
        'bank-account
         :customer-name "Sally Sue."
         :balance 1000
         :opening-bonus-percentage 5))

(print (slot-value *acct* 'balance))
(print (balance *acct*))

; There's no need to define the set and get methods like the belows.
; (defgeneric balance (account))
; (defmethod balance ((account bank-account))
;   (slot-value account 'balance))
; (print (balance *acct*))

; (defun (setf customer-name) (name account)
;   (setf (slot-value account 'customer-name) name))
(setf (customer-name *acct*) "Colin Ji")
(print (customer-name *acct*))

(defparameter *minimum-blance* 50)
; wiht-accessors just like with-slots, except it invoke accessors. 
(defmethod assess-low-balance-penalty ((account bank-account))
    (with-slots (balance) account
        (when (< balance *minimum-blance*)
            (decf balance (* balance .01)))))

(setf (balance *acct*) 40)
(assess-low-balance-penalty *acct*)
(print (balance *acct*))

(defclass foo ()
  ((a :initarg :a :initform "A" :accessor a)
   (b :initarg :b :initform "B" :accessor b)))
(defclass bar (foo)
  ((a :initform (error "Must supply a value for a"))
   (b :initarg :the-b :accessor the-b :allocation :class)))