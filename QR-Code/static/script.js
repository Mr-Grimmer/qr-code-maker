function isValidHexColor(color) {
    return /^#([0-9A-Fa-f]{6})$/.test(color);
}

const form = document.getElementById('qrForm');
const qrImage = document.getElementById('qrImage');
const downloadBtn = document.getElementById('downloadBtn');
const resultDiv = document.getElementById('result');
const errorMsg = document.getElementById('errorMsg');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = document.getElementById('data').value;
    let fillColor = document.getElementById('fillColor').value || '#000000';
    let backColor = document.getElementById('backColor').value || '#FFFFFF';

    if (!isValidHexColor(fillColor) && fillColor !== 'red' && fillColor !== 'blue' && fillColor !== 'green' && fillColor !== 'black' && fillColor !== 'white') {
        alert('Invalid fill color. Using default #000000 (black).');
        fillColor = '#000000';
    }
    if (!isValidHexColor(backColor) && backColor !== 'red' && backColor !== 'blue' && backColor !== 'green' && backColor !== 'black' && backColor !== 'white') {
        alert('Invalid background color. Using default #FFFFFF (white).');
        backColor = '#FFFFFF';
    }

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data, fill_color: fillColor, back_color: backColor })
        });
        const blob = await response.blob();
        if (response.ok) {
            qrImage.src = URL.createObjectURL(blob);
            qrImage.style.display = 'block';
            downloadBtn.style.display = 'inline-block';
            resultDiv.style.display = 'block';
            errorMsg.style.display = 'none';
        } else {
            throw new Error(await response.text());
        }
    } catch (error) {
        errorMsg.textContent = error.message;
        errorMsg.style.display = 'block';
        resultDiv.style.display = 'none';
    }
});
