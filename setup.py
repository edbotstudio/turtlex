#
# Python convenience functions to control turtle window appearance and behaviour.
#
# Copyright (c) Robots in Schools Ltd. All rights reserved.
#

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setuptools.setup(
	name = "turtlex",
	version = "1.0.3",
	description = "Python convenience functions to control turtle window appearance and behaviour",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url = "https://github.com/edbotstudio/turtlex",
	project_urls = {
		"Bug Tracker": "https://github.com/edbotstudio/turtlex/issues"
	},
	author = "Clive Haworth",
	author_email = "clive@ed.bot",
	license = "MIT",
	packages = [ "turtlex" ],
	package_dir = { "turtlex": "src" },
	python_requires= ">=3",
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent"
	]
)