# Import necessary libraries
from flask import Flask, render_template, request
import numpy as np
import os
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = 'C:/Users/justm/AppData/Local/Programs/Python/Python311/Plant-Leaf-Disease-Prediction-main/model.h5'
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")


def pred_tomato_dieas(tomato_plant):
    test_image = load_img(tomato_plant, target_size=(128, 128))  # load image
    print("@@ Got Image for prediction")

    # convert image to np array and normalize
    test_image = img_to_array(test_image)/255
    # change dimention 3D to 4D
    test_image = np.expand_dims(test_image, axis=0)

    result = model.predict(test_image)  # predict diseased palnt or not
    print('@@ Raw result = ', result)

    pred = np.argmax(result, axis=1)
    print(pred)
    if pred == 0:
        return "Tomato - Bacteria Spot Disease", 'Tomato-Bacteria Spot.html'

    elif pred == 1:
        return "Tomato - Early Blight Disease", 'Tomato-Early_Blight.html'

    elif pred == 2:
        return "Tomato - Healthy and Fresh", 'Tomato-Healthy.html'

    elif pred == 3:
        return "Tomato - Late Blight Disease", 'Tomato - Late_blight.html'

    elif pred == 4:
        return "Tomato - Leaf Mold Disease", 'Tomato - Leaf_Mold.html'

    elif pred == 5:
        return "Tomato - Septoria Leaf Spot Disease", 'Tomato - Septoria_leaf_spot.html'

    elif pred == 6:
        return "Tomato - Target Spot Disease", 'Tomato - Target_Spot.html'

    elif pred == 7:
        return "Tomato - Tomoato Yellow Leaf Curl Virus Disease", 'Tomato - Tomato_Yellow_Leaf_Curl_Virus.html'

    elif pred == 8:
        return "Tomato - Tomato Mosaic Virus Disease", 'Tomato - Tomato_mosaic_virus.html'

    elif pred == 9:
        return "Tomato - Two Spotted Spider Mite Disease", 'Tomato - Two-spotted_spider_mite.html'


potato_model_path = 'C:/Users/justm/AppData/Local/Programs/Python/Python311/Plant-Leaf-Disease-Prediction-main/model1.h5'
potato_model = load_model(potato_model_path)
print(potato_model)
print("Model Loaded Successfully")


def pred_potato_disease(potato_plant):
    test_image = load_img(potato_plant, target_size=(128, 128))  # load image
    print("@@ Got Image for prediction")

    # convert image to np array and normalize
    test_image = img_to_array(test_image)/255
    # change dimention 3D to 4D
    test_image = np.expand_dims(test_image, axis=0)

    result = potato_model.predict(test_image)  # predict diseased palnt or not
    print('@@ Raw result = ', result)

    pred = np.argmax(result, axis=1)
    print(pred)
    if pred == 0:
        return "Potato___Early_blight", 'Potato___Early_blight.html'
    elif pred == 1:
        return "Potato___Late_blight", 'Potato___Late_blight.html'
    elif pred == 2:
        return "Potato___healthy", 'Potato___healthy.html'


cotton_model_path = 'C:/Users/justm/AppData/Local/Programs/Python/Python311/Plant-Leaf-Disease-Prediction-main/model1.h5'
cotton_model = load_model(cotton_model_path)
print(cotton_model)
print("Model Loaded Successfully")


def pred_cotton_disease(cotton_plant):
    test_image = load_img(cotton_plant, target_size=(128, 128))  # load image
    print("@@ Got Image for prediction")

    # convert image to np array and normalize
    test_image = img_to_array(test_image)/255
    # change dimention 3D to 4D
    test_image = np.expand_dims(test_image, axis=0)

    result = cotton_model.predict(test_image)  # predict diseased palnt or not
    print('@@ Raw result = ', result)

    pred = np.argmax(result, axis=1)
    print(pred)
    if pred == 0:
        return "bacterial_blight", 'Cotton - Bacterial_blight.html'
    elif pred == 1:
        return "curl_virus", 'Cotton - Leaf_Curl_Virus.html'
    elif pred == 2:
        return "fussarium_wilt", 'Cotton - Fussarium_wilt.html'
    elif pred == 3:
        return "healthy", 'Cotton - Healthy.html'


# Create flask instance
app = Flask(__name__)

# render index.html page


@app.route("/")
def home():
    return render_template('Homepage.html')


@app.route("/tomato", methods=['GET', 'POST'])
def tomato():
    return render_template('Tomato.html')


@app.route("/potato", methods=['GET', 'POST'])
def potato():
    return render_template('Potato.html')


@app.route("/cotton", methods=['GET', 'POST'])
def cotton():
    return render_template('Cotton.html')


# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['image']  # fet input
        filename = file.filename
        print("@@ Input posted = ", filename)

        file_path = os.path.join(
            'C:/Users/justm/AppData/Local/Programs/Python/Python311/Plant-Leaf-Disease-Prediction-main/static/upload/', filename)
        file.save(file_path)

        print("@@ Predicting class......")

        pred, output_page = pred_tomato_dieas(tomato_plant=file_path)
        #   pred, output_page = pred_tomato_dieas(tomato_plant=file_path)

        return render_template(output_page, pred_output=pred, user_image=file_path)


# get input image from client then predict class and render respective .html page for solution
@app.route("/predict1", methods=['GET', 'POST'])
def predict1():
    if request.method == 'POST':
        file = request.files['image']  # fet input
        filename = file.filename
        print("@@ Input posted = ", filename)

        file_path = os.path.join(
            'C:/Users/justm/AppData/Local/Programs/Python/Python311/Plant-Leaf-Disease-Prediction-main/static/upload/', filename)
        file.save(file_path)

        print("@@ Predicting class......")

        pred, output_page = pred_potato_disease(potato_plant=file_path)

        return render_template(output_page, pred_output=pred, user_image=file_path)


@app.route("/predict2", methods=['GET', 'POST'])
def predict2():
    if request.method == 'POST':
        file = request.files['image']  # get input
        filename = file.filename
        print("@@ Input posted = ", filename)

        file_path = os.path.join(
            'C:/Users/justm/AppData/Local/Programs/Python/Python311/Plant-Leaf-Disease-Prediction-main/static/upload/', filename)
        file.save(file_path)

        print("@@ Predicting class......")

        pred, output_page = pred_cotton_disease(cotton_plant=file_path)

        return render_template(output_page, pred_output=pred, user_image=file_path)


# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False, port=8080)
