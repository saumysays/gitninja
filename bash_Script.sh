#!/bin/bash

date=$1
commit_msg=$2
git add .
git commit -m "$commit_msg" --amend --date="$date"
git push -f