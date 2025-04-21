#!/bin/bash
set -e

git add -A
git commit -m "${1:-update}"
git push origin main
echo "✅ main 分支已更新，无需发版"
