# créer une playlist à partir de critères divers (artiste, année, etc.), (Georges, Loic, Youlan) 
 
def generate_playlist(name, artist = None, year = None, genre = None):
    """generate a playlist according to the user's choice
    PARAMETERS
    ----------
    name: name of the playlist
    artist: create a playlist containing every song from 1 artist (str)
    year: create a playlist containing every song from a designated year (int)
    genre: create a playlist containing every song from a designated genre (str)
 
    RETURNS
    -------
    playlist# : create playlist with the corresponding name (dictionary)
    ########## QUID ? retour dico puis fichier ?  retour direct fichier txt ? fichier sous quelle formatage ?
    ########## QUID bis ? return en playlist n°x ou modification possible du nom de la playlist par l'utilisateur ? (je prends solution 2 pour la spé de la fonction show_content_playlist pour le moment)
    ########## Note Youlan : Besoin de retour ? Puisqu'on va créer un fichier ?
    
    VERSION
    -------
    specification: Hoebrechts Georges & Collad Youlan (v0.2)
    implementation: 
    """
 
# afficher le nom de toutes les playlists disponibles, (Georges, Loic, Youlan) 
 
def show_all_playlist():
    """show every playlist created by the user
    PARAMETERS
    ----------
    none
 
    RETURNS
    -------
    list_playlist : create a list of every playlist created by the user (list)
    
    VERSION
    -------
    specification: Hoebrechts Georges (v0.1)
    implementation: 
    """ 
 
# afficher les morceaux contenus dans une playlist, (Georges, Loic, Youlan, P-A) 
 
def show_content_playlist(playlist):
    """show the content of a playlist created by the user
    PARAMETERS
    ----------
    playlist : name of the playlist (str)
 
    RETURNS
    -------
    playlist_content : create a list of every song in the playlist (list)
    
    VERSION
    -------
    specification: Hoebrechts Georges (v0.1)
    implementation: 
    """    
 
# lire une playlist du début à la fin (appel « bloquant »). (Georges, Loic, Youlan) 
 
def read_playlist(playlist):
    """read every song contained in a playlist
    PARAMETERS
    ----------
    playlist : name of the playlist (str)
 
    RETURNS
    -------
    play_playlist : read every song contained in a playlist (bool)
    
    VERSION
    -------
    specification: Hoebrechts Georges (v0.1)
    implementation: 

    ####### Pourquoi un bool en retour ici ?
    """      

def sort_music(dir_path, music_path):
    """Extract music files from a directory and sort them into authors directory and album sub-directory
    
    Parameters
    ----------
    dir_path: path to directory containing the music files to sort (str)
    music_path: path where to creat a music directory to store sorted music (str)
    
    Return
    ------
    Je ne pense pas qu'il y ai besoin de retour pour le moment(J'essaie de piger comment utiliser la nouvelle matière afin de mieux pouvoir spécifier)
    
    Version
    -------
    specification: Aliti Dzenetan(v0.1)
    implementation:
    """
 
def show_all_music(music_path):
    """Display all the music files contained in a directory and its subdirectories.
    
    Parameters
    ----------
    music_path: path to directory the content is to be shown
    
    Version
    -------
    specification: Aliti Dzenetan(v0.1)
    implementation:
    """