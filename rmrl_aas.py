from flask import Flask, request, send_file
from tempfile import mkdtemp
import rmrl
import shutil
import logging
import os

app = Flask(__name__)


@app.route("/")
def index():
    return '''
    <form action="/render" method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=render>
    </form>
    '''


@app.route("/render", methods=['POST'])
def render():
    if 'file' not in request.files or not request.files['file'].filename.endswith('.zip'):
        return '', 400
    upload = request.files['file']
    fname = upload.filename
    tmpdir = mkdtemp()
    try:
        fpath = os.path.join(tmpdir, fname)
        upload.save(fpath)
        pdfname = fname.strip('zip') + '.pdf'
        return send_file(rmrl.render(fpath), download_name=pdfname)
    except Exception as e:
        logging.warning(e)
        return '', 500
    finally:
        shutil.rmtree(tmpdir)


if __name__ == '__main__':
    app.run(port=8080)
