import requests
from bs4 import BeautifulSoup

def _download_content(username, password, download_url):
    payload = {
        "name": username,
        "password": password
    }
    with requests.Session() as session:
        try:
            login = session.post("https://info.fortinet.com/session", data=payload)
            # login.cookies.p()
        except Exception, e:
            # "error".p()
            # # login.cookies.p()
            # session.cookies.p()
            pass
        # NOTE the stream=True parameter
        login = session.post("https://info.fortinet.com/login", data=payload)

        content = session.get(download_url, stream=True)
        return content



if __name__ == '__main__':
    from minitest import *

    with test("get_session"):
        username = "chengji"
        password = "Jcjc1609#"
        payload = {
            "name": username,
            "password": password
        }
        session = requests.Session()
        try:
            login = session.post("https://info.fortinet.com/session", data=payload)
            # login.cookies.p()
        except Exception, e:
            pass
        login = session.post("https://info.fortinet.com/login", data=payload)
        main_url = "https://info.fortinet.com/"
        main_page = session.post("https://info.fortinet.com/login", data=payload)

        soup = BeautifulSoup(main_page.content)
        fortigate_5_a = soup.find(title="FortiOS v5.00 release builds")
        fortigate_5_a.attrs.must_equal({u'href': u'/builds?project_id=123',
                u'title': u'FortiOS v5.00 release builds'})
        # print(soup.prettify())
        pass
