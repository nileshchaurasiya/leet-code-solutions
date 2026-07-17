#!/bin/bash
message='initial Test for sh command'

# echo "$message"

git status

git add .

git commit -m "$message"

echo "\n\nCode Commit Success... message = $message \n\n"

git push

echo "\n\nCode push Success..."