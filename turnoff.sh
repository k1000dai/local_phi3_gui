#! /bin/bash
#do not kill if the process is not running
if [ -z "$(ps $! | grep '[f]or_phi3/bin/python')" ]; then
    echo "Streamlit is not running"
    exit 1
fi
pnum=$(ps $! | grep "[f]or_phi3/bin/python")
pnum=$(echo $pnum | awk '{print $1}')
kill $pnum