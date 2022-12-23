from flask import Flask
from redis import Redis
import requests
import json
import socket

with open('./config.json') as json_config_file:
        config_data = json.load(json_config_file)

server_host = config_data['SERVER_HOST']
server_port = config_data['SERVER_PORT']
time = config_data['TIME']
coin_name = config_data['COIN_NAME']
api_route = config_data['API_ROUTE'] + coin_name
redis_host = config_data['REDIS_HOST']
redis_port = config_data['REDIS_PORT']

app = Flask(__name__)
redis = Redis(host=redis_host, port=redis_port)


@app.route('/')
def get_price():
    if not redis.get(coin_name):
        input_data = requests.get(api_route).json()
        price = input_data[0]['current_price']
        redis.setex(coin_name, time, price)
    price = redis.get(coin_name).decode("utf-8") 
    return {'name': coin_name, 'price': price, 'host':  socket.gethostname()}

if __name__ == "__main__":

    app.run(debug=True, host=server_host, port=server_port)
