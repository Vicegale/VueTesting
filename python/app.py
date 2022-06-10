import flask
import redis
import json

# Create the Flask application
app = flask.Flask(__name__)

#Health check endpoint
@app.route('/health')
def health():
    return 'OK'

#/items GET request
@app.route('/items', methods=['GET'])
def get_items():
    #get items from redis
    r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)
    items = r.lrange('items', 0, -1)
    return json.dumps(items)

#/items POST request
@app.route('/postitem', methods=['GET'])
def add_item():
    #get items from redis
    r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)
    #json stringify
    item = json.dumps({'name':'Boots of Haste', 'stats': ['+10% speed', '+10% movement speed']})
    r.rpush('items', item)
    return item

#Run the flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

