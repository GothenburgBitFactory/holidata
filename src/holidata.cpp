////////////////////////////////////////////////////////////////////////////////
//
// Copyright 2010 - 2016, Paul Beckingham, Federico Hernandez.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included
// in all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
// OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
// THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
//
// http://www.opensource.org/licenses/mit-license.php
//
////////////////////////////////////////////////////////////////////////////////

#include <cmake.h>
#include <Args.h>
#include <Datetime.h>
#include <iostream>

////////////////////////////////////////////////////////////////////////////////
int main (int argc, const char** argv)
{
  int status = 0;

  try
  {
    // Process arguments.
    Args args;
    args.addOption ("h",       false);
    args.addOption ("help",    false);
    args.addOption ("v",       false);
    args.addOption ("version", false);
    args.scan (argc, argv);

    if (args.getOption ("h") ||
        args.getOption ("help"))
    {
      std::cout << '\n'
                << "Usage: holidata [<options>] <phrase>\n"
                << '\n'
                << "  -h|--help       Show this usage\n"
                << "  -v|--version    Show this version\n"
                << '\n';
      return status;
    }

    else if (args.getOption ("v") ||
             args.getOption ("version"))
    {
      std::cout << "\n"
                << PACKAGE_STRING
                << " built for "
#if defined (DARWIN)
                << "Darwin"
#elif defined (SOLARIS)
                << "Solaris"
#elif defined (CYGWIN)
                << "Cygwin"
#elif defined (OPENBSD)
                << "OpenBSD"
#elif defined (FREEBSD)
                << "FreeBSD"
#elif defined (NETBSD)
                << "NetBSD"
#elif defined (LINUX)
                << "Linux"
#elif defined (KFREEBSD)
                << "GNU/kFreeBSD"
#elif defined (GNUHURD)
                << "GNU/Hurd"
#else
                << "Unknown"
#endif
                << "\n"
                << "Copyright (C) 2010 - 2016 Göteborg Bit Factory\n"
                << "\n"
                << "Holidata may be copied only under the terms of the MIT "
                   "license, which may be found in the source kit.\n"
                << "\n"
                << "Documentation for holidata can be found using 'man holidata' "
                   "or at http://tasktools.org/projects/holidata.html\n"
                << "\n";
      return status;
    }

    // Combine the positionals and parse.
    std::string phrase;
    for (auto i = 0; i < args.getPositionalCount (); i++)
    {
      if (phrase != "")
        phrase += ' ';

      phrase += args.getPositional (i);
    }

    Datetime d (phrase);
    std::cout << d.toISOLocalExtended () << '\n';
  }

  catch (std::string& error)
  {
    std::cout << error << "\n";
    return -1;
  }

  catch (...)
  {
    std::cout << "Unknown error\n";
    return -2;
  }

  return status;
}

////////////////////////////////////////////////////////////////////////////////
