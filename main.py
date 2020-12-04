from pygame import mixer
from mutagen.mp3 import EasyMP3
import os
import time
# créer une playlist à partir de critères divers (artiste, année, etc.), (Georges, Loic, Youlan) 
 
def generate_playlist(name, music_list, filter_type, artist = None, year = None, genre = None):
    """generate a playlist according to the user's choice
    Parameters
    ----------
    name: name of the playlist (str)
    music_list: List of dictionnaries containing all stored songs (list)
    filter_type: Can be "including" or "specific" details in the notes (str)
    artist: name of a chosen artist (str, optional)
    year: a chosen year (int, optional)
    genre: a chosen genre (str, optional)

    Notes
    -----
    If filter_type is set to "including" every song corresponding to at least one of the filter will be added to the playlist.
    At the opposite if filter_type is set to "specific" only the songs matching all filters will be added to the playlist.
    If no optional parameters are filled the playlist will not conain any song in the case of including filters but will contain all songs in case of specific filters.

    Version
    -------
    specification: Hoebrechts Georges, Collard Youlan (v.1 01/12/20)
    implementation: Collard Youlan (v.1 01/12/20)
    """

    if not os.path.exists('.\\Playlists'):
        os.mkdir('.\\Playlists')

    playlist = []
    if filter_type == 'specific':
        for song in music_list:
            if (artist in song['artist'] or artist == None) and (year == song['year'] or year == None) and (genre == song['genre'] or genre == None):
                playlist.append(song)

    elif filter_type == 'including':
        for song in music_list:
            if artist in song['artist']:
                playlist.append(song)
            elif year == song['year']:
                playlist.append(song)
            elif genre == song['genre']:
                playlist.append(song)

    if len(playlist) != 0:
        fh = open('.\\Playlists\\%s.txt' % name, 'w')
        song_str_list = []
        for song in playlist:
            song_str_list.append('%s -- %s' % (song['albumartist'], song['title']))
        fh.write(concatenate(song_str_list, '\n'))
        fh.close()
    else:
        print('Your playlist is empty and hasn\'t been created')
            


        
 
# afficher le nom de toutes les playlists disponibles, (Georges, Loic, Youlan) 
 
def show_all_playlist():
    """show every playlist created by the user
    
    Version
    -------
    specification: Hoebrechts Georges (v.1 01/12/20)
    implementation: Adam Loïc (v.1 04/12/20)
    """ 
    list_playlist = os.listdir("./Playlists")

    for playlist in list_playlist:
        print(playlist)
 
# afficher les morceaux contenus dans une playlist, (Georges, Loic, Youlan, P-A) 
 
def show_content_playlist(playlist):
    """show the content of a playlist created by the user
    Parameters
    ----------
    playlist : name of the playlist (str)
    
    Version
    -------
    specification: Hoebrechts Georges (v.1 01/12/20)
    implementation: 
    """
    fh = open('.\\Playlists\%s.txt' % playlist, 'r')
    lines = fh.readlines()

    for line in lines:
        artist, title = line.split(' -- ')
        print('%s - %s' % (artist, title))
    
    fh.close()
 
# lire une playlist du début à la fin (appel « bloquant »). (Georges, Loic, Youlan) 
 
def read_playlist(music_list, name):
    """read every song contained in a playlist

    Parameters
    ----------
    music_list: list of all musics (list)
    name : name of the playlist (str)

    Version
    -------
    specification: Hoebrechts Georges (v0.1), Hoebrechts Georges (v0.2)
    implementation: Hoebrechts Georges
    """
    # open playlist file according to it's name and read content + ? initialise ?

    fh = open('./Playlists/%s.txt' % name, 'r')

    lines = fh.readlines()

    # play music in the playlist + ? block ?

    for line in lines:
        artist_and_title = str.split(line, ' -- ')
        artist = artist_and_title[0]
        title = artist_and_title[1]

        play_music(music_list, title, artist)

    #close playlist file

    fh.close()

def concatenate(word_list, separator=''):
    """Concatenate word from a list to a string
    
    Parameters
    ----------
    word_list: a list of words (list)
    seperator: Seperator to put between the items to concatenate (str, optional)
    
    Returns
    -------
    string: the elements of word_list (str)

    Notes
    -----
    This function is not meant to be called directly by the end user

    Version
    -------
    specification: Aliti Dzenetan, Collard Youlan (v.1 02/12/20)
    implementation: Aliti Dzenetan, Collard Youlan (v.1 02/12/20)
    """
    #function used instead of str.join()
    string = ''
    for index, word in enumerate(word_list):
        string += word
        if not index == len(word_list) - 1:
            string += separator
    return string

