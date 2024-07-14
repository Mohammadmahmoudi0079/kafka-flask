import time
import json
from kafka import KafkaProducer
from pullData import pull_product,Product

def serializer(product_info):
    return json.dumps(product_info).encode('utf-8')

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer= serializer
)
product_list = pull_product()
if __name__=='__main__':
    for item in product_list:
        producer.send('product',Product.to_dict(item))
        print(item)
        time.sleep(1)