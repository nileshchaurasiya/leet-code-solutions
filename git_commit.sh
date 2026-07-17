#!/bin/bash
message='initial Test for sh command'

# echo "$message"

git status

git add .

git commit -m "$message"

echo "Code Commit Success...\n commit message = $message"

git push

echo "Code push Success..."