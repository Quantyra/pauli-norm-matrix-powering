"""Small exact arithmetic and clock checks for the S318 return witness."""

from collections import deque
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import subprocess
import sys

from verify_chain import installed_rules, path
from estimate_pauli_power import DrawLimit
from two_step_walk import prepare, trial, two_step_row


def check_rows():
    # These small Gaussian integers and power-of-two denominators are exactly
    # representable in binary64, including every partial sum in this fixture.
    matrices = {"I": ((1, 0), (0, 1)), "X": ((0, 1), (1, 0)),
                "Y": ((0, -1j), (1j, 0)), "Z": ((1, 0), (0, -1))}
    labels = ["".join(p) for p in product("IXYZ", repeat=2)]
    real_terms = {p: F((i % 5) - 2, 32) for i, p in enumerate(labels)
                  if p.count("Y") % 2 == 0}
    complex_terms = {p: F((i % 5) - 2, 32) for i, p in enumerate(labels)}
    checked = 0
    for terms in [real_terms, complex_terms, {"XI": F(1, 2), "ZI": F(1, 2)}, {}]:
        dense = [[sum(float(a) * matrices[p[0]][x//2][y//2]
                      * matrices[p[1]][x%2][y%2] for p, a in terms.items())
                  for y in range(4)] for x in range(4)]
        for x in range(4):
            row = two_step_row(x, prepare(terms))
            for y in range(4):
                entry = sum(dense[x][z] * dense[z][y] for z in range(4))
                assert row.get(y, (0, 0)) == (F(entry.real), F(entry.imag))
                checked += 1
    return checked


def check_walk():
    # C=B^2 has rows (26,8)/64 and (8,10)/64.
    prepared = prepare({"I": F(4, 8), "X": F(1, 8), "Z": F(1, 8)})
    row0 = two_step_row(0, prepared)
    row1 = two_step_row(1, prepared)
    assert row0 == {0: (F(26, 64), 0), 1: (F(8, 64), 0)}
    assert row1 == {0: (F(8, 64), 0), 1: (F(10, 64), 0)}
    # Drive the sampler through each first and second endpoint in its own table order.
    mean = moment = F(0)
    for middle, end in product(range(2), repeat=2):
        draws, probability = [], F(1)
        for row, target in [(row0, middle), ((row0, row1)[middle], end)]:
            masses = {y: abs(pair[0]) for y, pair in row.items()}
            scale = max(w.denominator for w in masses.values())
            prefix = 0
            for y, mass in masses.items():
                if y == target:
                    break
                prefix += int(mass * scale)
            draws.append(prefix)
            probability *= masses[target] / sum(masses.values())
        words = iter(draws)
        score = trial(prepared, 0, 4, 1, randbits=lambda _: next(words))
        mean += probability * score
        moment += probability * score**2
    assert mean == F(26**2 + 8**2, 64**2)
    assert moment == F((34*26)**2 + 34*8*18*8, 64**4)
    try:
        trial(prepared, 0, 2, 1, randbits=lambda bits: 2**bits - 1)
    except DrawLimit:
        pass
    else:
        raise AssertionError("expected bounded rejection")
    data = {"basis":"0", "power_unary":"11",
            "terms":[["I","0.1"],["X","0.001"],["Z","0.001"]]}
    cli = subprocess.run([sys.executable, "-B", str(Path(__file__).with_name("two_step_walk.py"))],
                         input=json.dumps(data), text=True, capture_output=True, check=True)
    assert json.loads(cli.stdout) == {"0":["13/32","0"], "1":["1/8","0"]}
    return str(mean), str(moment)


def check_window():
    ell = 162
    shapes = path(3, 18, True)
    swaps = set()
    branching = set()
    for t in range(ell + 1):
        a, i = divmod(t, 27)
        if i == 1 and a:
            assert shapes[t][3*a+1:3*a+3] == "GR"
            assert shapes[t+1][3*a+1:3*a+3] == "LG"
            (branching if a % 2 else swaps).add(t)
    assert sorted(branching) == [28, 82, 136]
    graph = {}
    for t in range(ell + 1):
        for b in (0, 1):
            targets = (0, 1) if t in branching else (b ^ (t in swaps),)
            for dest in targets:
                left, right = (t,b), (t+1,dest)
                graph.setdefault(left, []).append(right)
                graph.setdefault(right, []).append(left)
    dist = {(0,0): 0}
    queue = deque(dist)
    while queue:
        point = queue.popleft()
        for near in graph[point]:
            if near not in dist:
                dist[near] = dist[point] + 1
                queue.append(near)
    longest = max(dist[t,b] for t in range(2, ell+2) for b in (0, 1))
    assert longest <= 400
    for u in (1, 2, 4, 16):
        r = 16*u+2
        T = 27*(r-1)+2
        count = len(installed_rules(3,r,True)) + 1
        K = 1 << (256*count-1).bit_length()
        s = F(1,4*K)
        m = 144*K*T*T
        tau = F(1,1 << (256*m-1).bit_length())
        gamma0 = F(1,5*ell)  # strictly below the analytic surplus, since sqrt(2)>7/5
        assert m*s == 36*T*T and m % 4 == 0
        assert 2*gamma0*s - 2*(1+gamma0)*s*s - 6*ell*tau >= gamma0*s
        assert 3*tau <= s/(8*T) and m//2 > 800
    return sorted(branching), longest


if __name__ == "__main__":
    entries = check_rows()
    mean, moment = check_walk()
    hadamards, radius = check_window()
    print(json.dumps(dict(dense_entries=entries, walk_mean=mean, walk_second_moment=moment,
                          branching_times=hadamards, reachable_window_states=324,
                          maximal_connector=radius, rounding_cases=4, cli_and_retry=True), indent=2))
