import pandas as pd
import requests
from bs4 import BeautifulSoup

# Initialize lists to store the scraped data
Product_name = []
Prices = []
Reviews = []
DESCRIPTION = []

# Loop through pages
for i in range(2, 12):
    url = f"https://www.flipkart.com/search?q=mobiles+under+50000&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_7_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_7_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles+under+50000&requestId=fc9220bd-d24a-4d24-a44d-e7afdf73873e&as-backfill={i}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    # Find all product containers
    boxes = soup.find_all("div", class_="DOjaWF gdgoEp")

    # Iterate through each product box
    for box in boxes:
        # Extract product name
        name = box.find("div", class_="KzDlHZ")
        Product_name.append(name.text if name else "N/A")

        # Extract product price
        price = box.find("div", class_="Nx9bqj _4b5DiR")
        Prices.append(price.text if price else "N/A")

        # Extract product description
        description = box.find("ul", class_="G4BRas")
        DESCRIPTION.append(description.text if description else "N/A")

        # Extract reviews
        review = box.find("div", class_="XQDdHH")
        Reviews.append(review.text if review else "N/A")

# Create a DataFrame
df = pd.DataFrame({
    "Product Name": Product_name,
    "Prices": Prices,
    "DESCRIPTION": DESCRIPTION,
    "Reviews": Reviews
})

# Display the DataFrame
# print(df)
df.to_csv("D:/flipcart_mobiles_under_50000.csv")


# print(soup)
# while True:
# np = soup.find("a",class_= "_9QVEpD").get("href")
# # print(np)
# cnp = "https://www.flipkart.com/"+np
# print(cnp)

    # url = cnp
    # r = requests.get(url)
    # soup = BeautifulSoup(r.text, "lxml")