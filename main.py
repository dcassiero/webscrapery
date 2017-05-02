from bs4 import BeautifulSoup
import requests

params = []
r = requests.get("https://stage-services.icg360.org/cxcat/health", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.findAll("label", {"class": "control-label"})

print(results)