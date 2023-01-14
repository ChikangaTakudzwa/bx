#!/bin/bash

tkn pipeline start bx-pipeline \
-p repo-url="https://github.com/ChikangaTakudzwa/bx.git" \
-p branch="cd" \
-p build-image="" \
-w name=bx-workspace,claimName=bx-pvc \
-s pipeline \
--showlog