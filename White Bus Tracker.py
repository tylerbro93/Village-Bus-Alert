from bs4 import BeautifulSoup
from urllib.request import urlopen
url = "https://services.saucontds.com/public-services/public-key/stopgroups/display?publicKey=380a944f-aca4-5948-b754" \
      "-39f79e538b99&stops=The%20Gamecock%20Village&departures=true&zoom=225&hours=.5&style=redgrey&fields=Route" \
      ";Departure;Depart;Status;&expireHours=0 "
client = urlopen(url)
page = client.read()
soupPage = BeautifulSoup(page, "html.parser")

table = soupPage.findAll("td", {"class": "td-bold"})
times = []
for i in range(0, len(table)):
    if("AM" in table[i].text or "PM" in table[i].text):
        times.append(table[i].text)
print(times)
client.close()

