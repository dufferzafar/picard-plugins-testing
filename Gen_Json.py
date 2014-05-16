#!python3

# Imports
import os, json, re

# Used to extract information from plugin files
def getPluginData(filePath):
  plugData = {}

  with open(filePath) as f:
    for line in f:
      name = re.match(r'PLUGIN_NAME = (.*)', line)
      author = re.match(r'PLUGIN_AUTHOR = (.*)', line)
      desc = re.match(r'PLUGIN_DESCRIPTION = (.*)', line)
      ver = re.match(r'PLUGIN_VERSION = (.*)', line)
      apiver = re.match(r'PLUGIN_API_VERSIONS = (.*)', line)

      if name:
        plugData['title'] = name.group(1)
      if author:
        plugData['author'] = author.group(1)
      if desc:
        plugData['desc'] = desc.group(1)
      if ver:
        plugData['ver'] = ver.group(1)
      if apiver:
        plugData['apiver'] = apiver.group(1)

  return plugData

# Constants
plug_dir = "Plugins"

# Variables
plugins = []

# Walk in a park
for dirName in os.listdir(plug_dir):

  files = []

  for fileName in os.listdir(os.path.join(plug_dir, dirName)):
    ext = os.path.splitext(fileName)[1]

    if ext not in [".pyc"]:
      files.append(fileName)

      if fileName == "__init__.py":
        data = getPluginData(os.path.join(plug_dir, dirName, fileName))


  if data:
    data['name'] = dirName
    data['files'] = files
    plugins.append(data)

  else:
    plugins.append({
      "name" : dirName,
      "files" : files
      })

print(json.dumps({ "plugins": plugins }, sort_keys=True, indent=2))
