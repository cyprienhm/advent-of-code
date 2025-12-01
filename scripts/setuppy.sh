root=$(git rev-parse --show-toplevel)
out=$($root/scripts/daypath.sh $1 $2)/s.py

if [ ! -f $out ]; then
    cp $root/templates/s.py $out
else
    echo script already here
fi
