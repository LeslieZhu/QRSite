#!/usr/bin/env python
# encoding: utf-8

from __future__ import absolute_import

import sys

#if __package__ == '':
import os
path = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, path)


import qrsite

if __name__ == "__main__":
    import sys
    sys.exit(qrsite.main())
