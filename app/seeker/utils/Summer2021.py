from __future__ import print_function

import requests
from bs4 import BeautifulSoup
from ..models.Internship import Internship


class Summer2021:
    def add_internships():
        result = requests.get("https://github.com/Pitt-CSC/Summer2021-Internships")
        src = result.content
        soup = BeautifulSoup(src, 'lxml')

        table_body = soup.find('tbody')
        rows = table_body.find_all('tr')

        data = []

        for row in rows:
            cols = row.find_all('td')
            cols_link = row.find('a')
            cols_text = [ele.text.strip() for ele in cols]

            try:
                cols_link = cols_link.attrs['href']
                cols = cols_text.append(cols_link)
                data.append(cols_text)
            except Exception:
                pass

        for row in data:
            if not Internship.alreadyExists(row[3]):
                Internship.create(row[0], 'Summer', 2021, row[1], row[2], row[3])
