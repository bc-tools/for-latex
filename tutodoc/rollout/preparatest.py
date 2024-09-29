# Source: https://stackoverflow.com/a/25120960/4589608

from pathlib import Path
from random  import shuffle

THIS_DIR = Path(__file__).parent

TESTS_DIR = THIS_DIR / "tests"

testfiles = [
    p.stem
    for p in TESTS_DIR.glob("*.lvt")
]

shuffle(testfiles)

import multiprocessing
import subprocess
import shlex

from multiprocessing.pool import ThreadPool


def call_proc(cmd):
    """ This runs in a separate thread. """
    #subprocess.call(shlex.split(cmd))  # This will block until cmd finishes
    print(cmd)

    p = subprocess.Popen(
        shlex.split(cmd),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    out, err = p.communicate()

    return (out, err)


pool = ThreadPool(multiprocessing.cpu_count())

results = []

for tname in testfiles:
    results.append(
        pool.apply_async(
            call_proc,
            (f"l3build check {tname}",)
        )
    )

# Close the pool and wait for each running task to complete
pool.close()
pool.join()

for result in results:
    out, err = result.get()

    if err:
        print("out: {} err: {}".format(out, err))
