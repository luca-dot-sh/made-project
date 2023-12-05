#!/bin/bash

# Run from root folder of repo. Install requirements.txt first as described in README.

python3 project/system_level_test.py
if [ $? -eq 0 ]
then
    echo "---------------------------- System Level Test SUCCESSFUL------------------------"
else
    echo "---------------------------- System Level Test FAILED------------------------"
fi
printf "\n\n\n"

pytest project/unittests.py