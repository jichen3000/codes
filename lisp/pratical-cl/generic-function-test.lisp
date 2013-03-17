(defgeneric withdraw (account amount)
  (:documentation "Withdraw the specified amount from the account.
    Signal an error if the current balance is less than amount."))

; bank-account is a specializer
(defmethod withdraw ((acount bank-account) amount)
    (when (< (balance account) amount)
        (error "Account overdrawn."))
    (decf (balance account) amount))

; call-next-method just like super in the Java
(defmethod withdraw ((account checking-account) amount)
  (let ((overdraft (- amount (balance account))))
    (when (plusp overdraft)
      (withdraw (overdraft-account account) overdraft)
      (incf (balance account) overdraft)))
  (call-next-method))

; (defmethod withdraw ((proxy proxy-account) amount)
;   (withdraw (proxied-account proxy) amount))

; (defmethod withdraw ((account (eql *account-of-bank-president*)) amount)
;   (let ((overdraft (- amount (balance account))))
;     (when (plusp overdraft)
;       (incf (balance account) (embezzle *bank* overdraft)))
;     (call-next-method)))

