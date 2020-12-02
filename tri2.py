import os
from mutagen.mp3 import EasyMP3

def concatenate(word_list):
    """Concatenate word from a list to a string
    
    Parameters
    ----------
    word_list: a list of words (list)
    
    Returns
    -------
    string: the elements of word_list (str)

    Version
    -------
    specification: Aliti Dzenetan (v0.1)
    implementation: Aliti Dzenetan
    """
    #function used instead of str.join()
    string = ''
    for word in word_list:
        string += word
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
    
def show_all_music(path_to_txt):
    """Display all the music files contained in a directory and its subdirectories.
    
    Parameters
    ----------
    path_to_txt: path to the txt file containing all infos (str)
    
    Version
    -------
    specification: Aliti Dzenetan (v0.1)
    implementation: Aliti Dzenatan
    """
    dicti = information_dict(path_to_txt)
    print('The following songs are available :\n')
    for elem in dicti:
        print('%s from artist %s in album %s' % (elem['title'], elem['artist'], elem['album']))



            
   
sort_music('F:\Codage\Git\INFOA-5-MP3-1\\archive')
show_all_music('F:\Codage\Git\INFOA-5-MP3-1\dicti.txt')



