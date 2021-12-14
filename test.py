from SearchSpider import *

url = PreURL('https://pypi.org', 'https', 'https://pypi.org', '/search', 'q', 'numpy', 'span', get_by_class_title='package-snippet__name',
get_by_class_links='package-snippet__version')

URL = url.URL()
