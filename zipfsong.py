import sys
from operator import itemgetter

ALBUM_INFO_LINE = 0


def split_album(album_input):
    split_album = [line.split() for line in album_input]
    num_songs, num_to_sel = split_album[ALBUM_INFO_LINE]
    return num_songs, num_to_sel, split_album

def get_album_quality(album_split):
    #album_with_quality = [(index * int(views), index, song) for index, (views, song) in enumerate(split_album) if index != 0]
    album_with_quality = []

    for index, (views, song) in enumerate(album_split):
        if index != 0:
            quality = index * int(views)
            album_with_quality.append((quality, index, song))

    #print album_with_quality
    return album_with_quality

def get_top_songs(album_quality, num_to_sel):
    sorted_album = sorted(album_quality, key=itemgetter(0,1))

    reversed_album = [song for quality,index,song in reversed(sorted_album)]

    top_songs = reversed_album[:int(num_to_sel)]

    return top_songs


if __name__ == '__main__':
    album = sys.stdin.readlines()

    _, num_to_sel, split_album = split_album(album)
    album_with_quality = get_album_quality(split_album)
    top_songs = get_top_songs(album_with_quality, num_to_sel)

    print
    print "--------------------"
    print "OUTPUT"
    print "--------------------"
    print

    for song in top_songs:
        print song




