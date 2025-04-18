#!/bin/bash

# 用法: ./release.sh v0.1.2 "说明文字"

# 检查参数
if [ $# -lt 1 ]; then
  echo "❗ 用法: $0 <version_tag> [message]"
  exit 1
fi

TAG=$1
MESSAGE=${2:-"Release $TAG"}

# 删除旧 tag（本地 + 远程）
echo "🧹 删除旧 tag（如果存在）..."
git tag -d $TAG 2>/dev/null
git push origin :refs/tags/$TAG 2>/dev/null

# 添加新的 tag
echo "🏷️  创建新 tag: $TAG"
git tag -a $TAG -m "$MESSAGE"

# 推送 tag，触发 GitHub Actions
echo "🚀 推送 tag 到远程，触发 GitHub Actions..."
git push origin $TAG

echo "✅ 完成！请稍等几分钟，在 GitHub Releases 页面查看构建结果："
echo "   https://github.com/$(git remote get-url origin | sed -E 's#.*github.com[:/](.+)\.git#\1#')/releases/tag/$TAG"
