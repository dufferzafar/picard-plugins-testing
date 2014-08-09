# Testing ground for Picard's Plugin Delivery System

The repo contains a script `generate.py` that can create a json file from a folder of plugins. It reads the plugin files to extract information such as Author and Title from them, and creates a json with all that data. The json also contains the MD5 hashes of all the files used.

Apart from generating the json data, the script can also compress the plugin folders to zip files so they can be served easily.

Note: 

The Plugin API that used to be a part of the repo has now been [moved and merged](https://github.com/musicbrainz/picard-website/blob/master/views/api.py) into the main Picard website itself.
