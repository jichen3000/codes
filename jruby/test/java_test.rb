ENV.each do |i|
  p i
end
require 'java'
$CLASSPATH << 'D:/work/workspace/colin-java/bin'
$LOAD_PATH <<  'D:/library/Java/libs'
p $LOAD_PATH
# it need lib dir, and ojdbc14.jar
require 'ojdbc14.jar'
#require  'com.colin.test.ruby.RubyTest.class'
java_import 'com.colin.test.ruby.RubyTest'
java_import 'com.colin.test.ruby.Colin'
#include_class  'com.colin.test.ruby.RubyTest'
class JavaTest
  x = RubyTest.new
  x.check  
  p x.privateCheck
  p x.getInt
  p x.add(1, 2)
  c = Colin.new
  c.setName("jc")
  p c
  c = x.addColin(c)
  p c.getName
end
