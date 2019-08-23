from HtmlParse import HtmlParse
from entity.Music import Music
from entity.ShareMusic import ShareMusic

if __name__ == '__main__':
    songurl = 'https://music.163.com/song?id=4989687&userid=503583378'
    share_music = ShareMusic(songurl)
    songid = share_music.songid
    music = Music(songid)
    HtmlParse(songurl).parse_html(music)
    print(music)
