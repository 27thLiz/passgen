"""CLI tests for passgen."""

from passgen.utils import test

class CliTestCase(test.TestCase):
    def test_passgen_cli(self):
        argv = ['--foo=bar']
        with self.make_app(argv=argv) as app:
            app.run()
            self.eq(app.pargs.foo, 'bar')
