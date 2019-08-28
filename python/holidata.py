#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Holidata - generate holidata files.

Usage:
  holidata.py (--year=<value>) (--locale=<value>)

Options:
    --year=<value>       Specify which year to generate data for.
    --locale=<value>     Specify the locale for which data should be generated.

Dependencies:
    pip3 install arrow docopt
"""

import sys
from docopt import docopt

from countries import *

if __name__ == '__main__':
    args = docopt(__doc__)
    class_candidates = [cls for cls in Country.plugins if cls.locale == args['--locale']]

    if class_candidates:
        country = class_candidates[0](int(args['--year']))
        print(country.to_csv())
    else:
        sys.exit("No plugin found for locale: {}".format(args['--locale']))
