#!/usr/bin/env bash
# Runs every script and checks the key structural results. Needs Python 3.10+ and numpy.
# Outputs go to ./output/ ; compare with ./expected_output/ (random samples can differ between
# Python versions, so the checks below look at structural statements, not at every number).
set -u
cd "$(dirname "$0")"; mkdir -p output; fail=0
run() { dir=$1; s=$2; ( cd "$dir" && ENGINE_DIR=/nonexistent python3 "$s" ) > "output/${s%.py}.txt" 2>"output/${s%.py}.err" || { echo "FAIL (exit) $s"; fail=1; }; }
for s in exact_invariance_groups counterexamples random_cochain_check alt_product_check dim32_check general_n_check corr_check transcribe_check \
         uniformity_proof_check pairs_check pairs_classes sym_probe uniformity_probe_dep uniformity_probe; do run scripts $s.py; done
run sedenion paren_verify.py
need() { grep -q -- "$2" "output/$1.txt" && echo "ok    $1: $3" || { echo "FAIL  $1: $3"; fail=1; }; }
need exact_invariance_groups "left only  (L)   universal invariance group order  2" "L only: guaranteed symmetry group has order 2"
need exact_invariance_groups "right only (R)   universal invariance group order  2" "R only: guaranteed symmetry group has order 2"
need exact_invariance_groups "left and right   universal invariance group order 24" "L and R: order 24"
[ "$(grep -c "uniform: False" output/counterexamples.txt)" = 2 ] \
  && echo "ok    counterexamples: both one-condition cochains are non-uniform" || { echo "FAIL  counterexamples"; fail=1; }
need uniformity_proof_check "equal: True" "group <s1,s2,t3> equals S (order 24)"
need uniformity_proof_check "mismatches over 120 perms x 300 random quadruples x 5 edges: 0" "equivariance X_i(phi psi)=X_pi(i)(phi), 0 mismatches"
need transcribe_check "'(3) a(x,y,z)=a(x+y,y,y+z)': True" "three substitution identities hold"
need transcribe_check "\[5, 9, 10, 13, 11\] expected" "q_i = 5,9,10,13,11 for a,b,c,d = bits 1,2,4,8"
need dim32_check "{0: \[166576\], 2: \[48720\], 4: \[78960\]}" "n=5 census"
need dim32_check "n= 5 left alt: True right alt: True" "left/right alternativity n=5"
need alt_product_check "{0: \[15136\], 2: \[2688\], 4: \[4704\]}" "sedenion census"
need alt_product_check "{0: \[26656\], 2: \[3456\], 4: \[864\]}" "alternate product census"
need uniformity_probe_dep "nonuniform samples: 0 of 60" "60 random alternative cochains uniform"
need paren_verify "mismatches = 0" "triple formula vs brute force"
need corr_check "0.09765625 0.09765625" "E[X_i] = 25/256"
need pairs_check "explicit==brute: True" "explicit pair sums = brute force"
# every sample in general_n_check must show exactly one count per flip-set size
python3 - <<'PY' || fail=1
import re,ast
bad=0; n=0
for line in open("output/general_n_check.txt"):
    m=re.search(r"sizes? \{|flip-set size (\{.*?\}) odd", line)
    m=re.search(r"flip-set size (\{.*?\}) odd", line)
    if m:
        n+=1; d=ast.literal_eval(m.group(1))
        if any(len(v)!=1 for v in d.values()): bad+=1
print(("ok    " if n and not bad else "FAIL  ")+f"general_n_check: {n} samples, {bad} non-uniform")
raise SystemExit(1 if (bad or not n) else 0)
PY
[ $fail -eq 0 ] && echo "ALL KEY CHECKS PASSED" || echo "SOME CHECKS FAILED"; exit $fail
