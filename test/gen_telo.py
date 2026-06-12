#!/usr/bin/env python3
"""Generate synthetic sequences with known telomere arrays to exercise `seqtk telo -i`.
Model matches seqtk's: 5' telomere = CCCTAA array (+ strand), 3' = TTAGGG array (- strand)."""
import random

random.seed(7)
FWD = "CCCTAA"          # + strand motif (seqtk default)
REV = "TTAGGG"          # reverse complement of FWD (- strand)

def rnd(n):
    return "".join(random.choice("ACGT") for _ in range(n))

def fa(name, seq):
    return ">%s\n%s\n" % (name, seq)

# Record names carry the fixture type but are prefixed with "test_" so the seqtk
# output's name column clearly reads as a record name, not a tool-emitted type.
records = []

# test_clean: clean chromosome end layout -- + array at 5', - array at 3'
records.append(fa("test_clean",
    FWD*70 + rnd(2000) + REV*70))

# test_interstitial: interstitial + array in the middle, no terminal telomeres
records.append(fa("test_interstitial",
    rnd(1000) + FWD*80 + rnd(1000)))

# test_misjoin: annealed misjoin -- terminal +, internal [- , Ns, +] pair, terminal -
records.append(fa("test_misjoin",
    FWD*70 + rnd(1500) + REV*70 + "N"*100 + FWD*70 + rnd(1500) + REV*70))

# test_none: no telomere repeats at all
records.append(fa("test_none", rnd(2000)))

with open("test.fa", "w") as f:
    f.write("".join(records))

# Print expected array coordinates (approx, motif-level) for cross-checking
print("# expected arrays (0-based approx, before len-1 trim):")
def report(name, parts):
    pos = 0
    for kind, length in parts:
        if kind in ("+", "-"):
            print("#  %-18s %-2s %d..%d" % (name, kind, pos, pos+length))
        pos += length
report("test_clean", [("+",70*6),("r",2000),("-",70*6)])
report("test_interstitial", [("r",1000),("+",80*6),("r",1000)])
report("test_misjoin", [("+",70*6),("r",1500),("-",70*6),("N",100),("+",70*6),("r",1500),("-",70*6)])
