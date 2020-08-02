#!/bin/bash

# I need to clone a git repository
# provide the address to pyan for extracting caller callee
# get the output file with proper naming

repository=$1

mkdir temp
cd temp

echo 'Cloning repo: $repository'
git clone $repository

