from bs4 import BeautifulSoup
import requests
import csv
import os
import time
from win10toast import ToastNotifier
from pathlib import Path

#result = requests.get("https://www.nairaland.com/frinx/posts")

#soup = BeautifulSoup(result, 'html5lib')
#source = requests.get(f'https://www.nairaland.com/{username}/posts').text
#post = BeautifulSoup(source, 'lxml').find_all('table')[1].div.text

#post = soup.find_all('table')[1].div.text
#print(soup)
#current_post = post.text

icon_path = Path("C:/Users/aiiks/Workspace/Beautifulsoup/img/NL.ico")

toaster = ToastNotifier()



with open('save.csv', 'r') as csv_file:
    fieldnames = ['username','lastpost']
    csv_reader = csv.DictReader(csv_file, fieldnames=fieldnames)

    with open('save2.csv', 'w') as csv_file:
        fieldnames2 = ['username','lastpost']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames2)

        for line in csv_reader:
            username = line['username']

            source = requests.get(f'https://www.nairaland.com/{username}/posts').text
            post = BeautifulSoup(source, 'lxml').find_all('table')[1].div.text
            csv_writer.writerow({"username":line['username'],"lastpost":post})

            if post != line['lastpost']:
                toaster.show_toast(f'New Post from {username}!', f'{post}  https://www.nairaland.com/{username}/posts', icon_path=icon_path, duration=20)
                while toaster.notification_active(): time.sleep(0.1)
os.remove('./save.csv')
os.rename('./save2.csv', './save.csv')

