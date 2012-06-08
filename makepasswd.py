#!/usr/bin/env python

import random

__all__ = [ 'makepasswd' ]

def makepasswd(length = 8, strings = None):
  """Generates a password

  The strings parameter contains a list of strings, at least one character
  of each string in the list is used
  """

  strings = strings or [
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'abcdefghijklmnopqrstuvwxyz',
    '0123456789',
    '+@*#%&/()=?![]{},;.:-_'
  ]

  stringslen = len(strings)

  # use at least one char from each char string
  lists = range(stringslen)

  for i in range(length - stringslen):
    lists.append(random.randrange(0, stringslen))

  random.shuffle(lists)

  chars = [strings[i][random.randrange(0, len(strings[i]))] for i in lists]

  return ''.join(chars)[:length]

if __name__ == '__main__':
  import sys
  import getopt

  def main(argv = sys.argv):
    opts = None
    args = None

    try:
      opts, args = getopt.getopt(argv[1:], 'l:s', ['length=', 'style='])
    except getopt.error, msg:
      usage(msg)

      return -1

    length = 8
    style  = None

    for opt, arg in opts:
      if opt in ('-l', '--length'):
        length = int(arg)
      elif opt in ('-s', '--style'):
        if arg == 'numeric':
          style = ['0123456789']
        elif arg == 'alphanumeric':
          style = [
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            'abcdefghijklmnopqrstuvwxyz',
            '0123456789',
          ]
        elif arg == 'alphabet':
          style = [
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            'abcdefghijklmnopqrstuvwxyz',
          ]
        elif arg == 'lower':
          style = [
            'abcdefghijklmnopqrstuvwxyz',
          ]
        elif arg == 'upper':
          style = [
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
          ]
        elif arg == 'lowernumeric':
          style = [
            'abcdefghijklmnopqrstuvwxyz',
            '0123456789',
          ]
        elif arg == 'uppernumeric':
          style = [
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            '0123456789',
          ]

    print makepasswd(length, style)

  def usage(msg):
    if msg: print msg

    print """Generates a password

Options:

	-l, --length: Minimum length of the password

	-s, --style: Passwordstyle, valid values are:
		numeric
		alphanumeric
		alphabet
		lower
		upper
		lowernumeric
		uppernumeric
"""

  sys.exit(main())
