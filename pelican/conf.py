#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import datetime
import os
import sys
sys.path.append(os.curdir)

# index
AUTHOR = '薛浩'
SITEDESCRIPTION = 'BLOG.STICKMIND.COM - 薛浩的博客 - 严谨、有趣、持续更新：数学、编程、统计、英语、音乐、摄影……'
SITENAME = "薛浩的博客 - 追求卓越，宁静致远"
FAVICON = 'theme/img/notebook.png'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_LANG = 'zh-CN'
SITETITLE = "xuehao's blog"
SITESUBTITLE = "To make your dreams happen"
SITEURL = 'https://blog.stickmind.com'

# theme
THEME = "themes/Flex"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True
PYGMENTS_STYLE = 'github'
PYGMENTS_STYLE_DARK = 'monokai'

# content
PATH = 'content'
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
USE_FOLDER_AS_CATEGORY = False
RELATIVE_URLS = True

# structure
MAIN_MENU = True
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)
DISPLAY_PAGES_ON_MENU = True
HOME_HIDE_TAGS = True
SUMMARY_MAX_LENGTH = 38
DEFAULT_PAGINATION = 5

# copyright
COPYRIGHT_NAME = AUTHOR
COPYRIGHT_YEAR = datetime.now().year
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "local_icons": True,
    "language": "zh-CN",
}

# links
LINKS = (
    ('resume', 'https://www.stickmind.com'),
)

# social
SOCIAL = (
    ('github', 'https://github.com/xuehao'),
    ('envelope', 'mailto:xuehao0618@icloud.com'),
    ("rss", "/feeds/all.atom.xml"),
)

# plugins
PLUGINS = ["render_math", "simple_footnotes"]
