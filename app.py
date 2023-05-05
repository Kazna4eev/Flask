from flask import Flask, jsonify, request

app = Flask(__name__)


products = []


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({'products': products})


@app.route('/products', methods=['POST'])
def post_product():

    name = request.json.get('name')
    description = request.json.get('description')
    price = request.json.get('price')


    if not name or not description or not price:
        return jsonify({'error': 'Invalid data'}), 400


    product = {'name': name, 'description': description, 'price': price}
    products.append(product)

    return jsonify({'message': 'Product added successfully', 'product': product}), 201

if __name__ == '__main__':
    app.run(debug=True)
