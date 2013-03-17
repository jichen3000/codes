require 'rubygems'
require 'sinatra'
require 'haml'
require 'json'


set :root, File.dirname(__FILE__)
set :public_folder, Proc.new{ File.join(root, "") }
set :views, Proc.new{ File.join(root, "") }

# set :binding, "10.140.41.186"

get "/" do
  # send_file File.join(settings.public_folder, 'main.html')
  # haml :main
  File.read("main.html")
end

get "/test.html" do
    haml :test
end


# get "/sudoku/sudokuresult" do
#   #params[:fix_values].each {|point,v| p point,v}
#   result = NineSquare.new(params[:fix_values]).perform().get_multi_result()[0]
#   points = {}
#   result.each do |key,value|
#     new_key = key.join("_")
#     if not params[:fix_values][new_key]
#       points[key.join("_")]=value
#     end
#   end
#   points.to_json
# end

# def helper(group_index, inner_index)
#   y, x = group_index.divmod(3)
#   inner_y, inner_x = inner_index.divmod(3)
#   [x*3+inner_x, y*3+inner_y]
# end
