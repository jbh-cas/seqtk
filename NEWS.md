Fork addition (jbh-cas)
-----------------------

 * New feature: added option `-i` to the `telo` command for genome-wide
   internal telomere detection. Reports all telomere runs (terminal AND
   internal) on both strands with a strand-tagged class column. A
   telomere-Ns-telomere junction (the scaffold "annealed" pattern)
   is reported as one row `internalX annealedY`. A terminal
   telomere that absorbed such a junction across an N-gap is tagged
   `5p annealed+` or `3p annealed-`. The motif is auto-canonicalized to the
   lex-lower strand under `-i` so `+` is stable regardless of which strand of
   `-m` is supplied. Default `telo` behavior (no `-i`) is byte-for-byte
   identical to upstream r133.

 * New feature: added option `-v` (effective with `-i`) to append each
   array's score as a 6th column.

 * Identical results with `telo -i` to original seqtk for non-internal telomeres, except for 5p or 3p annotation:
   
   `seqtk telo -i F | grep -v internal | cut -f1-4` == `seqtk telo F`.


Release 1.5-r133 (1 June 2025)
------------------------------

Notable changes:

 * Improvement: support chromosomes longer than 2Gb (#192), provided @c-zhou

 * New feature: added option `-R` to the seq command to output sequences on
   both strands.

 * New feature: added option `-P` to telo to output scores

(1.5: 1 June 2025, r133)



Release 1.4-r122 (19 May 2023)
------------------------------

Notable changes:

 * Improvement: faster FASTX parsing (#123)

 * New feature: added the `telo` command to output telomere regions.

 * New feature: added the `size` command to count the number of sequences and
   the number of bases. Lighter and thus faster than `comp`.

 * New feature: added the `hpc` command to compress homopolymers in input
   sequences.

 * New feature: added the `split` command to split a large input file into
   multiple smaller files.

 * New feature: added the `gap` command to output non-ACGT regions in the input
   file.

 * New feature: added option `-s` to command `subseq` to support the strand
   field in BED. For the moment, this option does not work with other subseq
   options.

(1.4: 19 May 2023, r122)
