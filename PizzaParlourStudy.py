# Importing essential Libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

print('Start')
""" Choose the value of k which is the number of 
	Centers you want in your data """
print("Enter the number of Center you want in the data:",end=" ")
K = int(input())

# Preparing data
X,y = make_blobs(n_samples=500,n_features=2,centers=5,random_state=1)

""" To check the Shape of data generated 
	data Uncomment the following lines
	print(X.shape)
	print(y.shape)	"""

# Plotting the data to get visual idea
print("Original data Plot")
plt.figure(0)
plt.scatter(X[:,0],X[:,1])
plt.figure(1)
class Kmeans():

	def __init__(self,X,K):
		clusters = {}
		self.K = K
		self.data = X

	# Calculate the distance between two points(Vectors)
	def distance(self,v1,v2):
    	
		return np.sqrt(np.sum((v1 - v2)**2))

	""" Preparing a dictionary called clusters for K keys and assinging them propreties given below
	properties - Cetre coordinates, Points coordinates that came under the blob
	and color to assign while plotting the cluster """
	def make_cluster(self):
	    
	    """ K must not be greater than 10 Otherwise this will go out of bound """ 
	    colors = ['red','blue','pink','yellow','violet','green','cyan','magenta','black','white']
	    self.clusters = {}
	    for kx in range(self.K):
	        
	        center = X[np.random.randint(0,self.K + 1)]
	        color = colors[kx]

	        points = []
	        cluster = {

	            'points' : points,
	            'center' : center,
	            'color' : color
	        }
	        self.clusters[kx] = cluster

	# Function to Assign the points to the specific cluster
	def AssignPoints(self):
	    
	    for kx in range(self.K):
	        self.clusters[kx]['points'] = []
	        
	    for ix in range(self.data.shape[0]):

	        curr_point = self.data[ix]
	        dist = []
	        for kx in range(K):

	            d = self.distance(curr_point,self.clusters[kx]['center'])
	            dist.append(d)

	        current_cluster = np.argmin(dist)
	        self.clusters[current_cluster]['points'].append(curr_point)

	# Function to update the previous centers
	def UpdateCenter(self):
	    
	    old_centers = []
	    for kx in range(self.K):
	        
	        pts = np.array(self.clusters[kx]['points'])
	        
	        if pts.shape[0] > 0:
	        
	            new_center = pts.mean(axis=0)
	            old_centers.append(self.clusters[kx]['center'])
	            self.clusters[kx]['center'] = new_center

	    return old_centers

	# Function to plot the clusters along with their color and their center
	def plot_cluster(self):
	    

	    for kx in range(self.K):
	        
	        pts = np.array(self.clusters[kx]['points'])
	        
	        try:
	            plt.scatter(pts[:,0],pts[:,1],color=self.clusters[kx]['color'])
	        except:
	            pass
	        
	        center = self.clusters[kx]['center']
	        plt.scatter(center[0],center[1],color='black',marker="*")

	""" Main Fucntion to call all the other function and Plot the corresponding centers 
    as it achieves Saturation """

	def Predict(self,epochs = 30,min_value=0.01):
	    
	    self.make_cluster()
	    self.AssignPoints()
	    diff = 0
	    count = 0
	    
	    while count < epochs:        
	        is_saturated = True
	        old_centers = self.UpdateCenter()

	        for kx in range(self.K):
	            new_center = self.clusters[kx]['center']
	            old_center = old_centers[kx]
	            dist = self.distance(old_center,new_center)
	            
	            if dist > min_value:
	                is_saturated = False
	                break

	        if is_saturated is False:
	            self.AssignPoints()
	        else:
	            break
	        
	        count += 1
	    new_centers = []

	    for kx in range(self.K):
	    	new_centers.append(self.clusters[kx]['center'])

	    return new_centers

# Creating Object of the given class
classifier = Kmeans(X,K)

# Final Centers will be available as new_centers
new_centers = classifier.Predict()

# Plotting the final graph
classifier.plot_cluster()

# Showing the plotted Graph
plt.show()

#Thanks for Studying the Code.... :) Happy Coding!!!
print("End")