root=$(git rev-parse --show-toplevel)
cookie=$(cat $root/scripts/cookie.txt)
out_input=$($root/scripts/daypath.sh $1 $2)/input.txt

if [ ! -f $out_input ]; then
    curl "https://adventofcode.com/$1/day/$2/input" \
        --compressed \
        -H 'User-Agent: curl' \
        -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
        -H 'Accept-Language: en-US,en;q=0.5' \
        -H 'Accept-Encoding: gzip, deflate, br, zstd' \
        -H "Cookie: session=$cookie" \
        -o $out_input
else
    echo input already here
fi

out_example=$($root/scripts/daypath.sh $1 $2)/example.txt
if [ ! -f $out_example ]; then
    touch $out_example
else
    echo example already here
fi

