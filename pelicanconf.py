#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Fightfil'
SITENAME = u"Fightfil's Story Collection"
SITEURL = 'http://localhost:8000'
THEME = './theme/elegant'
PATH = 'content'

PLUGIN_PATHS = ['pelican-plugs', 'pelican-plugins']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'md-metayaml', 'neighbors']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.with_'],
}
TYPOGRIFY = True

LANDING_PAGE_ABOUT = {'title':'An Engineering Student\'s Fiction Repository',
                      'details': '''<p>Hi,</p>
        
        <p>My name is Macey, and when I'm online, I go by the name fightfil.
        I've been doing a lot of creative writing since sohpomore year in
        high school, and now I've decided to create a place where I can
        put some of it up to be showcased and read. That place is here!</p>
        
        <p>Below you can see some of my latest stories and essays, etc. On
        the top-bar, you can see links to summaries of my larger projects,
        which are also pointed to on the sidebar.</p>
        
        <p>I mostly write spec-fic styled content, '''
                     }

PROJECTS = [
    {
        'name':'The Penultimate Step',
        'url':'./pages/penultimate-step/index.html',
        'description':
            '''A serial story about a transgender girl
            running track in college and contending with her
            identity'''
        },
    {
        'name':'Sea Songs',
        'url':'./pages/sea-songs/index.html',
        'description':
            '''A story about a screenwriting student who goes to a summer-long
            program that is far more than it seems.'''
        },
    {
        'name': 'Zephra Helmb',
        'url': './pages/voltun.html',
        'description':
            '''A story I am writing for my creative writing seminar at
             University. Set in the Voltun world, Zephra is gender-fluid and
             a mage capable of minor shapeshifting.'''
    }
]

TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'English'

DISQUS_SITENAME = 'fightfil'

MARKDOWN = {
    'extension_configs': {'markdown.extensions.footnotes':{},
                          'markdown.extensions.smarty':{},
                          'pymdownx.smartsymbols':{},
                          'pymdownx.caret':{},
                          'markdown.extensions.tables':{},
                          'markdown.extensions.def_list':{},
                          'markdown.extensions.toc':{}
                         }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
