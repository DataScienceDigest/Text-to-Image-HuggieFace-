from flask import Flask,render_template,request
import io
from PIL import Image
from IPython.display import display
from io import BytesIO
from PIL import Image
import base64
import requests


API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
headers = {"Authorization": "Bearer entertokenhere"}


app = Flask(__name__)
def query(prompt): 
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content



@app.route('/', methods=["GET", "POST"])
def index():
    image_data = None
    if request.method == 'POST':
        prompt = request.form['prompt']
        print(f"Prompt received: {prompt}")

        image_bytes = query(prompt)
        
        if image_bytes:
            # Convert image bytes to base64 to display on the HTML page
            image_base64 = base64.b64encode(image_bytes).decode('utf-8')
            image_data = f"data:image/png;base64,{image_base64}"
            return render_template('front.html', image_data=image_data)
        
    return render_template('front.html', image_data=image_data)

if __name__ == "__main__":
    app.run(debug=True)
