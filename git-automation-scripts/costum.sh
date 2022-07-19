#!/usr/bin/env bash

git add -A

echo 'Enter the commit message:'
read commitmessage

git commit -m "$commitmessage"

echo 'Enter the name of the branch:'
read branch

git push origin $branch
