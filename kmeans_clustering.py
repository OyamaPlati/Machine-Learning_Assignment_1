from sklearn.cluster import KMeans
import numpy as np

### The dataset
features = np.array([[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]], np.float64)

### Initial centroid of each cluster 
centroids = np.array([[2, 10], [5, 8], [1, 2]], np.float64)

### Set the algorithm parameters before fitting the estimator to the data
kmeans = KMeans(init = centroids, n_clusters=3, n_init=1)

### Fit the model
kmeans.fit(features)

### Print to file
fo = open('results.txt', 'w')

fo.write("Iteration: 1")
fo.write('\n')
fo.write('Centriod: ')
content = str(kmeans.cluster_centers_) 
fo.write(content)
fo.write('\n')

NUM_ITER = kmeans.n_iter_
NUM_CLUSTERS = 3
    
for sample in range(2, NUM_ITER):
	fo.write('Iteration: ')
	fo.write(str(sample))
	fo.write('\n')
        
	for iter in range(NUM_ITER):
		kmeans = KMeans(n_clusters=NUM_CLUSTERS, init=centroids, max_iter=1, n_init=1)
		kmeans.fit(features)
		fo.write('Centroid: ')
		content = str(kmeans.cluster_centers_) 
		fo.write(content)
		fo.write('\n')	

### Close	
fo.close()
