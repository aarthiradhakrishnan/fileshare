import os
from flask import Flask, render_template, request, send_file,redirect

app = Flask(__name__)

@app.route('/')
def index():
    filenames = os.listdir('./static/files/')
    return render_template('index.html', filenames=filenames)

@app.route('/download/<filename>')
def download(filename):
    path= os.path.join('./static/files/', filename)
    return send_file(path, as_attachment=True)
    
if __name__ == '__main__':
    app.run(debug=True)