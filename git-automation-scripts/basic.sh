#!/usr/bin/env bash

git add -A

DATE=$(date)

git commit -m "$DATE"

git push origin main
