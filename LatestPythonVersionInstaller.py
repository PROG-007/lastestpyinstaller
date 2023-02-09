import requests
import time
import os
import urllib.request
from bs4 import BeautifulSoup

ver_dict=[]
url = "https://www.python.org/ftp/python/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
text_elements = [text.strip() for text in soup.stripped_strings]
for line in text_elements:
    if len(line) < 9 and len(line) > 4:
      sum=0
      isVer=True
      for i in line[:-1].split('.'):
        if i.isdigit() == False:
          isVer=False
          break
      if isVer:
        ver_dict.append(line[:-1])
ver_dict.remove(max(ver_dict, key=lambda x: [int(i) for i in x.split('.')]))
version=max(ver_dict, key=lambda x: [int(i) for i in x.split('.')])
print("Latest Python Version Found: ",version)
time.sleep(1)
url = f"https://www.python.org/ftp/python/{version}/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
text_elements = [text.strip() for text in soup.stripped_strings]
print(f"Searching for installer in {len(text_elements)} files")
time.sleep(1)
for line in text_elements:
    if line[-9::] == "amd64.exe":
        print("Downloading Installer... ",line)
        urllib.request.urlretrieve(url+f"/{line}", line)
        os.system(line)
        os.system(f"del {line}")
print(f"Finished!")
os.system("PAUSE")