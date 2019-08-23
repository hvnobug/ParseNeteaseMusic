from selenium import webdriver
from pyquery import PyQuery as pq

from entity import Music

driver = webdriver.Chrome()


class HtmlParse:
    def __init__(self, songurl):
        self._songurl = songurl

    def parse_html(self,music):
        driver.get(self._songurl)
        driver.switch_to.frame("g_iframe")
        html = driver.page_source
        doc = pq(html)

        def filter_mate(i, mate):
            mate_property = pq(mate).attr('property')
            return True if mate_property else False

        def each_mate(i, mate):
            mate = pq(mate)
            mate_property = mate.attr('property')
            mate_content = mate.attr('content')
            if mate_property == 'og:title':
                music.name = mate_content
            elif mate_property == 'og:type':
                music.type = mate_content
            elif mate_property == 'og:image':
                music.imageurl = mate_content
            elif mate_property == 'og:url':
                music.songurl = mate_content
            elif mate_property == 'og:description':
                music.description = mate_content
            elif mate_property == 'og:music:artist':
                music.artist = mate_content
            elif mate_property == 'og:music:album':
                music.album = mate_content
            elif mate_property == 'music:album':
                music.albumurl = mate_content
            elif mate_property == 'music:duration':
                music.duration = mate_content
            elif mate_property == 'music:musician':
                music.artisturl = mate_content
        doc('meta').filter(filter_mate).each(each_mate)

