# Import Libraries below
# Program to Upload Color Image and convert into Black & White image
import os
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
# import additional libraries below
import cv2
import numpy as np

app = Flask(__name__)

# Open and redirect to default upload webpage
@app.route('/')
def upload_form():
    return render_template('upload.html')

# Function to upload image and redirect to new webpage
@app.route('/', methods=['POST'])
def upload_video():
    file = request.files['file']
    filename = secure_filename(file.filename)
    # write the read and write function on image below 
    file.save(os.path.join('static/', filename))

        # ends here

    return render_template('upload.html', filename=filename)

@app.route('/display/<filename>')
def display_video(filename):
    return redirect(url_for('static', filename=filename))


if __name__ == "__main__":
    app.run(debug=True)
