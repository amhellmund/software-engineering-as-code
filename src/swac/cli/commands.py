from .arg_types import InitArgs, CheckArgs, BuildArgs, ServeArgs

def run_init(args: InitArgs) -> None:
    print("init")


def run_check(args: CheckArgs) -> None:
    print("check")


def run_build(args: BuildArgs) -> None:
    print("build")


def run_serve(args: ServeArgs) -> None:
    print("serve")