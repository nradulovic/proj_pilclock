#!/bin/bash

if [ -f bin/activate ]; then
    . bin/activate
fi

python3 -m pilclock || retval=$? && true

if [ -f bin/activate ]; then
    deactivate
fi

exit ${retval}
