root=$(git rev-parse --show-toplevel)
out=$root/$(printf "%d/day_%02d" $1 $2)
echo $out
