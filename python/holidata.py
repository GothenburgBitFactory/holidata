#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Holidata - generate holidata files.

Usage:
  holidata.py (--year=<value>) (--locale=<value>) [--output=<value>]

Options:
    --year=<value>       Specify which year to generate data for.
    --locale=<value>     Specify the locale for which data should be generated.
    --output=(csv|json)  Specify the output format [default: csv].

Dependencies:
    pip3 install arrow docopt
"""

import sys

from docopt import docopt

from emitters import *
from holidays import *

if __name__ == '__main__':
    args = docopt(__doc__)

    locales = [cls for cls in Locale.plugins if cls.locale == args['--locale']]

    if not locales:
        sys.exit("No plugin found for locale: {}".format(args['--locale']))

    locale = locales[0](int(args['--year']))

    emitters = [cls for cls in Emitter.plugins if cls.type == args['--output']]

    if not emitters:
        sys.exit("Unsupported output format: {}".format(args['--output']))

    emitter = emitters[0]()

    print(emitter.output(locale))
