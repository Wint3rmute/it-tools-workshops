echo Working on $1 ...
echo ctrl+c to stop live-compilation
. venv/bin/activate
echo $1 | entr ./prometheus.py -i $1
