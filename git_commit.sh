#!/bin/bash
message='initial Test for sh command'

# echo "$message"

git status

git add .

git commit -m "$message"

git push

echo "Code push Success...\n commit message = $message"