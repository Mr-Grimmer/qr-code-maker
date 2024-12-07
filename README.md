# QR Code Generator Project

## Overview
This project is a web application built with **Flask** that allows users to generate QR codes based on input data. Users can customize the QR code's foreground and background colors and download the generated QR code image.

## Features
- **QR Code Generation**: Create a QR code from any text or URL.
- **Custom Color Options**: Set custom foreground (fill) and background colors using color names or hex codes.
- **Downloadable Image**: The generated QR code is available for download in PNG format.
- **Responsive Design**: The interface is user-friendly and responsive for various screen sizes.

## Technologies Used
- **Python**: The backend logic is implemented using Flask.
- **HTML/CSS/JavaScript**: Used for creating the frontend.
- **qrcode**: Python library for generating QR codes.
- **Pillow**: Python Imaging Library for handling image processing.
- **webcolors**: Used for converting color names to hex codes.

## Project Structure
```
/qr_code_project
├── app.py            # Main Flask application file
├── templates/
│   └── index.html    # HTML template for the frontend
└── static/
    ├── css/
    │   └── styles.css  # Custom CSS for styling the web page
    └── js/
        └── scripts.js  # JavaScript for frontend interactivity
```

## Installation
To set up and run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/qr_code_project.git
   cd qr_code_project
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install Flask qrcode[pil] Pillow webcolors
   ```

4. **Run the Flask app**:
   ```bash
   python app.py
   ```

5. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:5000/`

## Usage
1. **Enter Data**: Type the URL or text you want to encode into the input field.
2. **Set Colors**: Optionally set custom colors for the QR code's foreground and background.
3. **Generate**: Click the "Generate QR Code" button.
4. **Download**: Once generated, the QR code image will appear with an option to download.

## Example
**Input**:
- Data: `https://example.com`
- Fill Color: `#FF5733`
- Background Color: `#FFFFFF`

**Output**:
- A downloadable PNG image of the QR code.

## Customization
- **Color Customization**: Supports hex codes (e.g., `#FF5733`) and color names (e.g., `red`).
- **Responsive Design**: The interface adjusts to different screen sizes, making it easy to use on both desktop and mobile.

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -am 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a pull request.

## License
This project is open-source and available under the [MIT License](LICENSE).
