# Apicell

## You can use this api to search in google, bing, pypi and subscene and get results
<br>
Method : POST
<br>
Parameter : query


### Example

```python
import request
url = 'http://127.0.0.1:8000/pypi-search/'
data = {'query' : 'numpy'}

post_req = requests.post(url, data=data)
json_res = post_req.json()

for url in json_res:
    print(url['url'])
```
