from flask import Flask, render_template, request, jsonify
from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def do_sum():
    num_1 = request.form['num1']
    num_2 = request.form['num2']
    output = str(int(num_1) * int(num_2))
    if num_1 and num_2:
        image = cv2.imread("./static/background.png")

        # Convert to PIL Image
        cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_im = Image.fromarray(cv2_im_rgb)

        draw = ImageDraw.Draw(pil_im)

        # Choose a font
        font = ImageFont.truetype("tahoma.ttf", 50)

        # Draw the text
        draw.text((0, 0), output, font=font)

        # Save the image
        cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
        cv2.imwrite("./static/result.png", cv2_im_processed)

        return jsonify({'output':output})
    return jsonify({'error':'Missing data!'})

if __name__ == '__main__':
    app.run()
