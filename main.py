from pygame import mixer
from mutagen.mp3 import EasyMP3
import os
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
    If no optional parameters are filled the playlist will contain every single song.

    Version
    -------
    specification: Hoebrechts Georges, Collard Youlan (v .1 01/12/20)
    implementation: Collard Youlan (v .1 01/12/20)
    """

    if not os.path.exists('./Playlists'):
        os.mkdir('./Playlists')

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
        fh = open('./Playlists/%s.txt' % name, 'w')
        song_str_list = []
        for song in playlist:
            song_str_list.append('%s - %s' % (song['albumartist'], song['title']))
        fh.write(concatenate(song_str_list, '\n'))
        fh.close()
    else:
        print('Your playlist is empty and hasn\'t been created')
            


        
 
# afficher le nom de toutes les playlists disponibles, (Georges, Loic, Youlan) 
 
def show_all_playlist():
    """show every playlist created by the user
    
    Version
    -------
    specification: Hoebrechts Georges (v0.1)
    implementation: Adam Loïc
    """ 
    raise NotImplementedError()
 
# afficher les morceaux contenus dans une playlist, (Georges, Loic, Youlan, P-A) 
 
def show_content_playlist(playlist):
    """show the content of a playlist created by the user
    Parameters
    ----------
    playlist : name of the playlist (str)
    
    Version
    -------
    specification: Hoebrechts Georges (v0.1)
    implementation: 
    """    
    raise NotImplementedError()
 
# lire une playlist du début à la fin (appel « bloquant »). (Georges, Loic, Youlan) 
 
def read_playlist(playlist):
    """read every song contained in a playlist
    Parameters
    ----------
    playlist : name of the playlist (str)
    
    Version
    -------
    specification: Hoebrechts Georges (v0.1)
    implementation: Hoebrechts Georges
    """
    raise NotImplementedError() 

def concatenate(word_list, separator=''):
    """Concatenate word from a list to a string
    
    Parameters
    ----------
    word_list: a list of words (list)
    seperator: Seperator to put between the items to concatenate (str, optional)
    
    Returns
    -------
    string: the elements of word_list (str)

    Version
    -------
    specification: Aliti Dzenetan, Collard Youlan (v0.1 02/12/20)
    implementation: Aliti Dzenetan, Collard Youlan (v0.1 02/12/20)
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
    list_of_music_dict: dictionnary containing all musics and their infos (dict)

    Notes
    -----
    create a file with informations in format title;artist;albumartist;year;album;track_number;genre;\n in  .txt file for each song
    
    Version
    -------
    specification: Aliti Dzenetan (v0.1)
    implementation: Aliti Dzenetan
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
                artist = concatenate(song_info['artist'][0].split('/'))
                artist = concatenate(artist.split(':'))

                dicti = {
                    'title': title,
                    'artist': artist,
                    'albumartist': song_info['albumartist'][0],
                    'year': song_info['date'][0].split('-')[0],
                    'album': album,
                    'track_number': song_info['tracknumber'][0],
                    'genre': genre
                    }                
                list_of_music_dict.append(dicti)

                path = '.\\'+dicti['artist']

                #creating directories artist/album for files if it doesn't exists 
                if not os.path.exists(path):
                    os.mkdir(path)
                path += '\\'+dicti['album']               
                if not os.path.exists(path):
                    os.mkdir(path)
                
                new_path = path+'\\'+dicti['track_number']+'. '+ dicti['title']+' '+'('+ dicti['year']+').mp3'
                
                
                os.rename(song_path, new_path)
    
    fh = open('.\\dicti.txt', 'w')
    for dic in list_of_music_dict:
        for key in dic:
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
    specification: Aliti Dzenetan (v0.1)
    implementation: Aliti Dzenetan
    """         
    list_of_music_dict = []
    fh = open(file_path, 'r')
    for line in fh.readlines():
        info = line.split(';')
        """dicti = {
            'title': info[0],
            'artist': info[1],
            'albumartist': info[2],
            'year': info[3],
            'album': info[4],
            'track_number': info[5],
            'genre':info[6]
                }"""
        dicti = {
            'title': '',
            'artist': '',
            'albumartist': '',
            'year': '',
            'album': '',
            'track_number': '',
            'genre': '' 
                }
        for index, key in enumerate(dicti):
            dicti[key] = info[index]
        list_of_music_dict.append(dicti)
    fh.close()
    return list_of_music_dict

def show_all_music(music_list):
    """Display all the music files contained in a directory and its subdirectories.
    
    Parameters
    ----------
    music_list: List of dictionnaries containing all stored songs (list)
    
    Version
    -------
    specification: Aliti Dzenetan (v0.1)
    implementation: Aliti Dzenatan
    """
    liste = os.listdir('.\\')
    print(liste)
    for directory in liste:
        if os.path.isdir('.\\'directory) and os.path.getsize('.\\'directory) != 0:           
            for album in os.listdir('.\\'directory):
                print('The album %s from artist %s contain those titles :\n' % (album, directory))
                for song in os.listdir('.\\directory\\album'):
                    print('%s\n' % song)

def play_music(title, music_dict):
    """
    Play music from start to finish
    
    Parameters
    ----------
    title: Title of the song (str) #Peut être info à trouvé avec mutagen pour indentification unique
    music_dict : Main data structures generated by sort_music (dict)
 
    Version
    -------
    specification: Dadzie Reeckel, Collard Youlan (v0.2)
    implementation: Dadzie Reeckel
    """
    #TODO: Build path from song_dict
#     mixer.music.load()
#     mixer.music.play()


# mixer.init()

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

for index, song in enumerate(_data_structures):
    if song['title'] == 'title2' and song['artist'] == 'artist2':
        print(_data_structures[index])

tag = EasyMP3('./test.mp3')
print(tag)
