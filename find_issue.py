from multiprocessing import get_context

import sys
import subprocess as sp
import pathlib
import textwrap
import argparse
import shutil
import re
import os
import random

curdir=pathlib.Path(__file__).parent
extra_path=[str(curdir/"pysource-codegen"),str(curdir/"pysource-minimize/src")]

sys.path+=extra_path


os.environ["PYTHONPATH"]=os.environ.get("PYTHONPATH","")+ os.pathsep+os.pathsep.join(extra_path)

from pysource_minimize import minimize

def main():

    parser = argparse.ArgumentParser(description="Description of your script")

# Add command-line arguments similar to Click options
    parser.add_argument("--num", type=int, default=100, help="Number of seeds to process")
    parser.add_argument("--failed", action="store_true", help="Run only failed examples")
    parser.add_argument("-r", "--regenerate", action="store_true", help="Run pysource-codegen again")
    parser.add_argument("--fail-fast", action="store_true", help="Fail after the first error")
    parser.add_argument("--sequential", action="store_true", help="Test seeds single threaded")
    parser.add_argument("seeds", nargs='*', type=int, help="Specific seeds to test")

    args = parser.parse_args()

    num = args.num
    seeds = args.seeds
    failed = args.failed
    sequential = args.sequential
    regenerate = args.regenerate
    fail_fast = args.fail_fast


    if not seeds:
        seeds = [random.randint(0,1_000_000_000_000) for _ in range(num)]

    work_dir = pathlib.Path("work")
    work_dir.mkdir(exist_ok=True)

    if failed:
        seeds = [int(f.stem.split("_")[-1]) for f in work_dir.glob("seed_*")]

    if sequential:
        for seed in seeds:
            test_seed((seed,regenerate))
    else:

        with get_context("spawn").Pool(maxtasksperchild=100) as p:
            for r in p.imap_unordered(test_seed, [(seed,regenerate) for seed in seeds]):
                if r and fail_fast:
                    break
            p.terminate()


def test_seed(args):
    (seed,regenerate)=args
    work_dir = pathlib.Path("work")
    work_dir.mkdir(exist_ok=True)

    seed_dir = work_dir / f"seed_{seed}"
    seed_dir.mkdir(exist_ok=True)

    source_file = seed_dir / "generated.py"
    print("test seed:", seed)

    exists_before = source_file.exists()

    if not exists_before or regenerate:

        result = sp.run(
            [
                sys.executable,
                "-W",
                "ignore",
                "generate_code.py",
                str(seed),
                str(source_file),
            ],
            capture_output=True,
        )

        (seed_dir / "generated_code.out").write_bytes(result.stdout + result.stderr)

        if result.returncode != 0:
            print("error during code generation message:")
            print(result.stdout.decode())
            print(result.stderr.decode())
            return

    result = sp.run(
        [sys.executable, "-W", "ignore", "test_code.py", str(source_file)],
        capture_output=True,
    )

    source = (source_file).read_text()

    if result.returncode != 0:
        print("error message:")
        print(result.stdout.decode())
        print(result.stderr.decode())

        def system_error(result):
            return "SystemError:" in result.stderr.decode()
        
        if not system_error(result):
            print(f"unknown error for seed {seed}")
            return

        print(f"found issue (seed = {seed}) -> minimize code")

        def checker(source):
            file = seed_dir / "check_minimize.py"
            file.write_text(source)
            result = sp.run(
                [sys.executable, "-W", "ignore", "test_code.py", str(file)],
                capture_output=True,
            )

            bug_exists = (
                result.returncode != 0
                and system_error(result)
            )

            if bug_exists:
                print(f"minimized to {len(source)} bytes")
                (seed_dir / "broken_code.py").write_text(source)

            return bug_exists

        newsource = minimize(source, checker,compilable=False,retries=2)

        result_file = seed_dir / f"bug.py"
        result_file.write_text(newsource)

        result = sp.run(
            [sys.executable, "test_code.py", str(result_file)], capture_output=True
        )
        output = (result.stdout + result.stderr).decode("utf-8")

        result_file.write_text(
            newsource + "\n\n# output:\n" + textwrap.indent(output, "# ")
        )

        print(f"minimized code ({result_file})")
        print(result_file.read_text())

        sample_file = seed_dir / "sample.py"

        def checker(sample_code):
            sample_code = re.sub(
                "source *=.*", f"source='''\n{newsource}\n'''", sample_code
            )
            sample_file.write_text(sample_code)
            result = sp.run(
                [sys.executable, "-W", "ignore", str(sample_file)], capture_output=True
            )

            bug_exists = (
                result.returncode != 0
                and system_error(result)
            )

            if bug_exists:
                print(f"minimized to {len(source)} bytes")
                (seed_dir / "broken_code.py").write_text(source)

            return bug_exists

        sample_code = pathlib.Path("./test_code.py").read_text()
        sample_code = minimize(sample_code, checker)
        sample_code = re.sub(
            "source *=.*", f"source='''\n{newsource}\n'''", sample_code
        )

        sample_file.write_text(sample_code)

        return True

    if exists_before:
        print(f"bug is solved ... delete {seed_dir}")
    shutil.rmtree(seed_dir)


if __name__ == "__main__":
    main()
