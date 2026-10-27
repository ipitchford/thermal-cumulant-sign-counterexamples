# SPDX-License-Identifier: MIT
"""Semantic negative controls for the exact verifiers.

Each control copies the package to a temporary directory, corrupts one claim or
one input in a verifier, and requires that verifier to FAIL. The unmodified
verifiers are run first and must PASS. Assertions are the checking mechanism,
so this script refuses to run under python -O.

Run from the package root:  uv run python3 -B -I code/negative_controls.py
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

if not __debug__:
    sys.exit('negative_controls.py must not run under -O: the verifiers rely on assert')

ROOT = Path(__file__).resolve().parent.parent
PY = [sys.executable, '-B', '-I']
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')

# (verifier, exact original text, corrupted text, meaning)
CONTROLS = [
    ('verify_determinant.py', "edge(ch,'cold',0,1,F(1,2),8)", "edge(ch,'cold',0,1,F(1,2),9)",
     'break cold-bath local detailed balance on edge 0-1'),
    ('verify_determinant.py', "E=[0,2,1]; pi=[F(40,63),F(5,63),F(18,63)]", "E=[0,2,1]; pi=[F(41,63),F(4,63),F(18,63)]",
     'wrong stationary law'),
    ('verify_determinant.py', "assert leads[2]/leads[0]==-F(16,21609)", "assert leads[2]/leads[0]==-F(17,21609)",
     'wrong leading coefficient of S'),
    ('verify_determinant.py', "y[1]=beta*j/R", "y[1]=-beta*j/R",
     'reversed current orientation in the limiting quadratic'),
    ('verify_poisson.py', "assert pi == [F(40,63),F(5,63),F(18,63)]", "assert pi == [F(40,63),F(18,63),F(5,63)]",
     'permuted stationary law'),
    ('verify_scaling.py', "assert cn[3]/cn[1] == F(-16,64827)", "assert cn[3]/cn[1] == F(16,64827)",
     'positive leading coefficient of K'),
    ('verify_scaling.py', "assert not (Nl-F(1,32)).d", "assert not (Nl-F(1,16)).d",
     'wrong two-state endpoint value'),
    ('verify_scaling.py', "bern = (1-tt)**4+F(1,2)*tt*(1-tt)**3+F(5,8)*tt**3*(1-tt)+F(1,8)*tt**4",
     "bern = (1-tt)**4+F(1,2)*tt*(1-tt)**3+F(5,8)*tt**3*(1-tt)+F(1,7)*tt**4",
     'wrong positive decomposition of H'),
    ('verify_extension.py', "sp.Interval(0, sp.oo)) == R(-15, 4)", "sp.Interval(0, sp.oo)) == R(-4, 1)",
     'wrong minimum of the normalised kurtosis limit'),
    ('verify_extension.py', "assert sp.simplify(ns - R(3, 2) * (1 - r)) == 0", "assert sp.simplify(ns - R(3, 2) * (1 + r)) == 0",
     'wrong normalised skewness limit'),
    ('verify_extension.py', "assert nsf == R(-9, 4) and nkf == R(-3, 4)", "assert nsf == R(-9, 4) and nkf == R(3, 4)",
     'wrong sign of the full-family normalised kurtosis'),
]

NEEDS_UV = {'verify_extension.py'}


def run(pkg, script):
    argv = PY + [f'code/{script}']
    if script in NEEDS_UV:
        uv = shutil.which('uv')
        if uv is None:
            sys.exit('uv not found; verify_extension.py needs numpy and sympy from uv.lock')
        argv = [uv, 'run', '--frozen', 'python3', '-B', '-I', f'code/{script}']
    return subprocess.run(argv, cwd=pkg, capture_output=True, text=True, env=ENV, timeout=1800).returncode


def main():
    failures = []
    with tempfile.TemporaryDirectory(prefix='thermal-nc-') as td:
        base = Path(td) / 'pkg'
        shutil.copytree(ROOT, base, ignore=shutil.ignore_patterns('.git', '__pycache__', '.venv'))
        for script in sorted({c[0] for c in CONTROLS}):
            if run(base, script) != 0:
                sys.exit(f'FAIL baseline {script} did not pass; controls are meaningless')
        print(f'baselines pass: {len({c[0] for c in CONTROLS})} verifiers')
        for i, (script, old, new, meaning) in enumerate(CONTROLS, 1):
            pkg = Path(td) / f'nc{i}'
            shutil.copytree(base, pkg)
            p = pkg / 'code' / script
            text = p.read_text()
            if text.count(old) != 1:
                sys.exit(f'FAIL control {i}: anchor not found exactly once in {script}')
            p.write_text(text.replace(old, new))
            rc = run(pkg, script)
            ok = rc != 0
            print(f'control {i:2d} {"rejected" if ok else "ACCEPTED"}: {meaning}')
            if not ok:
                failures.append(meaning)
            shutil.rmtree(pkg)
    if failures:
        sys.exit(f'FAIL {len(failures)} corruptions were accepted: {failures}')
    print(f'PASS all {len(CONTROLS)} semantic negative controls rejected')


if __name__ == '__main__':
    main()
