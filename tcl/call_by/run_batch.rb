require 'json'
def extract_result(all_str)
    regexp_rule = /tcl_result&&&(.+)&&&/m
    if match_result = all_str.match(regexp_rule)
        return JSON::load(match_result.captures.first)
    end
    nil
end
def run_bp_test()
    # [username, password, test_name, timeout_mins].pt
    tcl_path = File.join(File.dirname(__FILE__), 'batch.tcl')
    cmd_str = "bptcl #{tcl_path} test_run"
    # cmd_str = "date"
    # cmd_str.pt
    result = %x{#{cmd_str}}
    # $log.info(result)
    puts "result:#{result}"
    result
end

bp_result = run_bp_test()
puts extract_result(bp_result)

