#
#  tsne.py
#
# Implementation of t-SNE in Python. The implementation was tested on Python 2.7.10, and it requires a working
# installation of NumPy. The implementation comes with an example on the MNIST dataset. In order to plot the
# results of this example, a working installation of matplotlib is required.
#
# The example can be run by executing: `ipython tsne.py`
#
#
#  Created by Laurens van der Maaten on 20-12-08.
#  Copyright (c) 2008 Tilburg University. All rights reserved.

# see t-SNE.mindnode

import numpy
import pylab as Plot

def Hbeta(D = numpy.array([]), beta = 1.0):
	"""Compute the perplexity and the P-row for a specific value of the precision of a Gaussian distribution."""

	# Compute P-row and corresponding perplexity
	P = numpy.exp(-D.copy() * beta);
	sumP = sum(P);
	H = numpy.log(sumP) + beta * numpy.sum(D * P) / sumP;
	P = P / sumP;
	return H, P;


def x2p(X = numpy.array([]), tol = 1e-5, perplexity = 30.0):
	"""Performs a binary search to get P-values in such a way that each conditional Gaussian has the same perplexity."""
	# not exactly as equation 1 in t-SNE

	# Initialize some variables
	print "Computing pairwise distances..."
	(n, d) = X.shape;
	# sum_X = numpy.sum(numpy.square(X), 1);
	# D is matrix of distance numpy.add(numpy.add(-2 * numpy.dot(cc, cc.T), sum_cc).T, sum_cc)
	# d12, means, the distance between X1 and X2, d11 will be 0. 
	# D = numpy.add(numpy.add(-2 * numpy.dot(X, X.T), sum_X).T, sum_X);
	D = cal_distance_matrix(X)
	P = numpy.zeros((n, n));
	beta = numpy.ones((n, 1));
	logU = numpy.log(perplexity);

	# Loop over all datapoints
	for i in range(n):

		# Print progress
		if i % 500 == 0:
			print "Computing P-values for point ", i, " of ", n, "..."

		# Compute the Gaussian kernel and entropy for the current precision
		betamin = -numpy.inf;
		betamax =  numpy.inf;
		Di = D[i, numpy.concatenate((numpy.r_[0:i], numpy.r_[i+1:n]))];
		(H, thisP) = Hbeta(Di, beta[i]);

		# Evaluate whether the perplexity is within tolerance
		Hdiff = H - logU;
		tries = 0;
		while numpy.abs(Hdiff) > tol and tries < 50:

			# If not, increase or decrease precision
			if Hdiff > 0:
				betamin = beta[i].copy();
				if betamax == numpy.inf or betamax == -numpy.inf:
					beta[i] = beta[i] * 2;
				else:
					beta[i] = (beta[i] + betamax) / 2;
			else:
				betamax = beta[i].copy();
				if betamin == numpy.inf or betamin == -numpy.inf:
					beta[i] = beta[i] / 2;
				else:
					beta[i] = (beta[i] + betamin) / 2;

			# Recompute the values
			(H, thisP) = Hbeta(Di, beta[i]);
			Hdiff = H - logU;
			tries = tries + 1;

		# Set the final row of P
		P[i, numpy.concatenate((numpy.r_[0:i], numpy.r_[i+1:n]))] = thisP;

	# Return final P-matrix
	print "Mean value of sigma: ", numpy.mean(numpy.sqrt(1 / beta));
	return P;


def pca(X = numpy.array([]), no_dims = 50):
	"""Runs PCA on the NxD array X in order to reduce its dimensionality to no_dims dimensions."""

	# find the component according variance
	print "Preprocessing the data using PCA..."
	(n, d) = X.shape;
	# sub the mean by columns
	X = X - numpy.tile(numpy.mean(X, 0), (n, 1));
	# find eig
	(l, M) = numpy.linalg.eig(numpy.dot(X.T, X));
	Y = numpy.dot(X, M[:,0:no_dims]);
	return Y;

