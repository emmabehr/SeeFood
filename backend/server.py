import sys
from flask import Flask, json, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS

import classify
import edamam

app = Flask(__name__)
api = Api(app)
CORS(app)

no_ingredients = [{}]

class ClassifyIngredients(Resource):
    def get(self):
        labels = classify.getLabels()
        print(labels)
        return jsonify(labels)

    def post(self):
        for x in request.files:
            print(x)
        if 'image' not in request.files:
            print("No image found")
            return jsonify(no_ingredients)
        else:
            try:
                image = request.files.get('image')
                classification = classify.classify(image.read())
                print(classification)
                if classification is None:
                    return jsonify(no_ingredients)
                else:
                    recipes = edamam.searchByIngredient(classification)
                    result = [{'ingredient': classification, 'recipes': recipes}]
                    return result
                    #return jsonify([{'ingredient': classification}])
            except:
                print(sys.exc_info())
                return jsonify(no_ingredients)
            

api.add_resource(ClassifyIngredients, '/classify/')

if __name__ == '__main__':
    app.run(debug=True)