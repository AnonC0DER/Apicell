from rest_framework.decorators import api_view
from rest_framework.response import Response
from urllib.parse import urlencode, urlunparse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from googlesearch import search
import random


# Get Random useragent
def RandomUSERagent():
	fp = open('database/user_agents.txt', 'r')
	Content = fp.read()
	CoList = Content.split('\n')

	USER_AGENTS_LIST = []
	for i in CoList:
		try:
			USER_AGENTS_LIST.append(i)
		except:
			pass

	return random.choice(USER_AGENTS_LIST)



@api_view(['GET'])
def AllMethods(request):
    routes = [
        {'POST' : '/google-search/'},
        {'POST' : '/bing-search/'},
        {'POST' : '/pypi-search/'},
        {'POST' : '/subscene-search/'},
    ]

    return Response(routes)



# Search in Google.com
@api_view(['POST'])
def GOOGLE(request):
    # Get query from post method
    Query = request.data['query']

    Search = search(Query, num_results=20)

    return Response(Search)



# Search in bing.com
@api_view(['POST'])
def BING(request):
    # Get query from post method
    Query = request.data['query']

    # Prepare url
    url = urlunparse(('https', 'www.bing.com', '/search', '', urlencode({'q': Query}), ''))
    # get random user agent
    custom_user_agent = RandomUSERagent()
    # open url
    req = Request(url, headers={'User-Agent': custom_user_agent})
    page = urlopen(req)
    # read html page
    soup = BeautifulSoup(page.read(), 'lxml')
    # find all a tags
    links = soup.findAll('a')
    
    AllLinks = []
    AllTitles = []

    # append maximum 15 links and title to lists
    for link in links:
        # don't interrupt application if there's a problem with a link
        try:
            # filter a tags in page
            if link['href'].startswith('https://') or link['href'].startswith('http://'):
                # append the url
                AllLinks.append(link['href'])
                # append the title
                AllTitles.append(link.text)
            else:
                pass
        except:
            pass
    ####################################
    # all data append to this list
    data = []

    # append data to data list
    for title, link in zip(AllTitles, AllLinks):
        # append all data
        data.append(
            {
                'Title' : title,
                'url' : link, 
            }
        )

    # return data list    
    return Response(data)



# Search in subscene
@api_view(['POST'])
def SUBSCENE(request):
    # Get data
    Query = request.data['query']

    # subscene main domain
    subscene = 'https://subscene.com'
    # Prepare url
    url = urlunparse(('https', 'subscene.com/subtitles', '/searchbytitle', '', urlencode({'query': Query}), ''))
    # get random user agent
    custom_user_agent = RandomUSERagent()
    # open url
    req = Request(url, headers={'User-Agent': custom_user_agent})
    page = urlopen(req)
    # read html page
    soup = BeautifulSoup(page.read(), 'lxml')
    # find all a tags
    links = soup.findAll('a')

    subscene_links = []
    subscene_strings = []

    # append maximum 15 links and title to lists
    for url, _ in zip(links, range(15)):
        # filter a tags in page
        if '/subtitles/' in url['href']:
            # append full link to the list, example : https://subscene.com/subtitles/breaking-bad-fourth-season-2011
            subscene_links.append(subscene + url['href'])
            # append title to the list
            subscene_strings.append(url.text)
        else:
            pass

    ################################
    # all data append to this list
    data = []

    # append title and url to data list
    for title, link in zip(subscene_strings, subscene_links):
        # append all data
        data.append(
            {
                'Title' : title,
                'url' : link, 
            }
        )

    return Response(data)



# Search in pypi.org
@api_view(['POST'])
def PYPI(request):
    # Get query from post method
    Query = request.data['query']

    # pypi main domain
    pypi = 'https://pypi.org'
    # Prepare url : https://pypi.org/search/?q=Query 
    url = urlunparse(('https', 'pypi.org', '/search', '', urlencode({'q': Query}), ''))
    # get random user agent
    custom_user_agent = RandomUSERagent()
    # open url
    req = Request(url, headers={'User-Agent': custom_user_agent})
    page = urlopen(req)
    # read html page
    soup = BeautifulSoup(page.read(), 'lxml')
    # find all titles and versions 
    titles = soup.findAll('span', {'class' : 'package-snippet__name'})
    versions = soup.findAll('span', {'class' : 'package-snippet__version'})
    # find all links by class
    links = soup.findAll('a', {'class' : 'package-snippet'})
    # find all short descriptions by class
    descriptions = soup.findAll('p', {'class' : 'package-snippet__description'})
    
    pypi_names = []
    pypi_links = []
    pypi_strings = []
    
    # append all data into two lists
    for title, version in zip(titles, versions):
        pypi_names.append(f'{title.text} - {version.text}')

    for link in links:
        pypi_links.append(pypi + link['href'])

    for description in descriptions:
        pypi_strings.append(description.text)
    
    ################################################################
    # Return Result

    # title, description and url append to this list
    data = []
    # loop into pypi_links and pypi_strings
    for package_name, link, description, _ in zip(pypi_names, pypi_links, pypi_strings, range(15)):
        # append all data
        data.append(
            {
                'Package_name' : package_name,
                'description' : description,
                'url' : link, 
            }
        )

    # return data list    
    return Response(data)
    

# github.com/AnonC0DER