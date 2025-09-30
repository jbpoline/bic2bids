Sample invocation on oberon (using `uvx`)

    TMPDIR=/export01/heudiconv/tmp uvx heudiconv --dbg --bids -f code/reproin-map-heuristic.py \
        -o heudiconv-try4 \
        --files ~/proj/bic-bids/773559_MPN0000072_MPN1Scan1_*.tar.gz \
        --minmeta -c none -s 1 -l ''

- `-s 1` -- we need to provide subject id instead of potentially sensitivie one
  - TODO: just try and use the anonymization script?

- `-l ''` -- study description is there but not well harmonized
  - TODO: provide mapping to studies (I think heuristic can do that too)

- `-c none` -- just to test without conversion
  - TODO: test with conversion (dcm2niix)

