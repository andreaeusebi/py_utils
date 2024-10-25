# py_utils

Python3 modules providing general utilies and functions.

## Installation

Run following command (set the proper path to the py_utils/ folder):

``` 
python3 -m pip install -e /home/andrea/my_repos/py_utils
``` 

## Usage

In a Python script simply import and then use the module you need as follows:

``` 
import py_utils.log

...

py_utils.log.getCustomLogger(...)
``` 


## VSCode setup to avoid Import errors

1. Open Command Palette with _Ctrl+Shift+P_.
2. Select _Preferences: Open Workspace Settings_.
3. Scroll until _Python_ section.
4. Look for _Auto Complete: Extra Paths_ and click on _Edit in settings.json_.
5. In the field _python.autoComplete.extraPaths_ add the path to the py_utils/ folder.