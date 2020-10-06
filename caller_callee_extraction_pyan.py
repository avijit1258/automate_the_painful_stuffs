#!/bin/bash

# I need to clone a git repository
# provide the address to pyan for extracting caller callee
# get the output file with proper naming
# python caller_callee_extraction_pyan.py 'https://github.com/avijit1258/pyan' '/home/avijit/Github/pyan/pyan.py'
# python caller_callee_extraction_pyan.py 'https://github.com/scipy/scipy/' '/home/avijit/Github/pyan/pyan.py'
# /home/avijit/Github/updated_pyan/pyan/pyan3 *.py   --uses --no-defines --colored --grouped --annotated  -f fastapi.txt --uses --no-defines --tgf

import sys
import os
from datetime import datetime

repository = sys.argv[1]
pyan = sys.argv[2]


# os.system("mkdir temp")
# os.system("cd temp")

print("Cloning repo: ", repository)

git_clone = "git clone  "+ repository

os.system(git_clone)
current_wd = os.getcwd()
target_repo = current_wd + "/" + repository.split('/')[4]

output_file = repository.split('/')[4] + "_" +datetime.now().strftime("%m_%d_%Y")+ ".txt"

# execute_pyan = "python3 " + pyan + " " + target_repo+ "/**/*.py " + target_repo+ "/*.py --uses --no-defines --colored --grouped --annotated  -f " + output_file + " --uses --no-defines --tgf"
execute_pyan = "python3 " + pyan + " " + target_repo + " --uses --no-defines --colored --grouped --annotated  -f " + output_file + " --uses --no-defines --tgf"
print(execute_pyan)

os.system(execute_pyan)
os.system("rm -r "+ repository.split('/')[4])