def sort_music(dir_extract_path):
    """Extract music files from a directory and sort them into authors directory and album sub-directory
    
    Parameters
    ----------
    dir_path: path to directory containing the music files to sort (str)
    
    Returns
    -------
    list_of_music_dict: list containing all musics and their infos (list)

    Notes
    -----
    create a file with informations in format title;artist;albumartist;year;album;track_number;genre;\n in  .txt file for each song
    
    Version
    -------
    specification: Aliti Dzenetan (v.1 01/12/20)
    implementation: Aliti Dzenetan (v.1 02/12/20)
    """
    
    list_of_music_dict = []
    dir_list = os.listdir(dir_extract_path)
    for direc in dir_list: 
       
        dir_path = dir_extract_path +'\\'+direc 

        if os.path.isdir(dir_path): 
            song_list = os.listdir(dir_path)
            
            for song in song_list:
                
                song_path = dir_path+'\\'+song
                song_info = EasyMP3(song_path)
                
                #checking if the 'genre' exists
                if 'genre' in song_info:
                    genre = song_info['genre'][0]
                else:
                    genre = ' '

                #removing '/' and ':' from the title, album and name (to allow us to create valid paths)
                #we didn't use re.split (regex) to split on multiple delimiters because we haven't seen it in course yet
                title = concatenate(song_info['title'][0].split('/'))           
                title = concatenate(title.split(':'))                               
                album = concatenate(song_info['album'][0].split('/'))
                album = concatenate(album.split(':'))
                artists = []
                for artist in song_info['artist']
                    artist = concatenate(artist.split('/'))
                    artist = concatenate(artist.split(':'))
                    artists.append(artist)

                song_ref = {
                    'title': title,
                    'artist': artists,
                    'albumartist': song_info['albumartist'][0],
                    'year': song_info['date'][0].split('-')[0],
                    'album': album,
                    'track_number': song_info['tracknumber'][0],
                    'genre': genre
                }                
                list_of_music_dict.append(song_ref)

                path = '.\\audio'+'\\'+song_ref['artist']

                #creating directories artist/album for files if it doesn't exists 
                if not os.path.exists('.\\audio'):
                    os.mkdir('.\\audio')
                if not os.path.exists(path):
                    os.mkdir(path)
                path += '\\'+song_ref['album']               
                if not os.path.exists(path):
                    os.mkdir(path)
                
                new_path = path+'\\'+song_ref['track_number']+'. '+ song_ref['title']+' '+'('+ song_ref['year']+').mp3'
                
                
                os.rename(song_path, new_path)
    
    fh = open('.\\dicti.txt', 'w')
    for dic in list_of_music_dict:
        for key in dic:
            if key == 'artist':
                fh.write(contatenate(dic['artist'], ','))
            else:
                fh.write(dic[key] + ';')
        fh.write('\n')
    fh.close()   

    return list_of_music_dict

def information_dict(file_path):
    """Store music information from a file to a list of dictionnaries
    
    Parameters
    ----------
    file_path: path to the file listing music informations (str)
    
    Returns
    -------
    list_of_music_dict: list containing dictionnaries with music informations (list)

    Notes
    -----
    the infos about music is written in format title;artist;albumartist;year;album;track_number;genre;\n in the .txt file

    Version
    -------
    specification: Aliti Dzenetan (v.1 01/12/20)
    implementation: Aliti Dzenetan (v.1 02/12/20)
    """         
    list_of_music_dict = []
    fh = open(file_path, 'r')
    for line in fh.readlines():
        info = line.split(';')
        song_ref = {
            'title': info[0],
            'artist': info[1].split(','),
            'albumartist': info[2],
            'year': info[3],
            'album': info[4],
            'track_number': info[5],
            'genre':info[6]
        }
        list_of_music_dict.append(song_ref)

    fh.close()
    return list_of_music_dict

def show_all_music(path_to_txt):
    """Display all the music files contained in a directory and its subdirectories.
    
    Parameters
    ----------
    path_to_txt: path to the txt file containing all infos (str)
    
    Version
    -------
    specification: Aliti Dzenetan (v.1 01/12/20)
    implementation: Aliti Dzenatan (v.1 02/12/20)
    """
    songs_ref = information_dict(path_to_txt)
    print('The following songs are available :\n')
    for elem in songs_ref:
        print('%s from artist %s in album %s' % (elem['title'], concatenate(elem['artist'],', '), elem['album']))


def play_music(music_list, title, artist):
    """Play music from start to finish

    Parameters
    ----------
    mucic_list: List containing all songs
    title: Title of the song to play
    artist: Artist of the song to play
    
    ".\\audio\\artist\\album\\01. Titre (année)"

    Version
    -------
    specification: Dadzie Reeckel, Collard Youlan (v.1 01/12/20)
    implementation: Dadzie Reeckel
    """
    pass

mixer.init()

_data_structures = [
    {
        'title': 'title',
        'artist': ['artist'],
        'albumartist': 'artist',
        'year': 2014,
        'album': 'dfdff',
        'track_number': '01',
        'genre': 'Rock'
    },
    {
        'title': 'title2',
        'artist': ['artist2'],
        'albumartist': 'artist2',
        'year': 2015,
        'album': 'gfdiuovjfdi',
        'track_number': '02',
        'genre': 'Jazz'
    }
]

_list = information_dict("./dicti.txt")
print(_list)
generate_playlist("Test", _list, 'including', genre='Rock')