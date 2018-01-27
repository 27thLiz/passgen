passgen
==============================================================================

Generates easy to remember passwords, inspired by [xkcd #936](https://xkcd.com/936/)

Installation
------------

```
$ pip install -r requirements.txt

$ python setup.py install
```

Usage
-----

```
usage: passgen [-h] [--debug] [--quiet] [-c] [-f FROM] [-t TO] [-w WORDS]
               [-l--wordlist FILENAME] [-s SEPERATOR]
               {default} ...

Generates easy to remember passwords.

optional arguments:
  -h, --help            show this help message and exit
  --debug               toggle debug output
  --quiet               suppress all output
  -c, --copy            Copy password to the clipboard. Clears after 45
                        seconds.
  -f FROM, --from FROM  Set the minimum character count for words.
  -t TO, --to TO        Set the maximum character count for words.
  -w WORDS, --words WORDS
                        Set the number of words.
  -l--wordlist FILENAME
                        Set the word list file. Defaults to
                        /usr/share/dict/words
  -s SEPERATOR, --seperator SEPERATOR
                        Sets the character(s) used to seperate words.
```
