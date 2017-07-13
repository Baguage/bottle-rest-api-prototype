# -*- coding: utf-8 -*-
#
# This file is part of the Bottle Rest Api Prototype.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/Baguage/bottle-rest-api-prototype
#
# This Source Code Form is subject to the terms of the MIT License.
# If a copy of theMIT License was not distributed
# with this file, You can obtain one at https://opensource.org/licenses/MIT


# Please refer to https://bottlepy.org/docs/dev/deployment.html#apache-mod-wsgi
# for additional information

import os
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

import bottle
import main
# Do NOT use bottle.run() with mod_wsgi
application = bottle.default_app()