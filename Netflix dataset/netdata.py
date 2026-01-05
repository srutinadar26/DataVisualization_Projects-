import pandas as pd
import matplotlib.pyplot as plt

# Load the Netflix dataset
df = pd.read_csv('netflix_titles.csv')

# clean the data : remove rows with missing values in critical columns, and removes duplicate rows
df = df.dropna(subset=['release_year', 'type', 'duration', 'country', 'rating'])

# df['type'], selects the type column from the DataFrame
#This column contains values like: "Movie" and "Tv Show"

type_counts = df['type'].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(type_counts.index, type_counts.values, color=['skyblue', 'salmon'])
plt.title('Distribution of Content Types on Netflix')
plt.xlabel('Content Type')
plt.ylabel('Number of Titles')
plt.savefig('netflix_content_types_bar_chart.png')
plt.show()

rating_counts = df['rating'].value_counts().head(10)
plt.figure(figsize=(10, 6)) # --> (width, height)
plt.pie(rating_counts.values, labels=rating_counts.index, autopct='%1.1f%%', startangle=140)
# values = numerical data
plt.title('Top 10 Content Ratings on Netflix')
plt.xlabel('Content Rating')
plt.ylabel('Number of Titles')
plt.savefig('netflix_ratings_pie_chart.png')
plt.show()

movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration'] = movie_df['duration'].str.replace(' min', '').astype(int)
plt.figure(figsize=(10, 6))
plt.hist(movie_df['duration'], bins=30, color='lightgreen', edgecolor='black')
plt.title('Distribution of Movie Durations on Netflix')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.savefig('netflix_movie_durations_histogram.png')
plt.show()

release_year_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
plt.plot(release_year_counts.index, release_year_counts.values, color='purple')
plt.title('Number of Titles Released Over the Years on Netflix')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.savefig('netflix_release_years_line_plot.png')
plt.show()

country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(10, 6))
plt.barh(country_counts.index, country_counts.values, color='orange')
plt.title('Top 10 Countries by Number of Titles on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.savefig('netflix_top_countries_bar_chart.png')
plt.show()

# fiest subplot : movies
content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)
fig, ax = plt.subplots(1,2, figsize=(12,5))
ax[0].plot(content_by_year.index, content_by_year['Movie'], color = 'blue')
ax[0].set_title('Movies released every year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

# fiest subplot : TV shows
content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)
fig, ax = plt.subplots(1,2, figsize=(12,5))
ax[1].plot(content_by_year.index, content_by_year['TV Show'], color = 'salmon')
ax[1].set_title('TV shows released every year')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of TV shows')

fig.suptitle("Comparision of movies and TV shows over the years")
plt.tight_layout()
plt.savefig("moviestvshows_comparision.png")
plt.show()

