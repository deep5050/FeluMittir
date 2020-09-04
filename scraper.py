import requests
from bs4 import BeautifulSoup
from time import sleep



# do not run this script frequently
# If required increase the sleep count
main_url = "https://www.ebanglalibrary.com/category/%E0%A6%B8%E0%A6%A4%E0%A7%8D%E0%A6%AF%E0%A6%9C%E0%A6%BF%E0%A7%8E-%E0%A6%B0%E0%A6%BE%E0%A6%AF%E0%A6%BC/%E0%A6%AB%E0%A7%87%E0%A6%B2%E0%A7%81%E0%A6%A6%E0%A6%BE-%E0%A6%B8%E0%A6%AE%E0%A6%97%E0%A7%8D%E0%A6%B0/"


# did not handle the situation when each subpages has multilple subpages
def get_suburls(story_url):
    urls = []
    response = requests.get(story_url)
    if response.status_code == 200:
        
        
        soup = BeautifulSoup(response.content,'lxml')
        story_name = soup.find_all('h1',class_="page-title")[0]
        file_name = str(story_name).replace('<h1 class="page-title">',"").replace("</h1>","")
        entries = soup.find_all('div',class_="entry-summary")
        print(f' Got {len(entries)} subpages .... ')
        for entry in entries:
            link = entry.find_all('a')
            urls.append(link[0]['href'])

    if urls:
        i = 1
        for url in urls:
            print(f'Fetching {i} th subpage .....')
            sleep(5)
            fetch_substory(url,i,file_name)
            i = i+1

        print("DONE :)")

def fetch_substory(suburl,count,file_name):
    
    content = ""
    response = requests.get(suburl)
    if response.status_code == 200:

        if count == 1:
            content = f'<div align=center> <p align=center><h1 align=center>{file_name}</h1></p></div>'
            content = content + "\n\n\n"


        content = content +f'## {str(count)}'
        content = content + "\n\n"
        soup = BeautifulSoup(response.content,'lxml')
        story = soup.find_all('div',class_='entry-content')
        lines = story[0].find_all('p')
        for line in lines:
            content = content + str(line).replace('<p>',"").replace('</p>',"")+"\n\n\n"

    append_story(content,file_name)

def append_story(content,file_name):
    f = open(file_name+".md",'a')
    f.write(content)
    f.close()


# Feed urls from the tsv file or enter manually
url = "https://www.ebanglalibrary.com/category/%e0%a6%b8%e0%a6%a4%e0%a7%8d%e0%a6%af%e0%a6%9c%e0%a6%bf%e0%a7%8e-%e0%a6%b0%e0%a6%be%e0%a6%af%e0%a6%bc/%e0%a6%ab%e0%a7%87%e0%a6%b2%e0%a7%81%e0%a6%a6%e0%a6%be-%e0%a6%b8%e0%a6%ae%e0%a6%97%e0%a7%8d%e0%a6%b0/%e0%a6%b9%e0%a6%a4%e0%a7%8d%e0%a6%af%e0%a6%be%e0%a6%aa%e0%a7%81%e0%a6%b0%e0%a7%80-%e0%a6%89%e0%a6%aa%e0%a6%a8%e0%a7%8d%e0%a6%af%e0%a6%be%e0%a6%b8-%e0%a7%a7%e0%a7%af%e0%a7%ad%e0%a7%af/"

get_suburls(url)
