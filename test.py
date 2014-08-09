import os
import glob
import unittest

from generate import *

# The file that contains json data
plugin_file = "plugins.json"

# The directory which contains plugin files
plugin_dir = "plugins"

class GenerateTestCase(unittest.TestCase):
    """Run tests"""

    def test_generate_json(self):
        """
        Generates the json data from all the plugins
        and asserts that all plugins are accounted for.
        """

        print("\n#########################################\n")

        build_json()

        # Load the json file
        plugin_json = json.load(open(plugin_file, "r"))["plugins"]

        # All top level directories in plugin_dir
        plugin_folders = os.walk(plugin_dir).next()[1]

        # Number of entries in the json should be equal to the
        # number of folders in plugin_dir
        self.assertEqual(len(plugin_json), len(plugin_folders))

    def test_generate_zip(self):
        """
        Generates zip files for all folders and asserts
        that all folders are accounted for.
        """

        print("\n\n#########################################\n")

        zip_files()

        # All zip files in plugin_dir
        plugin_zips = glob.glob(os.path.join(plugin_dir,"*.zip"))

        # All top level directories in plugin_dir
        plugin_folders = os.walk(plugin_dir).next()[1]

        # Number of folders should be equal to number of zips
        self.assertEqual(len(plugin_zips), len(plugin_folders))

    def test_valid_json(self):
        """
        Asserts that the json data contains all the fields
        for all the plugins.
        """

        print("\n#########################################\n")

        build_json()

        # Load the json file
        plugin_json = json.load(open(plugin_file, "r"))["plugins"]

        # All plugins should contain all required fields
        for module_name, data in plugin_json.items():
            assert(isinstance(data['name'], unicode))
            assert(isinstance(data['api_version'], unicode))
            assert(isinstance(data['author'], unicode))
            assert(isinstance(data['downloads'], int))
            assert(isinstance(data['description'], unicode))

if __name__ == '__main__':
    unittest.main()
