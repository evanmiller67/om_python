#/usr/bin/env python3
"""
title: comments.py
author: exm540
date (created): 2019-09-16
date (updated): 2019-09-16
"""

## Start of all the things
## Bash to create this file: 
printf "#/usr/bin/env python3 \n\"\"\"\ntitle: filename.py\nauthor: $(whoami)\ndate(created): $(date "+%Y-%m-%d %H:%M:%S %Z")\ndate (updated): $(date "+%Y-%m-%d %H:%M:%S %Z")\n\"\"\"\n\n" >> $1.py
