def gen_scatter_data(count, value_max=100)
    count_1 = count-1
    indexs = (0..count_1).to_a
    indexs = indexs.map {|x| rand().round(2)+x}
    values = indexs.map {|x| rand(value_max)}
    values2 = indexs.map {|x| rand(value_max)}
    [indexs.zip(values).map {|x, y| "{x:#{x},y:#{y}}"}.join(","),
        indexs.zip(values2).map {|x, y| "{x:#{x},y:#{y}}"}.join(",")]
end
# count = 100
if __FILE__ == $0
    require 'minitest/autorun'
    require 'minitest/spec'
    require 'testhelper'

    describe "some" do
        it "function" do
            gen_scatter_data(100).ppt
        end
    end
end
