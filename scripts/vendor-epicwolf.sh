#!/usr/bin/env bash
set -euo pipefail
# Import the selected EpicWolf fork at a reproducible version into the current
# repository. Run only on a clean, disposable branch before reviewing changes.
UPSTREAM="https://github.com/ggurov/epicwolf.git"
REVISION="e2d446b76b97a2f88a41f261a5796964dc3df68a"
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"
if [[ -e .wolf || -e .claude ]]; then
  echo "Refusing to overwrite .wolf or .claude. Review and merge manually." >&2
  exit 2
fi
TEMP="$(mktemp -d)"
trap 'rm -rf "$TEMP"' EXIT
git clone --quiet "$UPSTREAM" "$TEMP/upstream"
git -C "$TEMP/upstream" checkout --quiet --detach "$REVISION"
test "$(git -C "$TEMP/upstream" rev-parse HEAD)" = "$REVISION"
cp -a "$TEMP/upstream/.wolf" "$ROOT/.wolf"
cp -a "$TEMP/upstream/.claude" "$ROOT/.claude"
cp "$TEMP/upstream/LICENSE" "$ROOT/EPICWOLF-LICENSE" 
printf '%s\n' "$UPSTREAM@$REVISION" > "$ROOT/EPICWOLF-UPSTREAM.txt"
echo "Vendored EpicWolf $REVISION. Review .claude hooks and run Node tests before merging."
echo "Files have been staged nowhere; inspect with git status and git diff --no-index as needed."
