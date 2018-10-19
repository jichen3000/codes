# http://stackoverflow.com/questions/8691812/get-object-methods-r

v <- 1:5
v
class(v)
# showMethods(classes="data.frame")
methods(class="data.frame")
methods(class=class(v))