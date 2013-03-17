require 'java'
$CLASSPATH << 'D:/work/workspace/megatrust-client/bin'
$LOAD_PATH <<  'D:/work/workspace/megatrust-client/lib'
$LOAD_PATH <<  'D:/library/Java/libs'

require 'slf4j-api-1.5.1.jar'
require 'slf4j-log4j12-1.5.1.jar'
require 'log4j-1.2.14.jar'
require 'jtestr-0.5'
import 'com.mchz.megatrust.agent.protocol.NetworkHandlerImpl'
#import 'com.mchz.megatrust.agent.protocol.ActionRequest'
#import 'com.mchz.megatrust.agent.protocol.Protocol'
import  'java.io.ByteArrayOutputStream'
import  'java.io.DataOutputStream'
#include_package  "java.lang"
#import java.lang.Class
import java.net.Socket
require 'test/unit'
require 'rr'
#class NetworkHandlerImpl
#  java_signature 'NetworkHandlerImpl()'
#  def initialize
#    p "initialize"
##    super(1,2)
#  end
#end
class NetworkHandlerImplTest < Test::Unit::TestCase
  include RR::Adapters::TestUnit
  def setup
#    o = JavaClass.forName('com.mchz.megatrust.agent.protocol.NetworkHandlerImpl').newInstance()
#    p o
#    o = Java::JavaClass.for_name('com.mchz.megatrust.agent.protocol.NetworkHandlerImpl').constructor
#    p o
#    o = java.lang.Object.new
#    p o.java_class
    o  = stub(java.net.Socket)
    stub(o).java_class.returns(java.net.Socket)
#    p o.java_class
#    NetworkHandlerImpl.methods.each {|x| p x}
    p NetworkHandlerImpl.new(o)
#    socket = Object.new
#    construct = NetworkHandlerImpl.java_class.constructor(java.net.Socket)
#    o = construct.new_instance(socket)
#    stub(NetworkHandlerImpl).NetworkHandlerImpl.returns do
#      super
#    end
#    stub(socket).getOutputStream.returns(ByteArrayOutputStream.new)
##    stub(socket).getInputStream.returns(nil)
#    @arr = NetworkHandlerImpl4Test.new()
  end
  def test_true
    
  end
#  def test_sendData
#    byte_output = ByteArrayOutputStream.new
#    @arr.sendData(DataOutputStream.new(byte_output))
#    bytes = String.from_java_bytes(byte_output.toByteArray)
#    length = 54
#    assert_equal(54,bytes[0,8].unpack("NN")[1])
#    assert_equal(@arr.id,bytes[8,8].unpack("NN")[1])
#    assert_equal(@arr.type,bytes[16,4].unpack("N")[0])
#    assert_equal(@arr.script.size,bytes[20,8].unpack("NN")[1])
#    assert_equal(@arr.script,bytes[28,@arr.script.size])
#    assert_equal(@arr.filePath.size,bytes[28+@arr.script.size,8].unpack("NN")[1])
#    assert_equal(@arr.filePath,bytes[36+@arr.script.size,@arr.filePath.size])
#    assert_equal(@arr.sid.size,bytes[36+@arr.script.size+@arr.filePath.size,8].unpack("NN")[1])
#    assert_equal(@arr.sid,bytes[44+@arr.script.size+@arr.filePath.size,@arr.sid.size])
#  end
  
  
end

