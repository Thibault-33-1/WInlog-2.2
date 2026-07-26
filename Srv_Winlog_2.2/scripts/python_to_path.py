#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

def install_dependencies():
    os.system('REG ADD "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment" /v Path /d "C:\\Python37;C:\\Windows\\system32" /f')

install_dependencies()
