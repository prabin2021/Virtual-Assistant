import pandas as pd

# Sample movie ratings data (user_id, movie_id, rating)
data = {
    'user_id': [1, 1, 1, 2, 2],
    'movie_id': ['A', 'B', 'C', 'B', 'C'],
    'rating': [5, 4, 3, 4, 5]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Calculate the mean rating for each movie
movie_ratings = df.groupby('movie_id')['rating'].mean().reset_index()

# Recommend top-rated movies to a user
def recommend_movies(user_id, top_n=3):
    user_movies = df[df['user_id'] == user_id]['movie_id']
    recommended_movies = movie_ratings[~movie_ratings['movie_id'].isin(user_movies)]
    return recommended_movies.sort_values(by='rating', ascending=False).head(top_n)

# Example: Recommend movies for user_id 1
user_id = 1
recommendations = recommend_movies(user_id)
print("Recommendations for user", user_id, ":")
print(recommendations)
