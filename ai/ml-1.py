import numpy as np
import random
import pdb

def forward (X, weight, bias):
     return X * weight + bias

def lossfunc(Ytrue, Ypred):
     n = len(Ytrue)
     return np.sum(Ytrue - Ypred) ** 2 / n

def backward (X, Ytrue, Ypred, loss, weight, bias):
     n = len(Ytrue)
     weight_gradient = (-2/n) * sum ( X * (Ytrue - Ypred))
     bias_gradient   = (-2/n) * sum (Ytrue - Ypred)

     learning_rate   = 0.0001
     weight = weight - (learning_rate * weight_gradient)
     bias   = bias   - (learning_rate * weight_gradient)

     return weight, bias

X = np.array([5])
Ytrue = np.array([2*X + 3 for x in X])
pdb.set_trace()
weight = random.random()
bias   = random.random()

for epoch in range(10000):
     Ypred = forward (X, weight, bias)
 
     loss  = lossfunc (Ytrue, Ypred)
     if loss < 0.00001:
          break
     if epoch % 10 == 0:
          print ("{:3d}, x={}, Y={}, Ypred={}, losses={:5.4f}, weight={}, bias={}".format(epoch, X, 2*X + 3, Ypred, loss, weight, bias))

     weight, bias = backward (X, Ytrue, Ypred, loss, weight, bias)
