import os
import random
from flask import Flask, jsonify, render_template, send_from_directory

app = Flask(__name__)

# Function to get a random image from the static/images folder
def get_random_image():
    image_folder = os.path.join(app.static_folder, 'images')
    images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    return random.choice(images) if images else None

# Route to generate NFT and return a random image URL
@app.route('/generate_nft')
def generate_nft():
    random_image = get_random_image()
    if random_image:
        image_url = f"/static/images/{random_image}"
        return jsonify(image_path=image_url)
    return jsonify(message="No images found"), 404

# Serving background images
@app.route('/background/<filename>')
def serve_background_image(filename):
    return send_from_directory(os.path.join(app.static_folder, 'background'), filename)

# Basic routes for rendering templates
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nft_voting_proposal')
def nft_voting_proposal():
    return render_template('nft_voting_proposal.html')

if __name__ == "__main__":
    app.run(debug=True)
