import pandas as pd
import numpy as np

df = pd.read_csv('spotify-2023.csv', encoding='latin-1')

df['streams'] = pd.to_numeric(df['streams'], errors='coerce')

df = df.dropna(subset=['streams', 'released_year'])

df['release_year'] = df['released_year'].astype(int)

yearly_streams = df.groupby('release_year')['streams'].mean().reset_index()
yearly_streams_sorted = yearly_streams.sort_values('release_year')
print("Средние потоки по годам:\n", yearly_streams_sorted)

for col in ['in_spotify_playlists', 'in_apple_playlists', 'in_deezer_playlists', 'in_shazam_charts']:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

condition = (
    (df['in_spotify_playlists'] == 1) &
    (df['in_apple_playlists'] == 1) &
    (df['in_deezer_playlists'] == 1) &
    (df['in_shazam_charts'] == 1)
)
popular_tracks = df[condition][['track_name', 'artist(s)_name']]
print("\nТреки во всех сервисах:\n", popular_tracks)

df['acousticness_%'] = pd.to_numeric(df['acousticness_%'], errors='coerce')
df['instrumentalness_%'] = pd.to_numeric(df['instrumentalness_%'], errors='coerce')

sorted_df = df.sort_values(
    ['acousticness_%', 'instrumentalness_%'],
    ascending=False
)
top_10 = sorted_df.head(10)[['track_name', 'artist(s)_name', 'acousticness_%', 'instrumentalness_%']]
print("\nТоп-10 треков:\n", top_10)

df['bpm'] = pd.to_numeric(df['bpm'], errors='coerce')

bins = [0, 90, 120, 150, np.inf]
labels = ['0-90', '91-120', '121-150', '151+']
df['bpm_category'] = pd.cut(df['bpm'], bins=bins, labels=labels)

bpm_stats = df.groupby('bpm_category')[['danceability_%', 'energy_%']].mean()
print("\nСтатистика по BPM:\n", bpm_stats)