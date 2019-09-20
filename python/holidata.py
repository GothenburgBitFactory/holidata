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


def create_locale_for(id, year):
    locales = [cls for cls in Locale.plugins if cls.locale == id]
    if not locales:
        return None
    else:
        return locales[0](year)


def create_emitter_for(output_format):
    emitters = [cls for cls in Emitter.plugins if cls.type == output_format]
    if not emitters:
        return None
    else:
        return emitters[0]()


if __name__ == '__main__':
    args = docopt(__doc__)

    locale = create_locale_for(args['--locale'], int(args['--year']))

    if locale is None:
        sys.exit("No plugin found for locale: {}".format(args['--locale']))

    emitter = create_emitter_for(args['--output'])

    if emitter is None:
        sys.exit("Unsupported output format: {}".format(args['--output']))

    print(emitter.output(locale))
