# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

import os
from app import app

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 3030))
	app.run(host='localhost', port=port)
