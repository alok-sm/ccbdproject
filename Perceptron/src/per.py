from pylab import rand,plot,show,norm,figure
from mpl_toolkits.mplot3d import Axes3D

class Perceptron:
 def __init__(self):
  """ perceptron initialization """
  self.w = rand(3)*2-1 # weights #change to rand(2) for 2 vars
  self.learningRate = 0.1

 def response(self,x):
  """ perceptron output """
  y = x[0]*self.w[0]+x[1]*self.w[1] +x[2]*self.w[2]# dot product between w and x
  if y >= 0:
   return 1
  else:
   return -1

 def updateWeights(self,x,iterError):
  """
   updates the weights status, w at time t+1 is
       w(t+1) = w(t) + learningRate*(d-r)*x
   where d is desired output and r the perceptron response
   iterError is (d-r)
  """
  self.w[0] += self.learningRate*iterError*x[0]
  self.w[1] += self.learningRate*iterError*x[1]
  self.w[2] += self.learningRate*iterError*x[2] #added

 def train(self,data):
  """ 
   trains all the vector in data.
   Every vector in data must have three elements,
   the third element (x[2]) must be the label (desired output)
  """
  learned = False
  iteration = 0
  while not learned:
   globalError = 0.0
   for x in data: # for each sample
    r = self.response(x)    
    if x[3] != r: # if we have a wrong response (changed to 3 from 2)
     iterError = x[3] - r # desired response - actual response (changed from 3 to 2)
     self.updateWeights(x,iterError)
     globalError += abs(iterError)
   iteration += 1
   if globalError == 0.0 or iteration >= 1000: # stop criteria
    print 'iterations',iteration
    learned = True # stop learning

def generateData(n):
 """ 
  generates a 2D linearly separable dataset with n samples. 
  The third element of the sample is the label
 """
 xb = (rand(n)*2-1)/3-0.5
 yb = (rand(n)*2-1)/3+0.5
 xr = (rand(n)*2-1)/3+0.5
 yr = (rand(n)*2-1)/3-0.5
 zb = (rand(n)*2-1)/3-0.5 #z added
 zr = (rand(n)*2-1)/3+0.5 #z added
 inputs = []
 for i in range(len(xb)):
  inputs.append([xb[i],yb[i],zb[i],1]) #z added
  inputs.append([xr[i],yr[i],zr[i],-1]) # z added
 return inputs

trainset = generateData(30) # train set generation
perceptron = Perceptron()   # perceptron instance
perceptron.train(trainset)  # training
testset = generateData(20)  # test set generation

fig = figure()
 
ax = Axes3D(fig)

# Perceptron test
for x in testset:
 r = perceptron.response(x)
 if r != x[3]: # if the response is not correct
  print 'error'
 if r == 1:
  ax.plot([x[0], x[0]], [x[1], x[1]], [0, x[2]],'--', linewidth=2, color='b', alpha=.5)
  #plot(x[0],x[1],x[2],'ob')  
 else:
  ax.plot([x[0], x[0]], [x[1], x[1]], [0, x[2]],'--', linewidth=2, color='r', alpha=.5)
  #plot(x[0],x[1],x[2],'or')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# plot of the separation line.
# The separation line is orthogonal to w
n = norm(perceptron.w)
ww = perceptron.w/n
ww1 = [ww[1],-ww[0]]
ww2 = [-ww[1],ww[0]]
#plot([ww1[0], ww2[0]],[ww1[1], ww2[1]],'--k')
show()

