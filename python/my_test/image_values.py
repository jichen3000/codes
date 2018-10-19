# for jupyter
%matplotlib inline
import matplotlib.pyplot as plt

plt.hist(the_image.flatten())
plt.ylabel('values')
plt.xlabel('image')
plt.title('Histogram of DICOM image')
plt.show()