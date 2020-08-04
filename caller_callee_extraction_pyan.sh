#!/bin/bash

# I need to clone a git repository
# provide the address to pyan for extracting caller callee
# get the output file with proper naming
# sh caller_callee_extraction_pyan.sh 'https://github.com/avijit1258/pyan.git' '/home/avijit/Github/pyan'

repository=$1
pyan=$2

mkdir temp
cd temp

echo "Cloning repo: $repository"
git clone $repository


