#!python3

import os
import zipfile
import tempfile
from flask import Flask, request, json, jsonify, abort, make_response
app = Flask(__name__)

# Load JSON Data
plugins = json.load(open("Plugins.json"))
plug_dir = "Plugins"


def find_plugin(id):
    plug = list(filter(lambda t: t['id'] == str(id), plugins['plugins']))

    if plug:
        return plug[0]
    else:
        return None

# Todo
def increase_count(plugin):
    """
    Increments the download count and updates the json file
    """
    pass


@app.route('/plugins', methods=['GET'])
def get_plugin():
    """
    Lists data of a plugin
    """

    pid = request.args.get('id', None)
    if pid:
        if find_plugin(pid):
            plug = {'plugin': find_plugin(pid)}
        else:
            return not_found(404)
    else:
        plug = plugins

    return jsonify(plug)


@app.route('/download', methods=['GET'])
def download_plugin():
    """
    Increments count and serves files as an attachment
    """

    pid = request.args.get('id', None)
    if pid:
        if find_plugin(pid):
            files = find_plugin(pid)['files']

            if len(files) == 1:
                fileName = list(files.keys())[0]
                filePath = os.path.join(plug_dir, pid, fileName)

                response = make_response(open(filePath).read())
                response.headers["Content-Disposition"] = "attachment; filename=" + fileName
            else:
                with tempfile.SpooledTemporaryFile() as tmp:
                    with zipfile.ZipFile(tmp, "w") as archive:
                        for fileName in list(files.keys()):
                            archive.write(os.path.join(plug_dir, pid, fileName), fileName)

                    tmp.seek(0)
                    response = make_response(tmp.read())
                    response.headers["Content-Disposition"] = "attachment; filename=" + pid + ".zip"

            return response
        else:
            return not_found(404)
    else:
        return jsonify({'error': 'id not specified'})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Plugin not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
