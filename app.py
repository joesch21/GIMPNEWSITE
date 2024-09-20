import os
import random
from flask import Flask, jsonify, render_template, send_from_directory

app = Flask(__name__)

# Function to get a random image from the static/images folder
def get_random_image():
    image_folder = os.path.join(app.static_folder, 'images')
    images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    if images:
        return random.choice(images)  # Select a random image from the list
    return None

# Route to handle NFT generation and select a random image
@app.route('/generate_nft')
def generate_nft():
    random_image = get_random_image()
    if random_image:
        image_url = f"/static/images/{random_image}"  # Return the image URL only
        return jsonify(image_path=image_url)  # Only return the image path as JSON
    else:
        return jsonify(message="No images found"), 404

# Serving the background image (for the About page or other purposes)
@app.route('/background/<filename>')
def serve_background_image(filename):
    return send_from_directory(os.path.join(app.static_folder, 'background'), filename)

# Basic routes for rendering templates
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about_artist')
def about_artist():
    return render_template('about_artist.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/rarity_score')
def rarity_score():
    return render_template('rarity_score.html')

@app.route('/favicon.ico')
def favicon():
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
