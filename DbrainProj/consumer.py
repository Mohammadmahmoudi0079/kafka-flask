import json
from kafka import KafkaConsumer
from json_fixer import fix_json_format

def save_to_file(data, file_name='topic_data.json'):
    with open(file_name, 'a') as file:
        file.write(json.dumps(data) + '\n')

def process_data_from_kafka():
    consumer = KafkaConsumer(
        'product',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
    )
    try:
        for item in consumer:
            try:
                product_data = json.loads(item.value)
                print(product_data)
                save_to_file(product_data)
            except json.JSONDecodeError as je:
                print(f"JSON decoding error: {je}")
                continue 
    except Exception as e:
        print(f"Exception occurred: {e}")
    finally:
        consumer.close()
        fix_json_format('topic_data.json', 'product_data.json')

if __name__ == '__main__':
    process_data_from_kafka()
