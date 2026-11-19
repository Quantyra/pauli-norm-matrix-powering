"""Finite diagnostics for the AGIK boundary rewrite and weighted history forms.

Tags forget the qubit value. The modified first move preserves the neighbor's
value and creates a spectator zero. The proof handles arbitrary work superpositions.
"""

from fractions import Fraction as F
import json


def installed_rules(width, rounds, modified):
    """AGIK section 2, rules 1-6, including both open ends."""
    size = width * rounds
    edges = [(0, "A", "V"), (size - 1, "V", "A")]
    for site in range(size - 1):
        across = (site + 1) % width == 0
        if not across:
            # Gate sweep in an aligned block. S is the fresh boundary symbol.
            source = "SR" if modified and site == 0 else "GR"
            edges.append((site, source, "LG"))
        # Turning flag V, left-moving flag A, right-moving data flag F.
        if across:
            edges.extend([(site, "GU", "LV"), (site, "VR", "XG")])
        else:
            edges.extend([(site, "VR", "XF"), (site, "FU", "LV")])
        edges.extend([(site, "VU", "AU"), (site, "LA", "AR"),
                      (site, "XA", "XV"), (site, "FR", "LF")])
    return edges


def possible(state, rules, reverse=False):
    moves = []
    for site, left, right in rules:
        source, target = (right, left) if reverse else (left, right)
        if state.startswith(source, site):
            moves.append(state[:site] + target + state[site + len(source):])
    return moves


def path(width, rounds, modified):
    size = width * rounds
    steps = width * (2 * width + 3) * (rounds - 1) + width - 1
    first = "S" if modified else "G"
    states = [first + "R" * (width - 1) + "U" * (size - width)]
    rules = installed_rules(width, rounds, modified)
    for t in range(steps + 1):
        current = states[t]
        assert possible(current, rules, reverse=True) == states[max(0, t - 1):t]
        future = possible(current, rules)
        assert len(future) == (t < steps)
        if future:
            states.append(future[0])
    assert len(set(states)) == steps + 1
    assert states[-1] == "X" * (size - width) + "L" * (width - 1) + "G"
    return states


def check_rewrites():
    cases = []
    for width in (3, 4, 5, 6):
        for rounds in (2, 3, 4):
            original = path(width, rounds, False)
            marked = path(width, rounds, True)
            assert original[1:] == marked[1:]
            cycle = width * (2 * width + 3)
            gate_positions = {
                (block * cycle + offset, block * width + offset)
                for block in range(rounds)
                for offset in range(width)
            }
            gate_positions.remove((0, 0))  # The start symbol replaces the first gate marker.
            assert {(t, tags.index("G")) for t, tags in enumerate(marked) if "G" in tags} == gate_positions
            assert [i for i, tags in enumerate(marked) if tags.startswith("SR")] == [0]
            assert [i for i, tags in enumerate(marked) if tags.startswith("LG")] == [1]
            assert [i for i, tags in enumerate(marked) if tags[-1] == "G"] == [len(marked)-1]
            cases.append({"logical_width_with_spectator": width, "rounds": rounds,
                          "steps": len(marked)-1})
    return cases


def assert_positive_definite(matrix):
    work = [row[:] for row in matrix]
    for k in range(len(work)):
        pivot = work[k][k]
        assert pivot > 0
        for i in range(k + 1, len(work)):
            factor = work[i][k] / pivot
            for j in range(k + 1, len(work)):
                work[i][j] -= factor * work[k][j]


def check_forms(steps):
    size = steps + 1
    pi = [F(1, 2)] + [F(1, 2 * steps)] * steps
    delta = F(1, 6 * steps**2)
    form = [[F(0) for _ in range(size)] for _ in range(size)]
    for edge in range(steps):
        conductance = pi[edge] * pi[edge + 1] / (pi[edge] + pi[edge + 1])
        expected = F(1, 2 * (steps + 1)) if edge == 0 else F(1, 4 * steps)
        assert conductance == expected
        form[edge][edge] += conductance
        form[edge+1][edge+1] += conductance
        form[edge][edge+1] -= conductance
        form[edge+1][edge] -= conductance
    assert sum(pi) == 1 and all(sum(row) == 0 for row in form)
    # Quotient the constant functions by choosing the representative f_T = 0.
    accept = [[form[i][j] - delta * (int(i == j)*pi[i] - pi[i]*pi[j])
               for j in range(steps)] for i in range(steps)]
    reject = [row[:] for row in form]
    reject[-1][-1] += pi[-1]
    for i in range(size):
        reject[i][i] -= delta * pi[i]
    assert_positive_definite(accept)
    assert_positive_definite(reject)


def main():
    cases = check_rewrites()
    lengths = list(range(1, 13))
    for steps in lengths:
        check_forms(steps)
    yes = (F(2, 3) - F(1, 48))/2 - F(3, 512)
    no = (F(1, 3) + F(1, 48))/2 + F(1, 256) + F(3, 512)
    assert yes == F(487, 1536) and yes - F(1, 32) > F(1, 4)
    assert no == F(287, 1536) and no + F(1, 32) < F(1, 4)
    print(json.dumps({"scope": "finite rewrite graphs, rational form and margin checks",
                      "clock_cases": cases, "weighted_forms_lengths": lengths,
                      "yes_lower": str(yes), "no_upper": str(no)}, indent=2))


if __name__ == "__main__":
    main()
