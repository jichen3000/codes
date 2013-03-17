require 'java'
$CLASSPATH << 'D:/work/workspace/megatrust-client/bin'


import 'com.mchz.megatrust.agent.protocol.ActionResultRequest'
import 'com.mchz.megatrust.agent.protocol.ActionRequest'
import 'com.mchz.megatrust.agent.protocol.Protocol'
import  'java.io.ByteArrayOutputStream'
import  'java.io.DataOutputStream'
require 'test/unit'
#require 'active_support/core_ext/kernel/requires'
#require 'active_support/test_case'
require 'rr'

class ActionResultRequestTest < Test::Unit::TestCase
  include RR::Adapters::TestUnit
  def setup
    action_request =  ActionRequest.new
    action_request.actionResultId = 100
    action_request.script = 'jc'
    action_request.sourceFilePath = '/home/colin'
    action_request.sid = '11111'
    action_request.scriptType = "COMMAND"
    @action_result_request = ActionResultRequest.new(action_request)
  end
  def test_getCode
    assert_equal(Protocol::ACTION_RESULT,@action_result_request.getCode())
  end
  
  def test_sendData
    byte_output = ByteArrayOutputStream.new
    @action_result_request.sendData(DataOutputStream.new(byte_output))
    bytes = String.from_java_bytes(byte_output.toByteArray)
    assert_equal(158,bytes[0,8].unpack("NN")[1])
    assert_equal(@action_result_request.id,bytes[8,8].unpack("NN")[1])
    assert_equal(@action_result_request.type,bytes[16,4].unpack("N")[0])
    assert_equal(@action_result_request.script.size,bytes[20,8].unpack("NN")[1])
    assert_equal(@action_result_request.script,bytes[28,@action_result_request.script.size])
    assert_equal(@action_result_request.filePath.size,bytes[28+@action_result_request.script.size,8].unpack("NN")[1])
    assert_equal(@action_result_request.filePath,bytes[36+@action_result_request.script.size,@action_result_request.filePath.size])
    assert_equal(@action_result_request.sid.size,bytes[36+@action_result_request.script.size+@action_result_request.filePath.size,8].unpack("NN")[1])
    assert_equal(@action_result_request.sid,bytes[44+@action_result_request.script.size+@action_result_request.filePath.size,@action_result_request.sid.size])
  end
  
#  def test_new_fake
#    # 不能使用下面的方法来mock一个对象。
#    action_request = ActionRequest.new
#    stub(action_request).actionResultId.returns(100)
#    stub(action_request).script.returns('jc')
#    stub(action_request).sourceFilePath.returns('/home/colin')
#    stub(action_request).sid.returns('11111')
#    stub(action_request).scriptType.returns("COMMAND")
#    stub(action_request).actionResultId.returns("COMMAND")
#    action_result_request = ActionResultRequest.new(action_request)
#  end
  
end

