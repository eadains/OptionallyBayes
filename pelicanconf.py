#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Erik Dains"
SITENAME = "Optionally Bayes"
SITETITLE = "Optionally Bayes"
SITESUBTITLE = "My journey in life and math. Anything goes."
SITEURL = "https://eadains.github.io/OptionallyBayes"
PATH = "content"
MAIN_MENU = True
COPYRIGHT_NAME = "Erik Dains"
COPYRIGHT_YEAR = "2020"
SITELOGO = SITEURL + "/photos/headshot.jpg"

TIMEZONE = "America/Chicago"

DEFAULT_LANG = "en"

THEME = "/home/eadains/Flex"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (("Pelican", "https://getpelican.com/"),
#         ("Python.org", "https://www.python.org/"),
#         ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#         ("You can modify those links in your config file", "#"),)

# Social widget
SOCIAL = (
    ("github", "https://github.com/eadains"),
    ("instagram", "https://www.instagram.com/erikdains/"),
    ("linkedin", "https://www.linkedin.com/in/erik-dains/"),
)

MENUITEMS = (
    ("Archives", "archives.html"),
    ("Categories", "categories.html"),
    ("Tags", "tags.html"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
