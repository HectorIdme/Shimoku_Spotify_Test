import pandas as pd

#Reading Data
df = pd.read_csv('dataset/spotify-2023.csv',encoding='latin-1')


#df.info()
#df.describe()

#Convert data type of columns
df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
df['in_deezer_playlists'] = pd.to_numeric(df['in_deezer_playlists'], errors='coerce')
df['in_shazam_charts'] = pd.to_numeric(df['in_shazam_charts'], errors='coerce')
df_convert = df.to_dict(orient='records')

#print(df.isna().sum())
#print("\nDuplicated rows: ",df.duplicated().sum())

#Data Cleaning
df['in_shazam_charts'].fillna('0',inplace=True)
df['in_deezer_playlists'].fillna('0',inplace=True)
df['in_deezer_playlists'] = df['in_deezer_playlists'].astype('int')
df['key'].fillna('-',inplace=True)
df.dropna(inplace=True)

#Get data for Table
df_cleaned = df.head()
df_cleaned = df_cleaned.to_dict(orient='records')


#Get top 10 songs with most streams on Spotify
top_streams = df[['track_name', 'artist(s)_name', 'streams']].sort_values(by='streams', ascending=False).head(10)
top_streams = top_streams.to_dict(orient='records')


#Get top 5 artistswith most songs
top_artists = df['artist(s)_name'].value_counts().head(5)
top_artists = top_artists.reset_index()
top_artists.columns = ['artist', 'count']
top_artists = top_artists.to_dict(orient='records')


#Filtering out data of between 2018 and 2023
filtered_data = df[(df['released_year'] >= 2018) & (df['released_year'] <= 2023)]
song_counts_by_year = filtered_data['released_year'].value_counts().sort_index()
song_counts_by_year = song_counts_by_year.reset_index()
song_counts_by_year.columns = ['year','count']

#Distribution of Songs Released By Month
songs_by_month = df.groupby('released_month')['track_name'].count().reset_index()
songs_by_month.columns = ['month','count']
songs_by_month = songs_by_month.to_dict(orient='records')

#Distribution of Songs Released By Day
songs_by_day = df.groupby('released_day')['track_name'].count().reset_index()
songs_by_day.columns = ['day','count']
songs_by_day = songs_by_day.to_dict(orient='records')


#Correlation between Spotify Playlist and Streams
correlation = df['in_spotify_playlists'].corr(df['streams'])
df_correlations = df.head(20)
x_values = df_correlations['in_spotify_playlists'].values
y_values = df_correlations['streams'].values

#points_correlation_spotify_streams = [list(pair) for pair in zip(x_values, y_values)]
scatter_source = pd.DataFrame({'x': x_values, 'y': y_values})
#data = pd.DataFrame({'x': x_values, 'y': y_values})
#print(data)