from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack, send_from_directory, jsonify

import json
import datetime
import print_helper

app = Flask(__name__, static_url_path='') 


@app.route("/")
def index():
    print(app.config)
    # return "Hello World!"
    # return app.send_static_file('index.html')
    # config = {
    #     "username":"admin",
    #     "ip": "10.160.19.45"
    # }
    return send_from_directory("","fileupload_jquery.html")

@app.route('/api/v1/fgt_config_file', methods=["post"])
def save_fgt_config_file():
    # check if the post request has the file part
    # if 'file' not in request.files:
    #     flash('No file part')
    #     return redirect(request.url)
    file = request.files['file']
    file.p()
    return ""
    # if user does not select file, browser also
    # submit a empty part without filename
    # if file and file.filename:
    #     filepath = os.path.join("saved_files","fgt_configs", file.filename)
    #     file.save(filepath)
    #     return jsonify({'data': {'real_path':filepath, 'file_name':file.filename},
    #             'status':DataStatus.SUCCESS.value})
    # else:
    #     return jsonify({'msg': "upload file has issue!",'status':DataStatus.FAILED.value})


if __name__ == '__main__':
    app.run(debug=True)
