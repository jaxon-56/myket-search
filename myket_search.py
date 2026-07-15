import requests
from bs4 import BeautifulSoup


class MyketSearch:

    BASE_URL = "https://myket.ir/Search/Apps"

    def search(self, keyword: str, page: int = 0):

        response = requests.get(
            self.BASE_URL,
            params={
                "keyword": keyword,
                "page": page
            },
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        apps = []

        for app in soup.select("div.list-app"):

            link = app.select_one("a.app-detail-link")
            name = app.select_one("p.app-name")
            category = app.select_one("p.app-group")
            image = app.select_one("img")

            apps.append({
                "name": name.get_text(strip=True),
                "package_name": link["data-package-name"],
                "category": category.get_text(strip=True),
                "url": "https://myket.ir" + link["href"],
                "icon": image["src"]
            })

        return apps
