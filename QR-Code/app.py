from flask import Flask, request, jsonify, send_file, render_template
import qrcode as qr
from PIL import Image
import io
import webcolors

app = Flask(__name__)

# Function to validate hex color codes
def is_valid_color(color):
    """Check if the color is a valid hex color code."""
    return len(color) == 7 and color.startswith("#") and all(c in "0123456789ABCDEFabcdef" for c in color[1:])

# Function to convert color name to hex code
def color_name_to_hex(color_name):
    """Convert a color name to a hex code."""
    try:
        return webcolors.name_to_hex(color_name)
    except ValueError:
        return None  # Return None if the color name is invalid

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    try:
        if request.is_json:
            data = request.json.get('data', '').strip()
            fill_color = request.json.get('fill_color', '#000000').strip()
            back_color = request.json.get('back_color', '#FFFFFF').strip()
        else:
            data = request.form.get('data', '').strip()
            fill_color = request.form.get('fill_color', '#000000').strip()
            back_color = request.form.get('back_color', '#FFFFFF').strip()

        if not data:
            return jsonify({'error': 'Data for QR code is required'}), 400

        # Convert color names to hex codes if needed
        if not is_valid_color(fill_color):
            hex_color = color_name_to_hex(fill_color)
            if hex_color:
                fill_color = hex_color
            else:
                fill_color = '#000000'  # Default black
        if not is_valid_color(back_color):
            hex_color = color_name_to_hex(back_color)
            if hex_color:
                back_color = hex_color
            else:
                back_color = '#FFFFFF'  # Default white

        # Generate QR Code
        code = qr.QRCode(
            version=1,
            error_correction=qr.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        code.add_data(data)
        code.make(fit=True)

        img = code.make_image(fill_color=fill_color, back_color=back_color)

        # Save to a BytesIO stream
        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)

        return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='qrcode.png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
