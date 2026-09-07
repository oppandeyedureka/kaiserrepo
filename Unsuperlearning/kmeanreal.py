import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import numpy as np

# Sample data
data = {
    'CustomerID': range(1, 31),
    'Age': [25, 28, 30, 32, 35, 38, 40, 42, 45, 48, 50, 52, 55, 58, 60, 23, 26, 29, 31, 34, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54],
    'Annual Income (k$)': [250, 260, 280, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 80, 90, 100, 110, 120, 250, 270, 290, 310, 330, 350, 370, 390, 410, 430],
    'Spending Score (1-100)': [20, 22, 25, 38, 20, 22, 25, 28, 30, 32, 35, 38, 40, 42, 45, 85, 87, 88, 89, 40, 50, 52, 55, 58, 60, 62, 65, 68, 70, 72]
}

df = pd.DataFrame(data)
X = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Use 3 clusters
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, init='k-means++', max_iter=300, n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(X_scaled)

# Visualization
fig, ax = plt.subplots(figsize=(10, 6))

# Cluster visualization
colors = plt.cm.Set3(np.linspace(0, 1, optimal_k))
for i in range(optimal_k):
    ax.scatter(X_scaled[y_kmeans == i, 0], X_scaled[y_kmeans == i, 1], 
                s=100, c=[colors[i]], label=f'Cluster {i+1}')
ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            s=300, c='red', marker='X', label='Centroids')
ax.set_title(f'Customer Segments (k={optimal_k})')
ax.set_xlabel('Age (Standardized)')
ax.set_ylabel('Annual Income (Standardized)')
ax.legend()
ax.grid()

plt.tight_layout()
plt.show()

df['Cluster'] = y_kmeans
print(df.groupby('Cluster').agg({'Age': 'mean', 'Annual Income (k$)': 'mean', 'Spending Score (1-100)': 'mean'}))
