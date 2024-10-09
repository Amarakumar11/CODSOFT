import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist, squareform # type: ignore

# Sample data
data = {
    'User ID': [1, 1, 2, 2, 3, 3],
    'Movie ID': [101, 102, 101, 103, 102, 104],
    'Rating': [5, 3, 4, 2, 4, 5]
}

df = pd.DataFrame(data)

# Create user-item matrix
user_item_matrix = df.pivot(index='User ID', columns='Movie ID', values='Rating')

# Fill NaN with 0 for similarity calculations
user_item_matrix = user_item_matrix.fillna(0)

# Convert DataFrame to numpy array
user_item_matrix_array = user_item_matrix.values

# Calculate cosine similarity matrix using scipy
distance_matrix = pdist(user_item_matrix_array, metric='cosine')
similarity_matrix = 1 - squareform(distance_matrix)
np.fill_diagonal(similarity_matrix, 0)  # Don't use self-similarity

# Predict ratings
def predict_ratings(user_id, user_item_matrix, similarity_matrix):
    user_index = user_item_matrix.index.get_loc(user_id)
    sim_scores = similarity_matrix[user_index]
    user_ratings = user_item_matrix.iloc[user_index].values
    
    # Calculate weighted ratings
    sim_sum = np.sum(np.abs(sim_scores))
    if sim_sum == 0:
        return np.zeros(user_item_matrix.shape[1])
    
    weighted_ratings = np.dot(sim_scores, user_item_matrix.fillna(0).values)
    predicted_ratings = weighted_ratings / sim_sum
    return predicted_ratings

# Example: Predict ratings for User 1
user_id = 1
predicted_ratings = predict_ratings(user_id, user_item_matrix, similarity_matrix)
predicted_ratings_df = pd.DataFrame(predicted_ratings, index=user_item_matrix.columns, columns=['Predicted Rating'])
print(predicted_ratings_df)
