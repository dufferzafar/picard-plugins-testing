# Testing ground for Picard's Plugin Delivery System

Apart from a folder that contains sample plugins, the repo contains two main scripts.

## GenJSON:

This script can create a json file from a folder of plugins. It reads the plugin files to extract information such as Author and Title from them, and creates a json with all that data. The json also contains the MD5 hashes of all the files used.

## PluginAPI:

The json generated above is loaded and served as via Flask.

It supports the following endpoints:

```
/plugins 

  Lists all the plugins

/plugins?id=<plugid>

  List a specific plugin whose id matches with <plugid>

/download?id=<plugid>

  Increments the download count and initiates download of a plugin.
  If a plugin contains a single file, it is served as is, whereas if there are
  multiple files, they are compressed in a zip and are then served.
```
