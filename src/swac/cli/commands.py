import uvicorn

from .arg_types import InitArgs, CheckArgs, BuildArgs, ServeArgs

from swac.backend.server import create_server

def run_init(args: InitArgs) -> None:
    print("init")


def run_check(args: CheckArgs) -> None:
    print("check")


def run_build(args: BuildArgs) -> None:
    print("build")


def run_serve(args: ServeArgs) -> None:
    uvicorn.run(
        app=create_server(),
        host=args.host,
        port=args.port,
    )