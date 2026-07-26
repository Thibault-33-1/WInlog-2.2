#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import sys

def install_pillow():

	subprocess.call("py -3 -m pip install --upgrade pip")
        subprocess.call("py -3 -m pip install --upgrade Pillow")

        print("Pillow a été installé avec succès.")


install_pillow()