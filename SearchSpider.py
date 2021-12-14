from urllib import request
from urllib.parse import urlencode, urlunparse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from bs4.element import PageElement, SoupStrainer
import lxml

def get_random_USERAGENT():
    return 's'


class PreURL:
    
    def __init__(
        self, 
        website, http, maindomain, search_page, website_query, query,
        html_tag_titles, html_tag_links, get_by_class_title, get_by_id_title, get_by_id_links, get_by_class_links 
    ):
        self.website = website if website else None
        self.http = http
        self.maindomain = maindomain
        self.search_page = search_page
        self.website_query = website_query
        self.query = query
        self.html_tag_titles = html_tag_titles if html_tag_titles else None
        self.html_tag_links = html_tag_links if html_tag_links else None
        self.get_by_class_title = get_by_class_title if get_by_class_title else None
        self.get_by_id_title = get_by_id_title if get_by_id_title else None
        # get variables for to find links by id or class name
        self.get_by_id_links = get_by_id_links if get_by_id_links else None
        self.get_by_class_links = get_by_class_links if get_by_class_links else None
    

    def URL(self):
        # if the website didn't add the main url in html page this variable is required
        Website_url = self.website
        # Prepare url : https://pypi.org/search/?q=Query 
        PreURL = urlunparse((self.http, self.maindomain, self.search_page, '', urlencode({self.query : self.website_query})))
        # get random user agent
        User_Agent = get_random_USERAGENT
        # open url
        request = Request(PreURL)
        open_page = urlopen(request)
        # read html page
        Read_Page = BeautifulSoup(open_page.read(), 'lxml')

        return Read_Page




class FindTags(PreURL):
    def Search(self):
        Read_Page = PreURL.URL()

        # if get_by_class not equal to None and get_by_id equal to None, then this variable is self.get_by_class else self.get_by_id
        Class_OR_Id = self.get_by_class if self.get_by_class != None and self.get_by_id == None else self.get_by_id
        # find all titles
        titles = Read_Page.findAll(self.html_tag_titles, {self.html_tag_titles : Class_OR_Id})    
        # find all links by class
        links = Read_Page.findAll(self.html_tag, {self.html_tag_links : Class_OR_Id})

        print(200)


