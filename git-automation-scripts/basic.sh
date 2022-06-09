#!/usr/bin/env bash

cd ..

git add .

DATE=$(date)

git commit -m "$DATE"

git push origin main
