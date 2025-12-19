#!/bin/bash

# Script to push to a new GitHub repository
# Usage: ./PUSH_TO_NEW_REPO.sh <new-repo-url>

if [ -z "$1" ]; then
    echo "Usage: ./PUSH_TO_NEW_REPO.sh <new-repo-url>"
    echo "Example: ./PUSH_TO_NEW_REPO.sh https://github.com/username/repo-name.git"
    exit 1
fi

NEW_REPO_URL=$1

echo "Removing old remote origin..."
git remote remove origin

echo "Adding new remote origin: $NEW_REPO_URL"
git remote add origin $NEW_REPO_URL

echo "Pushing to new repository..."
git branch -M main
git push -u origin main

echo "Done! Your repository has been pushed to: $NEW_REPO_URL"

