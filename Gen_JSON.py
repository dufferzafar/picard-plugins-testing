# Imports
import os
import json
import re
import hashlib
import subprocess
import os


def get_data(filePath):
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


def build_json():
    """
    Traverse the plugins directory to generate json data.
    """

    for dirName in os.listdir(plugDir):

        files = {}
        data = {}

        for fileName in os.listdir(os.path.join(plugDir, dirName)):
            ext = os.path.splitext(fileName)[1]

            if ext not in [".pyc"]:
                files[fileName] = hashlib.md5(open(os.path.join(plugDir, dirName,
                                                                fileName), "rb").read()).hexdigest()

            if not data:
                data = get_data(os.path.join(plugDir, dirName, fileName))

        found = False
        for p in plugins:
            if p["id"] == dirName:
                found = True
                break

        if found:
            print("Updating " + dirName)
            if data:
                for key, value in data.items():
                    p[key] = value
            p["files"] = files
        else:
            print("Adding " + dirName)
            data['id'] = dirName
            data['files'] = files
            data['downloads'] = 0
            plugins.append(data)

# Pull contents from Github
# subprocess.call(["git", "pull", "-q"])

plugDir = "Plugins"
outFile = "Plugins.json"

if os.path.isfile(outFile):
    plugins = json.load(open(outFile, "r"))["plugins"]
else:
    plugins = []

build_json()

# print(json.dumps({"plugins": plugins}, sort_keys=True, indent=2))
json.dump({"plugins": plugins}, open(outFile, "w"), sort_keys=True, indent=2)
