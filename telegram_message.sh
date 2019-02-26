#!/bin/bash

TOKEN=$TOKEN
CHAT_ID=$CHAT_ID
COMMIT_URL='https://github.com/UtkucanBykl/6kelimeBackend/commit/'
MESSAGE='Status :'$STATU 'Commit => '$COMMIT_URL$TRAVIS_COMMIT' Commit Message: '$TRAVIS_COMMIT_MESSAGE' Event Type: '$TRAVIS_EVENT_TYPE' Branch: '$TRAVIS_PULL_REQUEST_BRANCH
URL="https://api.telegram.org/bot$TOKEN/sendMessage"

curl -s -X POST $URL -d chat_id=$CHAT_ID -d text="$MESSAGE"
