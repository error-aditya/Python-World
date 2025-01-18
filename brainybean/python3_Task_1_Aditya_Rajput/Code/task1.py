from flask import Flask, request, render_template_string
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# file extensions for each folder
ALLOWED_PDF_EXTENSIONS = {'pdf'}
ALLOWED_DOCX_EXTENSIONS = {'docx'}
ALLOWED_IMAGE_EXTENSIONS = {'jpg', 'png'}

# Folder paths
PDF_FOLDER = 'pdf'
DOC_FOLDER = 'doc'
IMAGE_FOLDER = 'image'

# it will create directories if they do not exist
for folder in [PDF_FOLDER, DOC_FOLDER, IMAGE_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Function will check the file extension
def allowed_file(filename, extension_set):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extension_set

# Route for file upload form
@app.route('/')
def upload_form():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head><title>Upload File</title></head>
        <body>
            <h1>Upload a file</h1>
            <form method="POST" enctype="multipart/form-data">
                <input type="file" name="file">
                <button type="submit">Upload</button>
            </form>
        </body>
        </html>
    ''')

# Route to handle file upload
@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file', 400

    filename = secure_filename(file.filename)

    if allowed_file(filename, ALLOWED_PDF_EXTENSIONS):
        file.save(os.path.join(PDF_FOLDER, filename))
        return f'File saved in {PDF_FOLDER} folder', 200
    elif allowed_file(filename, ALLOWED_DOCX_EXTENSIONS):
        file.save(os.path.join(DOC_FOLDER, filename))
        return f'File saved in {DOC_FOLDER} folder', 200
    elif allowed_file(filename, ALLOWED_IMAGE_EXTENSIONS):
        file.save(os.path.join(IMAGE_FOLDER, filename))
        return f'File saved in {IMAGE_FOLDER} folder', 200
    else:
        return 'Invalid file type', 400

if __name__ == '__main__':
    app.run(debug=True)
