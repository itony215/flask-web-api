from flask import Flask,jsonify,request
app = Flask(__name__)
stores = [{
    'name': 'Elton first store',
    'items': [{'name':'my item 1', 'price': 30 }],
    },
    {
    'name': 'Elton second store',
    'items': [{'name':'my item 2', 'price': 15 }],
    },
]
#post /store data: {name :}
@app.route('/predict' , methods=['POST'])
def upload_image():
    if request.method == 'POST' and request.files['image']:
        img = request.files['image']
        return '20'
    else:
    	  return "Where is the image?"
#get /store
@app.route('/store')
def get_stores():
    return jsonify(stores)
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        return jsonify ({'message': 'store not found'})
#get /store/<name>/item data: {name :}
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify( {'items':store['items'] } )
    return jsonify ({'message':'store not found'})


app.run(port=5000, debug=True)