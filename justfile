qsetup:
  #!/usr/bin/env bash
  year=$(echo {{ invocation_directory() }} | rg '(\d{4})' -o)
  day=$(echo {{ invocation_directory() }} | rg 'day_0?(\d+)' -o -r '$1')
  just setup $year $day

setup year day:
  scripts/getinput.sh {{year}} {{day}}
  scripts/setuppy.sh {{year}} {{day}}
