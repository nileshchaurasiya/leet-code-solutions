#!/bin/bash
message='27. Remove Element'

# echo "$message"

git status

git add .

git commit -m "$message"

echo "\n\nCode Commit Success... message = $message \n\n"

git push

echo "\n\nCode push Success...\n\n"