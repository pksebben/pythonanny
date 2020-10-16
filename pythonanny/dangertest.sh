#!/bin/bash

python3 nanny.py &
python3 dangerfailtest.py && exit
