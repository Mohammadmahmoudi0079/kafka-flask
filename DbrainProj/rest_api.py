from flask import Flask, send_file,url_for
import json
import os

app = Flask(__name__)

def load_data():
    with open('product_data.json', 'r') as f:
        data = json.load(f)
    return data


@app.route('/', methods=['GET'])
def get_data():
    data = load_data()
    json_data = json.dumps(data,indent=4)
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Product Informations</title>
    </head>
    <body>
        <a href="{url_for('download')}">Download JSON file</a>
        <pre>{json_data}</pre>
    </body>
    </html>
    '''


@app.route('/download', methods=['GET'])
def download():
    filename = 'product_data.json' 
    json_file_path = os.path.join(app.root_path, filename)  
    return send_file(json_file_path, as_attachment=True)
    


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001)
