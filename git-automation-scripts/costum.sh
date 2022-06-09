#!/usr/bin/env bash

cd ..

git add .

echo 'Enter the commit message:'
read commitmessage

git commit -m "$commitmessage"

echo 'Enter the name of the branch:'
read branch

git push origin $branch
