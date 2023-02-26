
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
