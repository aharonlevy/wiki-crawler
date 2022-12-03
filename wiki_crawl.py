'''
crawl through wikipedia and prints the page HTML
'''
import ssl
import requests


def get_page_data():
    '''
    prints the HTML the page the user request
    '''
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    #make a request from wikipedia API
    html_req_url = "https://en.wikipedia.org/api/rest_v1/page/html/"
    page_name = input("Please write the subject name: ")
    html_req_url_end = "?redirect=true"

    response = requests.get(html_req_url + page_name + html_req_url_end, timeout= 15)
    if response.status_code == 200:
        print(response.content)
    else:
        print(response.status_code)
get_page_data()
