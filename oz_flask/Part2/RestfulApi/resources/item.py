from flask_restful import Resource
from flask import request

items = []

class Item(Resource):
    def get( self , name):
        for item in items:
            if item['name'] == name:
                return item

        return {"message": "Item not found"}

    def post( self , name):
        for item in items:
            if item['name'] == name:
                return {"message": "Item already exists"}, 400

        data = request.get_json()

        new_item = {'name': name, 'price' : data['price']}
        items.append(new_item)

        return new_item

    def put( self, name ):
        data = request.get_json()

        for item in items:
            if item['name'] == name:
                item['price'] = data['price']
                return item

        new_item = {'name': name, 'price' : data['price']}
        items.append(new_item)

        return new_item

    def delete( self , name):
        global items

        items = [item for item in items if item['name'] != name]

        return {"message": "Item deleted"}