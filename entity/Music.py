import requests


class Music:

    def __init__(self, songid='', name='', type='', imageurl='', description='', artist='', album='',
                 albumurl='', duration=0, artisturl=''):
        self.songurl = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(songid)
        self.lrcurl = 'http://music.163.com/api/song/media?id={}'.format(songid)
        self.name = name
        self.type = type
        self.artist = artist
        self.album = album
        self.duration = duration
        self.description = description
        self.albumurl = albumurl
        self.artisturl = artisturl
        self.imageurl = imageurl

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def songurl(self):
        return self._songurl

    @songurl.setter
    def songurl(self, songurl):
        self._songurl = songurl

    @property
    def lrcurl(self):
        return self._lrcurl

    @lrcurl.setter
    def lrcurl(self, lrcurl):
        self._lrcurl = lrcurl
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        response = requests.get(lrcurl, headers=headers)
        if response.status_code == 200:
            json = response.json()
            self.lyric = json.get('lyric', '')

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, artist):
        self._artist = artist

    @property
    def album(self):
        return self._album

    @album.setter
    def album(self, album):
        self._album = album

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        self._duration = duration

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def albumurl(self):
        return self._albumurl

    @albumurl.setter
    def albumurl(self, albumurl):
        self._albumurl = albumurl

    @property
    def artisturl(self):
        return self._artisturl

    @artisturl.setter
    def artisturl(self, artisturl):
        self._artisturl = artisturl

    @property
    def imageurl(self):
        return self._imageurl

    @imageurl.setter
    def imageurl(self, imageurl):
        self._imageurl = imageurl

    @property
    def lyric(self):
        return self._lyric

    @lyric.setter
    def lyric(self, lyric):
        self._lyric = lyric

    def __str__(self):
        return '''
         songurl:\t{}
         imageurl:\t{}
         lrcurl:\t{}
         name:\t{}
         artist:\t{}
         type:\t{}
         album:\t{}
         duration:\t{}
         albumurl:\t{}
         artisturl:\t{}
         lyric:
{}
         '''.format(self.songurl, self.imageurl, self.lrcurl, self.name, self.artist, self.type, self.album,
                    self.duration,
                    self.albumurl, self.artisturl, self.lyric)
