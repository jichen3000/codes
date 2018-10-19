# code in Chapter 8\csv_files.jl:
fname = "wine.csv"
# use ; to avoid print the value of data
data = readdlm(fname, ';');

# data2 = readcsv(fname)

# data3 = readdlm(fname, ';', Float64, '\n', header=true)

# row3 = data[3, :]
# col3 = data[ :, 3]

# # To get a matrix with the data from columns 3, 6, and 11, execute the following command:
# z = [data[:,3] data[:,6] data[:,11]]

# writedlm("partial.dat", data, ';')