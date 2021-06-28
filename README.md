

## Backend

    Requirements:
        Ensure the following python packages are installed:

            pip install opencv-contrib-python
            pip install numpy
            pip install tensorflow
            pip install flask
            pip install flask_restful
            pip install flask_cors

    Uses TensorFlow to create a Neural Network
        - run train.py to create a neural network model that is saved to file under the 'model' directory

        place images in the following structure
        images
            <class_directory>
                <images of particular ingredient>

    WebServer running API written using Flask
        post images to the classifier and it will return the ingredient it finds and a selection of recipes

    Create a file called edamam.conf and ensure it has contents similar to this:
    {
        "api_key": "<edamam api keyt here",
        "api_app": "<edamam api keyt here">"
    }
    

## FrontEnd

    Built using ReactJS


