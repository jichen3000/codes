def gen_code(start_index, end_index)
    result = ""
    start_index.upto(end_index).each do |index|
        result += %Q{
        n.res4b#{index}_branch2a = L.Convolution(n.res4b#{index-1}, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
        n.bn4b#{index}_branch2a = L.BatchNorm(n.res4b#{index}_branch2a, in_place=True, use_global_stats=True)
        n.scale4b#{index}_branch2a = L.Scale(n.res4b#{index}_branch2a, in_place=True, bias_term=True)
        n.res4b#{index}_branch2a_relu = L.ReLU(n.res4b#{index}_branch2a, in_place=True)

        n.res4b#{index}_branch2b = L.Convolution(n.res4b#{index}_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
        n.bn4b#{index}_branch2b = L.BatchNorm(n.res4b#{index}_branch2b, in_place=True, use_global_stats=True)
        n.scale4b#{index}_branch2b = L.Scale(n.res4b#{index}_branch2b, in_place=True, bias_term=True)
        n.res4b#{index}_branch2b_relu = L.ReLU(n.res4b#{index}_branch2b, in_place=True)
        
        n.res4b#{index}_branch2c = L.Convolution(n.res4b#{index}_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
        n.bn4b#{index}_branch2c = L.BatchNorm(n.res4b#{index}_branch2c, in_place=True, use_global_stats=True)
        n.scale4b#{index}_branch2c = L.Scale(n.res4b#{index}_branch2c, in_place=True, bias_term=True)

        n.res4b#{index} = L.Eltwise(n.res4b#{index-1}, n.res4b#{index}_branch2c)
        n.res4b#{index}_relu = L.ReLU(n.res4b#{index}, in_place=True)
            
        }
    end
    result
end

if __FILE__ == $0
    require 'minitest/autorun'
    require 'minitest/spec'
    require 'testhelper'

    describe "some" do
        it "function" do
            puts gen_code(6,22)
        end
    end
end