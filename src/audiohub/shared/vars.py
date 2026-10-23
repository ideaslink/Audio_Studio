"""
parameters and environment vars

__author__ = "vci"
__copyright__ = "Copyright 2026, vci"
__license__ = "MIT"
__version__ = "1.0.0.10"
__maintainer__ = "vci"
__email__ = "contact@hsharp.com"
__status__ = "development"
__reference__ = "vci"

"""

"""
Breeze Blue environment variables
These variables are used to configure the Breeze Blue client

You need to set these variables in your environment, e.g. 

    # for Windows
    setx BREEZE_API_KEY "YOUR_BreezeBlue_API_KEY"

    # for Linux or MacOS
    export BREEZE_API_KEY="YOUR_BreezeBlue_API_KEY"

The above setup is to avoid revealing sensitive information in your codebase.
"""

BREEZE_BLUE_VARS = {
    "API_KEY": "BREEZE_API_KEY"
}