def cal_distance_matrix(x_rows):
	row_squares = numpy.sum(numpy.square(x_rows), 1);
	distance_matrix = numpy.add(numpy.add(-2 * numpy.dot(x_rows, x_rows.T), row_squares).T, row_squares);
	return distance_matrix


def tsne(X = numpy.array([]), no_dims = 2, initial_dims = 50, perplexity = 30.0):
	"""Runs t-SNE on the dataset in the NxD array X to reduce its dimensionality to no_dims dimensions.
	The syntaxis of the function is Y = tsne.tsne(X, no_dims, perplexity), where X is an NxD NumPy array."""

	# Check inputs
	# wrong, not check the X type
	if isinstance(no_dims, float):
		print "Error: array X should have type float.";
		return -1;
	if round(no_dims) != no_dims:
		print "Error: number of dimensions should be an integer.";
		return -1;

	# Initialize variables
	X = pca(X, initial_dims).real;
	(n, d) = X.shape;
	max_iter = 1000;
	initial_momentum = 0.5;
	final_momentum = 0.8;
	eta = 500;
	min_gain = 0.01;
	# sample of normal distribution, mean = 0, stardand_variance = 1
	Y = numpy.random.randn(n, no_dims);
	dY = numpy.zeros((n, no_dims));
	iY = numpy.zeros((n, no_dims));
	gains = numpy.ones((n, no_dims));

	# Compute P-values
	P = x2p(X, 1e-5, perplexity);
	P = P + numpy.transpose(P);
	P = P / numpy.sum(P);
	P = P * 4;									# early exaggeration
	P = numpy.maximum(P, 1e-12);

	# Run iterations
	for iter in range(max_iter):

		# Compute pairwise affinities
		# sum_Y = numpy.sum(numpy.square(Y), 1);
		# num = 1 / (1 + numpy.add(numpy.add(-2 * numpy.dot(Y, Y.T), sum_Y).T, sum_Y));
		num = 1 / (1 + cal_distance_matrix(Y))
		num[range(n), range(n)] = 0;
		Q = num / numpy.sum(num);
		Q = numpy.maximum(Q, 1e-12);

		# Compute gradient
		PQ = P - Q;
		for i in range(n):
			# equation 5
			# dY[i,:] = numpy.sum(numpy.tile(PQ[i,:] * num[i,:], (no_dims, 1)).T * (Y[i,:] - Y), 0)
			dY[i,:] = numpy.sum(numpy.tile(PQ[:,i] * num[:,i], (no_dims, 1)).T * (Y[i,:] - Y), 0);

		# Perform the update
		if iter < 20:
			momentum = initial_momentum
		else:
			momentum = final_momentum
		gains = (gains + 0.2) * ((dY > 0) != (iY > 0)) + (gains * 0.8) * ((dY > 0) == (iY > 0));
		gains[gains < min_gain] = min_gain;
		# last step in simple version of SNE
		iY = momentum * iY - eta * (gains * dY);
		Y = Y + iY;
		Y = Y - numpy.tile(numpy.mean(Y, 0), (n, 1));

		# Compute current value of cost function
		if (iter + 1) % 10 == 0:
			C = numpy.sum(P * numpy.log(P / Q));
			print "Iteration ", (iter + 1), ": error is ", C

		# Stop lying about P-values
		if iter == 100:
			P = P / 4;

	# Return solution
	return Y;


if __name__ == "__main__":
	print "Run Y = tsne.tsne(X, no_dims, perplexity) to perform t-SNE on your dataset."
	print "Running example on 2,500 MNIST digits..."
	# X.shape is 2500,784
	# one image is 28 * 28 =784
	X = numpy.loadtxt("./data/mnist2500_X.txt");
	labels = numpy.loadtxt("./data/mnist2500_labels.txt");
	# import ipdb; ipdb.set_trace()
	Y = tsne(X, 2, 50, 20.0);
	Plot.scatter(Y[:,0], Y[:,1], 20, labels);
	Plot.show();
