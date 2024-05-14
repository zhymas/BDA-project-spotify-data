import pandas as pd
import matplotlib.pyplot as plt

track_df = pd.read_csv('spotify_tracks.csv')

print("General information about the data:")
print(track_df.info())

print("\nTrack popularity statistics:")
print(track_df['popularity'].describe())

print("\nMost popular tracks:")
print(track_df.sort_values(by='popularity', ascending=False).head(10))

artist_counts = track_df['artist'].value_counts().head(10)

plt.figure(figsize=(10, 6))
artist_counts.plot(kind='bar', color='green')
plt.title('Top 10 Artists by Number of Tracks')
plt.xlabel('Artist')
plt.ylabel('Number of Tracks')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(track_df['duration_ms'] / 1000, bins=20, color='salmon', edgecolor='black')
plt.title('Distribution of Track Duration')
plt.xlabel('Duration (seconds)')
plt.ylabel('Number of Tracks')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(track_df['duration_ms'] / 1000, track_df['popularity'], color='purple', alpha=0.5)
plt.title('Track Popularity vs. Duration')
plt.xlabel('Duration (seconds)')
plt.ylabel('Popularity')
plt.show()
