import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.preprocessing import LabelEncoder

application = Flask(__name__) #Initialize the flask App
model = pickle.load(open('model.pkl', 'rb'))

@application.route('/')
def home():
    return render_template('index.html')

@application.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = np.array([[int(x) for x in request.form.values()]])
    prediction = model.predict(features)
    

    output = [np.argmax(prediction)]
    
    if output == [1]:
        return render_template('index.html', prediction_text='Your Stress Level is Normal')
    elif output == [0]:
        return render_template('index.html', prediction_text='Your Stress Level is Low...')
    else:
        return render_template('index.html', prediction_text='Your Stress Level is High..! ')


if __name__ == "__main__":
    application.run(debug=True)


#https://images.squarespace-cdn.com/content/v1/5ea41ebb94c41a2df14cb3ee/1605658400008-RXR027AYW0X2GVZ12UWX/Breathe.png