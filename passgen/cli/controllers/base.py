"""passgen base controller."""

from cement.ext.ext_argparse import ArgparseController, expose
from passgen.core.generator import generator


class BaseController(ArgparseController):
    class Meta:
        label = 'base'
        description = 'Generates easy to remember passwords.'
        arguments = [
            (['-c', '--copy'],
             dict(help='Copy password to the clipboard. Clears after 45 seconds.', dest='copy', action='store_true',)),
            (['-f', '--from'],
             dict(help='Set the minimum character count for words.', dest='from', action='store',)),
            (['-t', '--to'],
             dict(help='Set the maximum character count for words.', dest='to', action='store',)),
            (['-w', '--words'],
             dict(help='Set the number of words.', dest='words', action='store',)),
            (['-l' '--wordlist'],
             dict(help='Set the word list file. Defaults to /usr/share/dict/words', dest='filename', action='store',)),
            (['-s', '--seperator'],
             dict(help='Sets the character(s) used to seperate words.', dest='seperator', action='store',)),
        ]

    @expose(hide=True)
    def default(self):
        gen = generator()
        min_count = int(self.app.config.get("passgen", "from")) + 1
        max_count = int(self.app.config.get("passgen", "to")) + 1
        word_count = int(self.app.config.get("passgen", "words"))
        seperator = self.app.config.get("passgen", "seperator")
        filename = self.app.config.get("passgen", "filename")
        if min_count > max_count:
            # TODO log warning
            max_count = min_count
        copy = self.app.pargs.copy

        password = gen.generate_password(
            filename, min_count, max_count, word_count, seperator)
        
        if (copy):
            pass
        else:
            print(password)
