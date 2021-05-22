from sklearn.cluster import KMeans
import numpy as np

### The dataset
features = np.array([[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]], np.float64)
print("#------------------------------------------------------------------------------------------>")
print ("Features")
print (features)

### Initial centroid of each cluster 
centroids = np.array([[2, 10], [5, 8], [1, 2]], np.float64)
print("#------------------------------------------------------------------------------------------->")
print("Initial Centroids")
print(centroids)

### Constant variables
NUM_CLUSTERS = 3         # k
NUM_ITER = 3          	 # n
###NUM_ATTEMPTS = 5      # m

### Set the algorithm parameters before fitting the estimator to the data
kmeans = KMeans(init = centroids, n_clusters=NUM_CLUSTERS, n_init=1)

### Fit the model
kmeans.fit(features)

print("#------------------------------------------------------------------------------------------->")
print("The lowest SSE value")
print(kmeans.inertia_)

### Print to file
fo = open('results.txt', 'w')

print("#------------------------------------------------------------------------------------------->")
print("Final locations of the centroids")
fo.write("Iteration: 1")
fo.write('\n')
print(kmeans.cluster_centers_)
fo.write('Centriod: ')
content = str(kmeans.cluster_centers_) 
fo.write(content)
fo.write('\n')


print("#------------------------------------------------------------------------------------------->")
print("The number of iterations required to converge")
print(kmeans.n_iter_)
NUM_ITER = kmeans.n_iter_

print("#------------------------------------------------------------------------------------------->")
print("Here are the predicted labels")
print(kmeans.labels_)

final_cents = []
final_inert = []
    
for sample in range(2, NUM_ITER):
	print('\nCentroid attempt: ', sample)
	fo.write('Iteration: ')
	fo.write(str(iter))
	fo.write('\n')
	kmeans = KMeans(n_clusters=NUM_CLUSTERS, init=centroids, max_iter=1, n_init=1)#, verbose=1) 
	kmeans.fit(features)
	inertia_start = kmeans.inertia_
	intertia_end = 0
	cents = kmeans.cluster_centers_
        
	for iter in range(NUM_ITER):
		kmeans = KMeans(n_clusters=NUM_CLUSTERS, init=centroids, max_iter=1, n_init=1)
		kmeans.fit(features)
		print('Iteration: ', iter)
		print('Inertia:', kmeans.inertia_)
		print('Centroid: ', kmeans.cluster_centers_)
		fo.write('Centroid: ')
		content = str(kmeans.cluster_centers_) 
		fo.write(content)
		fo.write('\n')
		inertia_end = kmeans.inertia_
		cents = kmeans.cluster_centers_

		final_cents.append(cents)
		final_inert.append(inertia_end)
		print('Difference between initial and final inertia: ', inertia_start-inertia_end)		

### Close	
fo.close()
