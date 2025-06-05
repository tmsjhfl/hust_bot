# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""
Python module serving as a project/extension template.
"""

# Register Gym environments.
from .tasks import *

# Register UI extensions.
from .ui_extension_example import *

import os

HUST_BOT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HUST_BOT_ENV_DIR = os.path.join(HUST_BOT_ROOT, "source", "hust_bot", "hust_bot")
