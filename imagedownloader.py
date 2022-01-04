import requests,os,sys
from pathlib import Path
from bs4 import BeautifulSoup
print("running...")
s=input("enter a keyword")
url="https://unsplash.com/s/photos/"+s
#url="https://www.pexels.com/@hiteshchoudhary"
res=requests.get(url)
res.raise_for_status()
link=[]
soup=BeautifulSoup(res.text,"html.parser")
#x=soup.find_all("img",{"class":"_2UpQX"})
x=soup.select("._2UpQX")
print(len(x))
for i in x:
    if i.attrs["src"] not in link:
        link.append(i.attrs["src"])


print(len(link))
p=Path.cwd()
os.mkdir(p/s)

for i in range(1,len(link)+1):
    print(link[i-1])
    print(f"download {i} succesful...")
    myfile = open(p / s / f"image{i}.jpg", "wb")
    res = requests.get(link[i - 1])
    for chunks in res.iter_content(1000):
        myfile.write(chunks)




