import os
import requests
from bs4 import BeautifulSoup

# URL of the directory containing images
url = 'https://livedemo00.template-help.com/wt_prod-12465/'

# Send HTTP request to fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all img tags
img_tags = soup.find_all('img')

# Create a folder to save images
os.makedirs('downloaded_images', exist_ok=True)

# Download images
for img_tag in img_tags:
    img_url = img_tag.get('src')
    if img_url:
        full_img_url= "https://livedemo00.template-help.com/wt_prod-12465/"+img_url
        print("========================================================path is "+img_url)
      
        img_name = os.path.basename(img_url)
        img_path = os.path.join('downloaded_images', img_name)

        # Download image
        img_response = requests.get(full_img_url)
        with open(img_path, 'wb') as f:
            f.write(img_response.content)
        print(f'Downloaded {img_name}')
