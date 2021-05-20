import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import numpy as np

### The dataset
features = np.array([[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]], np.float64)
print("#------------------------------------->")
print (features)

### Apply feature scaling to the dataset
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
print("#-------------------------------------->")
print(scaled_features)

### Initial centroid of each cluster 
centroids = np.array([[2, 10], [5, 8], [1, 2]], np.float64)

