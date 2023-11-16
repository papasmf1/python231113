import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

search_keyword = "iPhone 15"
wb = Workbook()
ws = wb.active
ws.append(["Page", "Blog Address", "Blog Name", "Title", "Posting Date"])

for page in range(1, 101):  # Loop through pages 1 to 100
    url = f"https://search.naver.com/search.naver?where=view&sm=tab_pge&query={search_keyword}&start={page * 10 - 9}"

    # Send a GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the elements containing the information you need
        blog_posts = soup.find_all('li', class_='bx _svp_item')

        for post in blog_posts:
            # Extract blog address
            blog_address = post.find('a', class_='api_txt_lines').get('href')

            # Extract blog name
            blog_name = post.find('a', class_='sub_txt').text

            # Extract title of the post
            title = post.find('a', class_='api_txt_lines').text

            # Extract posting date
            posting_date = post.find('span', class_='sub_time sub_txt').text

            # Append data to the Excel sheet
            ws.append([page, blog_address, blog_name, title, posting_date])

    else:
        print(f"Failed to retrieve page {page}")

# Save the workbook to a file
file_path = r'c:\work\blog.xlsx'
wb.save(file_path)
print(f"File saved at {file_path}")
