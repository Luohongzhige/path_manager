#!/bin/bash
set -e

# 获取版本号
VERSION=$(grep '^version *= *' pyproject.toml | sed -E 's/version *= *"([^"]+)"/\1/')
TAG="v$VERSION"

echo "🏷️  当前版本为: $VERSION"
echo "🏷️  准备打 tag: $TAG"

# 确保 tag 不存在
if git rev-parse "$TAG" >/dev/null 2>&1; then
  echo "❌ Tag $TAG 已存在，发布失败"
  exit 1
fi

# 添加更改并提交（可选）
git add -A
git commit -m "release: $TAG" || echo "⚠️ 无需提交"

# 打 tag 并推送
git tag $TAG
git push origin main
git push origin $TAG

echo "✅ 发布成功，tag: $TAG"
