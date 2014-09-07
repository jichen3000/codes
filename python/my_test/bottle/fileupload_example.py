from bottle import route, run, request, static_file
import os


@route("/")
def main_html():
    return static_file('fileupload.html', root='./')

@route('/upload', method='POST')
def do_upload():
    category = request.forms.get('category')
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return "File extension not allowed."

    save_path = "./"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    upload.save(file_path)
    return "File successfully saved to '{0}'.".format(file_path)

run(host='localhost', port=9999,reloader=True)
