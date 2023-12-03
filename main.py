from shimoku_client import client
from pipeline import (
    df_cleaned,
    top_streams, 
    top_artists, 
    song_counts_by_year, 
    songs_by_month, 
    songs_by_day,
    scatter_source
    
)


#Menu: Data Table

client.set_menu_path('Data Table')

client.plt.table(
    data=df_cleaned, order=0, 
    title="Review Registers of Most Streamed Spotify Songs 2023",
    page_size_options=[3,5, 10]
)


#Menu: Data Analysis

client.set_menu_path('Top Features')

client.plt.horizontal_bar(
    data=top_streams, x='track_name', y='streams', order=0,
    title='Top 10 Songs with Most Streams on Spotify', 
    x_axis_name='Streams (in billions)', y_axis_name='Track Name',
    cols_size= 12
)

client.plt.horizontal_bar(
    data=top_artists, x='artist', y='count', order=1,
    title='Top 5 Artists with Most Songs', 
    x_axis_name='Nmber of songs', y_axis_name='Artist(s) Name',
    cols_size= 12
)

client.plt.line(
    data=song_counts_by_year, order=2, x='year',
    rows_size=2, cols_size=12,
    x_axis_name='Year', y_axis_name='Numbers of Songs Released',
    title='Evolution of Songs Released on Spotify (2018-2023)'
)


client.plt.bar(
    data=songs_by_month, x='month', y='count', order=3,
    title='Distribution of Songs by Month', 
    x_axis_name='Month', y_axis_name='Number of Songs Released',
    cols_size= 6
)

client.plt.bar(
    data=songs_by_day, x='day', y='count', order=4,
    title='Distribution of Songs by Day', 
    x_axis_name='Day', y_axis_name='Number of Songs Released',
    cols_size= 6
)

"""
#Problems 
client.plt.scatter_with_effect(
    data= scatter_source, x='x', y='y', order=5, 
    x_axis_name='Number of Spotify Playlists', y_axis_name='Total Number of Streams',
    title='Correlation between Spotify Playlists and Streams (Correlation Coefficient: 0.79)'
)
"""
