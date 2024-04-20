import typed_argparse as tap

from .arg_types import InitArgs, CheckArgs, BuildArgs, ServeArgs
from .commands import run_init, run_check, run_build, run_serve

def main () -> None:
    tap.Parser(
        tap.SubParserGroup(
            tap.SubParser("init", InitArgs),
            tap.SubParser("check", CheckArgs),
            tap.SubParser("build", BuildArgs),
            tap.SubParser("serve", ServeArgs),
        )
    ).bind(
        tap.Binding(InitArgs, run_init),
        tap.Binding(CheckArgs, run_check),
        tap.Binding(BuildArgs, run_build),
        tap.Binding(ServeArgs, run_serve),
    ).run()