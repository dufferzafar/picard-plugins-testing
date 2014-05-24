#!python3

# Imports
import os
import json
import re
import hashlib
import subprocess

def getPluginData(filePath):
    """
    Extract usable information from plugin files.
    """
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

plug_dir = "Plugins"
plugins = []

# Pull contents from Github
# subprocess.call(["git", "pull", "-q"])

# Traverse the plugins dir to create JSON
for dirName in os.listdir(plug_dir):

    files = {}
    data = {}

    for fileName in os.listdir(os.path.join(plug_dir, dirName)):
        ext = os.path.splitext(fileName)[1]

        if ext not in [".pyc"]:
            files[fileName] = hashlib.md5(open(os.path.join(plug_dir, dirName,
                                            fileName), "rb").read()).hexdigest()

        if not data:
            data = getPluginData(os.path.join(plug_dir, dirName, fileName))

    if data:
        data['id'] = dirName
        data['files'] = files
        plugins.append(data)

    else:
        plugins.append({"id": dirName, "files": files})

# print(json.dumps({ "plugins": plugins }, sort_keys=True, indent=2))
json.dump({"plugins": plugins}, open("Plugins.json", "w"), sort_keys=True, indent=2)
