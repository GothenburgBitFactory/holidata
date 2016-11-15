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
#include <iostream>
#include <unistd.h>
#include <sys/types.h>
#include <pwd.h>

////////////////////////////////////////////////////////////////////////////////
int main (int argc, char** argv)
{
  int status = 0;

  try
  {
    // Locate $HOME.
    struct passwd* pw = getpwuid (getuid ());
    if (!pw)
      throw std::string ("Could not determine the home directory.");

    std::string rcFile = pw->pw_dir;
    rcFile += "/.holidatarc";

    // Process arguments.
    for (int i = 1; i < argc; ++i)
    {
      if (! strcmp (argv[i], "-h") ||
          ! strcmp (argv[i], "--help"))
      {
        std::cout << '\n'
                  << "Usage: holidata [<options>]\n"
                  << '\n'
                  << "  -h|--help       Show this usage\n"
                  << "  -v|--version    Show this version\n"
                  << "  -f|--file       Override default ~/.holidatarc\n"
                  << '\n';
        return status;
      }

      else if (! strcmp (argv[i], "-v") ||
               ! strcmp (argv[i], "--version"))
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
                  << "Clog may be copied only under the terms of the MIT "
                     "license, which may be found in the source kit.\n"
                  << "\n"
                  << "Documentation for clog can be found using 'man clog' "
                     "or at http://tasktools.org/projects/clog.html\n"
                  << "\n";
        return status;
      }

      else if (argc > i + 1 &&
               (! strcmp (argv[i], "-f") ||
                ! strcmp (argv[i], "--file")))
      {
        rcFile = argv[++i];
      }

      else
      {
        // TODO Positionals.
      }
    }
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
