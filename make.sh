#!/usr/bin/bash
# Generates pelican content
pelican content
# Commits and pushes using given message. Files automatically staged with -a flag
read -p "Commit Message: " m
git commit -a -m "$m"
git push origin master
# Uses ghp-import package to commit and push pelican output files to gh-pages branch.
ghp-import -p output