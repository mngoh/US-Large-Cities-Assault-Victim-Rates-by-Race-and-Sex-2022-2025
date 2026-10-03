"""Flatten each state-year zip to one row per victim per offense, for that state's cities only.

Runs the kit's `nibrs.py flatten` on data/raw/<ST>-<year>.zip with the ORIs of the state's cities whose window covers
that year (tier 2 cities start in 2024), writing data/interim/flat/<ST>-<year>.csv and a log in out/logs/. At most three
run at once (the machine has 16 GB and the big states load large tables), largest and smallest files interleaved.
Existing outputs are skipped.

  python scripts/flatten_states.py            # every state-year
  python scripts/flatten_states.py CA NY      # some states
"""
import concurrent.futures as cf
import os
import pathlib
import subprocess
import sys

from cities import CITIES, STATES

ROOT = pathlib.Path(__file__).resolve().parent.parent
KIT = pathlib.Path(os.path.expanduser(os.environ.get("DISPARITY_KIT", "~/.claude/disparity-kit/kit")))
PY = sys.executable
FLAT = ROOT / "data/interim/flat"
YEARS = [2022, 2023, 2024, 2025]


def jobs(states):
    out = []
    for st in states:
        for y in YEARS:
            oris = [c["ori"] for c in CITIES if c["state"] == st and int(c["start"][:4]) <= y]
            z = ROOT / f"data/raw/{st}-{y}.zip"
            if oris and not (FLAT / f"{st}-{y}.csv").exists():
                out.append((st, y, oris, z))
    big = sorted(out, key=lambda j: -j[3].stat().st_size)
    order = []
    while big:  # largest, smallest, next largest, ...
        order.append(big.pop(0))
        if big:
            order.append(big.pop())
    return order


def run(job):
    st, y, oris, z = job
    dest = FLAT / f"{st}-{y}.csv"
    tmp = FLAT / f"{st}-{y}.part.csv"
    cmd = [PY, KIT / "nibrs.py", "flatten", z, "--out", tmp] + [a for o in oris for a in ("--ori", o)]
    with open(ROOT / f"out/logs/flatten_{st}-{y}.log", "w") as log:
        r = subprocess.run([str(a) for a in cmd], cwd=ROOT, stdout=log, stderr=subprocess.STDOUT)
    if r.returncode:
        return f"{st}-{y}: FAILED (exit {r.returncode}), see out/logs/flatten_{st}-{y}.log"
    tmp.rename(dest)
    return f"{st}-{y}: " + (ROOT / f"out/logs/flatten_{st}-{y}.log").read_text().strip().splitlines()[-1].rsplit(" (", 1)[-1].rstrip(")")


def main():
    states = sys.argv[1:] or STATES
    FLAT.mkdir(parents=True, exist_ok=True)
    (ROOT / "out/logs").mkdir(parents=True, exist_ok=True)
    todo = jobs(states)
    print(f"{len(todo)} state-years to flatten", flush=True)
    with cf.ThreadPoolExecutor(max_workers=3) as ex:
        for fut in cf.as_completed([ex.submit(run, j) for j in todo]):
            print(fut.result(), flush=True)


if __name__ == "__main__":
    main()
