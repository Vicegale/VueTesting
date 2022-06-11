import flask
import rejson
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
    r = rejson.Client(host='redis', port=6379, db=0, decode_responses=True)
    items = r.jsonget('items')
    #set response content type
    #set access control headers
    headers = {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}
    response = flask.Response(json.dumps(items), status=200, headers=headers)
    return response

#/items POST request
@app.route('/items', methods=['POST'])
def add_item():
    #get items from redis
    r = rejson.Client(host='redis', port=6379, db=0, decode_responses=True)
    #json stringify
    item = flask.request.get_json()
    r.jsonarrappend('items', rejson.Path.rootPath(), item)
    return item

#Run the flask application
if __name__ == '__main__':
    r = rejson.Client(host='redis', port=6379, db=0, decode_responses=True)
    if(not r.exists('items')):
        r.jsonset('items', rejson.Path.rootPath(), [])
    app.run(host='0.0.0.0', debug=True)

