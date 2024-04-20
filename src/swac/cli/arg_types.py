import typed_argparse as tap


class InitArgs(tap.TypedArgs):
    pass

class CheckArgs(tap.TypedArgs):
    pass

class BuildArgs(tap.TypedArgs):
    pass

class ServeArgs(tap.TypedArgs):
    host: str = tap.arg(help="The server host.", default="127.0.0.1",)
    port: int = tap.arg(help="The server port.", default=25000, )