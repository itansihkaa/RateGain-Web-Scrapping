import requests
from bs4 import BeautifulSoup
import json

url = "https://rategain.com/blog/"

# Define a user-agent in the headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Send a GET request to the URL
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all blog items
    blog_items = soup.find_all(class_="blog-item")

    # Initialize an empty list to store the extracted data
    extracted_data = []

    # Loop through each blog item and extract the required information
    for blog_item in blog_items:
        blog_title = blog_item.find(class_="content").find("h6").text.strip()
        blog_date = blog_item.find(class_="blog-detail").find(class_="bd-item").find("span").text.strip()
        blog_img_url = blog_item.find(class_="img").find("a")["data-bg"]
        like_count = blog_item.find(class_="zilla-likes").find("span").text.strip()

        # Create a dictionary for each blog entry
        blog_entry = {
            "blog_title": blog_title,
            "blog_date": blog_date,
            "blog_img_url": blog_img_url,
            "like_count": like_count
        }

        # Add the dictionary to the list
        extracted_data.append(blog_entry)

    # Convert the list of dictionaries to JSON format
    json_data = json.dumps(extracted_data, indent=2)

    # Print the JSON data
    # print(json_data)

    # Write the JSON data to a file
    with open("blog_data.json", "w") as json_file:
        json_file.write(json_data)

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
