from flask import Flask
from flask import render_template
from flask import request

from gcs_utils import make_signed_upload_url

app = Flask(__name__)


@app.route("/gen_signed_url")
def gen_signed_url():
    file_name = request.args.get('n')
    file_type = request.args.get('t')
    signed_url = make_signed_upload_url('mabuy-product', file_name, content_type=file_type)
    return signed_url


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
