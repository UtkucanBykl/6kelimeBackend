#!/bin/bash

TOKEN=$TOKEN
CHAT_ID=$CHAT_ID
MESSAGE='Status :'$STATU 'Commit => https://github.com/UtkucanBykl/6kelimeBackend/commit/'$TRAVIS_COMMIT' Commit Message: '$TRAVIS_COMMIT_MESSAGE' Event Type: '$TRAVIS_EVENT_TYPE' Branch: '$TRAVIS_PULL_REQUEST_BRANCH
URL="https://api.telegram.org/bot$TOKEN/sendMessage"

curl -s -X POST $URL -d chat_id=$CHAT_ID -d text="$MESSAGE"
