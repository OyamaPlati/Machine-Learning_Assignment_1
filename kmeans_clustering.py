from sklearn.cluster import KMeans
import numpy as np

### The dataset
features = np.array([[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]], np.float64)

### Initial centroid of each cluster 
centroids = np.array([[2, 10], [5, 8], [1, 2]], np.float64)

### Print to file
fo = open('results.txt', 'w')

N = 3
    
for iter in range(1, N):
	fo.write('Iteration: ')
	fo.write(str(iter))
	fo.write('\n')
	kMeans = KMeans(n_clusters=N, init=centroids, max_iter=1, n_init=1)
	        
	for cluster in range(N):
		kMeans.fit(features)
		intermediate_centers = kMeans.cluster_centers_
		fo.write('Cluster: ' + str(cluster))
		fo.write('\n')
		fo.write('Centroid: \n')
		fo.write(str(intermediate_centers))
		fo.write('\n')
		kMeans = KMeans(n_clusters=N, init=intermediate_centers, max_iter=1, n_init=1)	

### Close	
fo.close()
