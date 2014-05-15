#!python3

from flask import Flask, request, json, jsonify, abort, make_response
app = Flask(__name__)

# Load JSON Data
plugins = json.load(open("Plugins.json"))

# @app.route('/plugins', methods = ['GET'])
# def get_plugins():
#   return jsonify( plugins )

@app.route('/plugins', methods = ['GET'])
def get_plugin():

  pid = request.args.get('id', None)
  ptitle = request.args.get('title', None)

  if pid:
    plug = { 'plugin' : list(filter(lambda t: t['id'] == int(pid), plugins['plugins'])) }

  elif ptitle:
    plug = { 'plugin' : list(filter(lambda t: t['title'] == str(ptitle), plugins['plugins'])) }

  else:
    plug = plugins

  return jsonify( plug )

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Plugin not found' } ), 404)

if __name__ == '__main__':
  app.run(debug = True)
