#!/usr/bin/env python3
"""Verify the hard invariant the user requires:
    seqtk telo -i FILE | grep -v internal | cut -f1-4   ==   seqtk telo FILE
across adversarial fixtures (leading/trailing junk, N-interrupted telomeres,
whole-contig telomere, marginal scores, inverted terminal, interstitial-only)."""
import random, subprocess, sys

random.seed(11)
SEQTK = "../seqtk"
FWD, REV = "CCCTAA", "TTAGGG"
def rnd(n): return "".join(random.choice("ACGT") for _ in range(n))

cases = {
    "clean_both":   FWD*70 + rnd(2000) + REV*70,
    "lead_junk5p":  rnd(13) + FWD*70 + rnd(2000) + REV*70,
    "ns_in_5ptelo": FWD*45 + "N"*40 + FWD*45 + rnd(2000) + REV*70,
    "trail_junk3p": FWD*70 + rnd(2000) + REV*70 + rnd(17),
    "all_telo":     FWD*120,
    "marginal5p":   FWD*52 + rnd(2000),
    "inverted5p":   REV*70 + rnd(2000),
    "interstitial": rnd(1000) + FWD*80 + rnd(1000),
    "double_misjoin": FWD*70 + rnd(1500) + REV*70 + "N"*100 + FWD*70 + rnd(1500) + REV*70,
    "none":         rnd(2000),
}
open("adversarial.fa", "w").write("".join(">%s\n%s\n" % kv for kv in cases.items()))

def run(args):
    return subprocess.run([SEQTK, "telo"] + args + ["adversarial.fa"],
                          capture_output=True, text=True).stdout

default = run([])
i_full  = run(["-i"])
# apply: grep -v internal | cut -f1-4
filtered = "\n".join("\t".join(ln.split("\t")[:4])
                     for ln in i_full.splitlines() if "internal" not in ln)
filtered = (filtered + "\n") if filtered else ""

ok = (filtered == default)
print("INVARIANT  seqtk telo -i | grep -v internal | cut -f1-4  ==  seqtk telo :",
      "PASS" if ok else "FAIL")
if not ok:
    print("\n--- default ---\n" + default + "\n--- filtered -i ---\n" + filtered)

print("\nFull -i output:")
for ln in i_full.splitlines():
    print("  " + ln)
sys.exit(0 if ok else 1)
