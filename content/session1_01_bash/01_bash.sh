#!/usr/bin/bash

#Lukas Steinwender
#NOTE: run from project root!


#%%useful commands for exploration
pwd #current working directory
ls .
ls content -alrt
echo ""

head ./README.md
echo ""

tail ./README.md
echo ""

cat ./README.md
echo ""

grep "requirements" *.*
echo ""

find -name "README.md"
echo ""

#%%appending to PATH
echo $PATH
export PATH="$PATH:/some/path"
echo $PATH

#%%sourcing (and activating venvs)
source .venv/bin/activate
which python3    #shows which installation of python is in use

#some python scripts
python3 <<EOF
import pandas as pd
print(pd.__version__)
EOF
deactivate

