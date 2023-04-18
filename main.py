import requests
import bs4 as bs
import csv
import pandas as pd
def extract_data(s):
    url = f"https://www.flipkart.com/search?q=bags&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={s}"
    data = requests.get(url)
    res = data.text
    soup = bs.BeautifulSoup(res, "lxml")
    data = soup.find_all('div',class_="_2WkVRV")
    price = soup.find_all('div',class_="_30jeq3")
    off = soup.find_all('div',class_="_3Ay6Sb")
    original_price = soup.find_all('div',class_="_30jeq3")
    output_list = [[i.text.strip() for i in data],[i.text.strip() for i in price],[i.text.strip() for i in off],[i.text.strip() for i in original_price]]
    return output_list
dict1 = {"name":[],"price":[],"offer":[],"original price":[]}
for i in range(1,6):
    dict = extract_data(i)
    dict1['name']+=dict[0]
    dict1['price']+=dict[1]
    dict1['offer']+=dict[2]
    dict1['original price']+=dict[3]
with open('flipkart1.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Price", "Offer", "Original Price"])
    writer.writerows(zip(*dict1.values()))
