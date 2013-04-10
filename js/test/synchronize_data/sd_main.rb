require 'sinatra'
require 'sinatra/reloader'
require 'json'

settings.public_folder = "."
get '/' do
  send_file File.join(settings.public_folder, 'index.html')
end

post "/clock" do
  # result = NineSquare.new(params[:fix_values]).perform().get_multi_result()[0]
  # points = {}
  # result.each do |key,value|
  #   new_key = key.join("_")
  #   if not params[:fix_values][new_key]
  #     points[key.join("_")]=value
  #   end
  # end
  # points.to_json

  # puts "records",params[:records]

  result = params[:records].map {|key, value| value['serverDate'] = "1"; value}
  puts "result:",result
  puts "addr:",request.ip
  puts "host:",request.host
  puts "rage!"
  result.to_json
end

# def helper(group_index, inner_index)
#   y, x = group_index.divmod(3)
#   inner_y, inner_x = inner_index.divmod(3)
#   [x*3+inner_x, y*3+inner_y]
# end
