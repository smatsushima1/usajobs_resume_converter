
# from bs4 import BeautifulSoup as bsp
# import requests

# def pull_usajobs(posting_address):
#     hres = requests.get(posting_address).text
#     soup = bsp(hres, 'html.parser')
#     # Parse job title
#     banner = soup.find('div', {'class': 'usajobs-joa-banner__body usajobs-joa-banner--pilot__body'})
#     jtitle = banner.find('h1').text.strip()
#     dtitle = banner.find('h5', {'class': 'usajobs-joa-banner__dept'}).text.strip()
#     otitle = banner.find('h5', {'class': 'usajobs-joa-banner__hiring-organization'}).text.strip()
#     # Parse all duties
#     dsection = soup.find('div', {'id': 'duties'})
#     duties = dsection.find_all('li')
#     all_duties = ''
#     for i in duties:
#         all_duties += '- ' + i.text + '\n'
#     return jtitle, dtitle, otitle, all_duties
    

# def pull_usajobs2(posting_address):
#     hres = requests.get(posting_address).text
#     soup = bsp(hres, 'html.parser')
#     # Parse job title
#     banner = soup.find('div', {'class': 'usajobs-joa-banner__body usajobs-joa-banner--pilot__body'})
#     jtitle = banner.find('h1').text.strip()
#     dtitle = banner.find('h5', {'class': 'usajobs-joa-banner__dept'}).text.strip()
#     otitle = banner.find('h5', {'class': 'usajobs-joa-banner__hiring-organization'}).text.strip()
#     # Parse all duties
#     dsection = soup.find('div', {'id': 'duties'})
#     duties = dsection.find_all('li')
#     all_duties = ''
#     for i in duties:
#         all_duties += '- ' + i.text + '\n'
#     return jtitle, dtitle, otitle, all_duties

#print(pull_usajobs('https://www.usajobs.gov/job/707979000'))

def print_dev(txt):
    print('Text to print: ' + txt)
    
print_dev('ugh')

