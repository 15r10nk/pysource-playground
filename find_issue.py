

from pysource_minimize import minimize

import sys
import subprocess as sp
import pathlib
import textwrap
import click



@click.command()
@click.option("--seed-start",type=int,default=0)
@click.option("--num",type=int,default=100)
@click.option("--failed",is_flag=True,help="run only failed examples")
@click.argument("seeds",nargs=-1,type=int)
def main(seed_start,num,seeds,failed):

    workdir=pathlib.Path("work")
    workdir.mkdir(exist_ok=True)

    if not seeds:
        seeds=range(seed_start,seed_start+num)

    if failed:
        seeds=[int(f.stem.split("_")[-1]) for f in workdir.glob("bug_*.py")]


    for seed in seeds:
        print("test seed:",seed)
        result=sp.run([sys.executable,"-W", "ignore" ,"generate_code.py",str(seed)],capture_output=True)


        source=(workdir/"generated_code.py").read_text()

        (workdir/"generated_code.out").write_bytes(result.stdout+result.stderr)



        if result.returncode !=0:
            print(result.stdout.decode())
            print(result.stderr.decode())
            original_error=result.stderr.decode().splitlines()[-1]

            print("found issue -> minimize code")


            def checker(source):
                file=(workdir/"check_minimize.py")
                file.write_text(source)
                result=sp.run([sys.executable,"-W", "ignore","test_code.py",str(file)],capture_output=True)

                bug_exists = result.returncode!=0 and result.stderr.decode().splitlines()[-1]==original_error

                if bug_exists:
                    print(f"minimized to {len(source)} bytes")
                    (workdir/"broken_code.py").write_text(source)

                return bug_exists
                

            newsource=minimize(source,checker)


            result_file=workdir/f"bug_{seed}.py"
            result_file.write_text(newsource)

            result=sp.run([sys.executable,"test_code.py",str(result_file)],capture_output=True)
            output=(result.stdout+result.stderr).decode("utf-8")

            result_file.write_text(newsource+"\n\n# output:\n"+textwrap.indent(output,"# "))


            print(f"minimized code ({result_file})")
            print(result_file.read_text())
        else:
            for f in workdir.glob(f"bug_{seed}.*"):
                print(f"bug is solved ... delete {f}")
                f.unlink()
            
            #return 


if __name__ == "__main__":
    main()

    

