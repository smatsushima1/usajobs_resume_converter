
from bs4 import BeautifulSoup as bsp
#from jscript import pullAddress
from pyscript import Element

def print_dev(pvalue):
    x = 'Value is: ' + pvalue
    Element('dt').write(x)


def print_dev2():
    Element('jt').write(Element('posting').value)
    Element('dt').write('This works')
    Element('ot').write('This works2')
    Element('ad').write('This works3')
    

def pull_posting():
    hres = ""
    # hres = requests.get(pullAddress()).text
    #hres = await pyodide.http.pyfetch(pullAddress())
    soup = bsp(hres, 'html.parser')
    # Parse job, department, and office
    banner = soup.find('div', {'class': 'usajobs-joa-banner__body usajobs-joa-banner--pilot__body'})
    jtitle = banner.find('h1').text.strip()
    dtitle = banner.find('h5', {'class': 'usajobs-joa-banner__dept'}).text.strip()
    otitle = banner.find('h5', {'class': 'usajobs-joa-banner__hiring-organization'}).text.strip()
    # Parse all duties
    dsection = soup.find('div', {'id': 'duties'})
    duties = dsection.find_all('li')
    all_duties = ''
    for i in duties:
        all_duties += '- ' + i.text + '\n'
    # Add all data
    Element('jt').write(jtitle)
    Element('dt').write(dtitle)
    Element('ot').write(otitle)
    Element('ad').write(all_duties)


from pyodide.http import pyfetch, FetchResponse
from typing import Optional, Any

async def request(url: str, method: str = "GET", body: Optional[str] = None,
                  headers: Optional[dict[str, str]] = None, **fetch_kwargs: Any) -> FetchResponse:
    """
    Async request function. Pass in Method and make sure to await!
    Parameters:
        url: str = URL to make request to
        method: str = {"GET", "POST", "PUT", "DELETE"} from `JavaScript` global fetch())
        body: str = body as json string. Example, body=json.dumps(my_dict)
        headers: dict[str, str] = header as dict, will be converted to string...
            Example, headers=json.dumps({"Content-Type": "application/json"})
        fetch_kwargs: Any = any other keyword arguments to pass to `pyfetch` (will be passed to `fetch`)
    Return:
        response: pyodide.http.FetchResponse = use with .status or await.json(), etc.
    """
    kwargs = {"method": method, "mode": "no-cors"}  # CORS: https://en.wikipedia.org/wiki/Cross-origin_resource_sharing
    if body and method not in ["GET", "HEAD"]:
        kwargs["body"] = body
    if headers:
        kwargs["headers"] = headers
    kwargs.update(fetch_kwargs)

    response = await pyfetch(url, **kwargs)
    return response


import asyncio
import json

async def main():
    baseurl = "https://www.usajobs.gov/job/707979000"

    # GET
    headers = {"Content-type": "application/json"}
    response = await request(f"{baseurl}/posts/2", method="GET", headers=headers)
    print(f"GET request=> status:{response.status}, json:{await response.json()}")

    # # POST
    # body = json.dumps({"title": "test_title", "body": "test body", "userId": 1})
    # new_post = await request(f"{baseurl}/posts", body=body, method="POST", headers=headers)
    # print(f"POST request=> status:{new_post.status}, json:{await new_post.json()}")

    # # PUT
    # body = json.dumps({"id": 1, "title": "test_title", "body": "test body", "userId": 2})
    # new_post = await request(f"{baseurl}/posts/1", body=body, method="PUT", headers=headers)
    # print(f"PUT request=> status:{new_post.status}, json:{await new_post.json()}")

    # # DELETE
    # new_post = await request(f"{baseurl}/posts/1", method="DELETE", headers=headers)
    # print(f"DELETE request=> status:{new_post.status}, json:{await new_post.json()}")

# asyncio.ensure_future(main())