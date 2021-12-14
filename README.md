# Apicell

## You can use this api to search in google, bing, pypi and subscene and get results
<br>
_Method_ : **POST**
<br>
_Parameter_ : **query**


### Example

```python
import request
url = 'https://apicell.anon-c0der.repl.co/pypi-search/'
data = {'query' : 'numpy'}

post_req = requests.post(url, data=data)
json_res = post_req.json()

for url in json_res:
    print(url['url'])

```
