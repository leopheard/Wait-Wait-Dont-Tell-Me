import requests
import re
from bs4 import BeautifulSoup
import xbmc

def get_soup(url1):
    """
    @param: url of site to be scraped
    """
    page = requests.get(url1)
    soup = BeautifulSoup(page.text, 'html.parser')
    xbmc.log('type: %s'%(type(soup)),xbmc.LOGDEBUG)
    print("type: ", type(soup))
    return soup
get_soup("https://www.npr.org/rss/podcast.php?id=344098539")


def get_playable_podcast(soup):
    """
    @param: parsed html page            
    """
    subjects = []
    for content in soup.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            desc = content.find('description')
#            desc = desc.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': "https://media.npr.org/assets/img/2019/05/23/screen-shot-2019-05-23-at-8.46.21-am_sq-7dcea391e7a87ca3569fe3d2047dda0144e5d86f.png?s=1400"
        }
        subjects.append(item)
    return subjects


def compile_playable_podcast(playable_podcast):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []

    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })

    return items


def get_playable_podcast1(soup):
    """
    @param: parsed html page            
    """
    subjects = []
    for content in soup.find_all('item', limit=7):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            desc = content.find('description')
#            desc = desc.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': "https://media.npr.org/assets/img/2019/05/23/screen-shot-2019-05-23-at-8.46.21-am_sq-7dcea391e7a87ca3569fe3d2047dda0144e5d86f.png?s=1400"
        }
        subjects.append(item) 
    return subjects


def compile_playable_podcast1(playable_podcast1):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })
    return items
