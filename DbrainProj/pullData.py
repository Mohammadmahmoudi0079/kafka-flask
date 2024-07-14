import requests
from bs4 import BeautifulSoup
import json

class Product:
    def __init__(self, title, price, description, stock_info):
        self.title = title
        self.price = price
        self.description = description
        self.stock_info = stock_info

    def __repr__(self):
        return (f"Title : {self.title} \n Price : {self.price} \n Description : {self.description} \n Stock : {self.stock_info} \n ---------------------")
    def to_dict(self):
        return {
            'title': self.title,
            'price': self.price,
            'description': self.description,
            'stock_info': self.stock_info
        }
    @staticmethod
    def serialize(product):
        return json.dumps(product.to_dict(), indent=4)
    @staticmethod
    def serialize_list(product_list):
        return json.dumps([product.to_dict() for product in product_list], indent=4)
    
url = 'https://scrapeme.live/shop/'
response = requests.get(url)

product_list =[]
def pull_product():
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        products = soup.find_all('li', class_='product')

        for product in products:
        
            title = product.find('h2', class_='woocommerce-loop-product__title').text
            price = product.find('span', class_='woocommerce-Price-amount amount').text
            link = product.find('a')['href']
            product_response = requests.get(link)
            if product_response.status_code == 200:
                product_soup = BeautifulSoup(product_response.content, 'html.parser')

                description_tag = product_soup.find('div', class_='woocommerce-product-details__short-description')
                description = description_tag.text.strip()

                stock_tag = product_soup.find('p', class_='stock')
                stock_info = stock_tag.text.strip()

            product_instance = Product(title, price, description, stock_info)
            product_list.append(product_instance)
        return product_list