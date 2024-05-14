import pandas as pd

track_df = pd.read_csv('spotify_tracks.csv')

print("General information about the data:")
print(track_df.info())

print("\nTrack popularity statistics:")
print(track_df['popularity'].describe())

print("\nMost popular tracks:")
print(track_df.sort_values(by='popularity', ascending=False).head(10))
