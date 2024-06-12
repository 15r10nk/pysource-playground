

from pysource_minimize import minimize

import sys
import subprocess as sp
import pathlib
import textwrap
import click
import shutil



@click.command()
@click.option("--seed-start",type=int,default=0)
@click.option("--num",type=int,default=100)
@click.option("--failed",is_flag=True,help="run only failed examples")
@click.argument("seeds",nargs=-1,type=int)
def main(seed_start,num,seeds,failed):

    work_dir=pathlib.Path("work")
    work_dir.mkdir(exist_ok=True)

    if not seeds:
        seeds=range(seed_start,seed_start+num)

    if failed:
        seeds=[int(f.stem.split("_")[-1]) for f in work_dir.glob("seed_*")]


    for seed in seeds:

        seed_dir=work_dir/f"seed_{seed}"
        seed_dir.mkdir(exist_ok=True)

        source_file=(seed_dir/"generated.py")
        print("test seed:",seed)
        if not source_file.exists():

            result=sp.run([sys.executable,"-W", "ignore" , "generate_code.py",str(seed),str(source_file)],capture_output=True)

            (seed_dir/"generated_code.out").write_bytes(result.stdout+result.stderr)

            if result.returncode !=0:
                print("error during code generation message:")
                print(result.stdout.decode())
                print(result.stderr.decode())
                continue

        result=sp.run([sys.executable,"-W", "ignore","test_code.py",str(source_file)],capture_output=True)

        source=(source_file).read_text()

        if result.returncode !=0:
            print("error message:")
            print(result.stdout.decode())
            print(result.stderr.decode())
            original_error=result.stderr.decode().splitlines()[-1]

            print(f"found issue (seed = {seed}) -> minimize code")


            def checker(source):
                file=(seed_dir/"check_minimize.py")
                file.write_text(source)
                result=sp.run([sys.executable,"-W", "ignore","test_code.py",str(file)],capture_output=True)

                bug_exists = result.returncode!=0 and result.stderr.decode().splitlines()[-1]==original_error

                if bug_exists:
                    print(f"minimized to {len(source)} bytes")
                    (seed_dir/"broken_code.py").write_text(source)

                return bug_exists
                

            newsource=minimize(source,checker)


            result_file=seed_dir/f"bug.py"
            result_file.write_text(newsource)

            result=sp.run([sys.executable,"test_code.py",str(result_file)],capture_output=True)
            output=(result.stdout+result.stderr).decode("utf-8")

            result_file.write_text(newsource+"\n\n# output:\n"+textwrap.indent(output,"# "))


            print(f"minimized code ({result_file})")
            print(result_file.read_text())
            continue


        print(f"bug is solved ... delete {seed_dir}")
        shutil.rmtree(seed_dir)
            


if __name__ == "__main__":
    main()

    

