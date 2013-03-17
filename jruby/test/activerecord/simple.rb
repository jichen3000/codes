#development:
#  adapter: oracle
#  database: testapp_development
#  username: testapp
#  password:
require 'java'
require 'rubygems'
require "D:/work/workspace/colin-jruby/lib/ojdbc14.jar"

require "active_record"
ActiveRecord::Base.establish_connection(
  :adapter => 'jdbc',
  :driver => 'oracle.jdbc.driver.OracleDriver',
  :url => 'jdbc:oracle:thin:@172.16.4.98:1521:xe',
#  :adapter  => "oracle",
#  :database => "xe",
  :username => "colin_test",
  :password => "colin_test"
)
ActiveRecord::Base.pluralize_table_names = false
ActiveRecord::Base.table_name_prefix = 'mc$ma_'
#log_path = File.join(File.dirname(__FILE__),'sql.log')
#ActiveRecord::Base.logger = Logger.new(log_path, 3, 2048000)
class Issue < ActiveRecord::Base
end
p issue_detail = Issue.find(:first)
p "ok"