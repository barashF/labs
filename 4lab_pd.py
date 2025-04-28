import pandas as pd
import numpy as np

# Загрузка данных с указанием кодировки
df = pd.read_csv('spotify-2023.csv', encoding='latin-1')

# ---------------------------------------------------------------
# 1. Анализ популярности треков по годам
# ---------------------------------------------------------------

# Преобразуем колонку 'streams' в числовой формат (ошибки -> NaN)
df['streams'] = pd.to_numeric(df['streams'], errors='coerce')

# Удаляем строки с NaN в 'streams' и 'released_year'
df = df.dropna(subset=['streams', 'released_year'])

# Преобразуем год в целое число
df['release_year'] = df['released_year'].astype(int)

# Группировка по году и вычисление среднего
yearly_streams = df.groupby('release_year')['streams'].mean().reset_index()
yearly_streams_sorted = yearly_streams.sort_values('release_year')
print("Средние потоки по годам:\n", yearly_streams_sorted)

# ---------------------------------------------------------------
# 2. Треки во всех плейлистах и чартах
# ---------------------------------------------------------------

# Проверяем, что колонки содержат бинарные значения (1/0)
# Если данные хранятся как строки, преобразуем их в числа:
for col in ['in_spotify_playlists', 'in_apple_playlists', 'in_deezer_playlists', 'in_shazam_charts']:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

# Фильтрация
condition = (
    (df['in_spotify_playlists'] == 1) &
    (df['in_apple_playlists'] == 1) &
    (df['in_deezer_playlists'] == 1) &
    (df['in_shazam_charts'] == 1)
)
popular_tracks = df[condition][['track_name', 'artist(s)_name']]
print("\nТреки во всех сервисах:\n", popular_tracks)

# ---------------------------------------------------------------
# 3. Топ-10 по акустичности и инструментальности
# ---------------------------------------------------------------

# Убедимся, что колонки имеют числовой формат
df['acousticness_%'] = pd.to_numeric(df['acousticness_%'], errors='coerce')
df['instrumentalness_%'] = pd.to_numeric(df['instrumentalness_%'], errors='coerce')

# Сортировка и выбор топ-10
sorted_df = df.sort_values(
    ['acousticness_%', 'instrumentalness_%'],
    ascending=False
)
top_10 = sorted_df.head(10)[['track_name', 'artist(s)_name', 'acousticness_%', 'instrumentalness_%']]
print("\nТоп-10 треков:\n", top_10)

# ---------------------------------------------------------------
# 4. Категории BPM
# ---------------------------------------------------------------

# Преобразуем BPM в числовой формат
df['bpm'] = pd.to_numeric(df['bpm'], errors='coerce')

# Создаем категории
bins = [0, 90, 120, 150, np.inf]
labels = ['0-90', '91-120', '121-150', '151+']
df['bpm_category'] = pd.cut(df['bpm'], bins=bins, labels=labels)

# Вычисляем статистику
bpm_stats = df.groupby('bpm_category')[['danceability_%', 'energy_%']].mean()
print("\nСтатистика по BPM:\n", bpm_stats)