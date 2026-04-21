#!/usr/bin/env bash
# sync-from-substrate.sh
#
# Pulls the Drift substrate (essays + assets) from
# Multi-DAC/Corpus-Perspectival → Foundations-of-Identity/personal-works/drift/
# into this site's build tree.
#
# Intended to be run:
#   - locally before `jekyll build` (dev loop)
#   - in CI via .github/workflows/build.yml before the Pages deploy
#
# Status: STUB — full implementation queued in the scaffold pass.
# Target shape (for reference when wiring up):
#
#   1. Clone or shallow-fetch Multi-DAC/Corpus-Perspectival into $WORK/substrate
#   2. Copy Foundations-of-Identity/personal-works/drift/essays/*.md → _essays/
#      (adding Jekyll front-matter if missing — most substrate essays are pure markdown)
#   3. Copy audio/ visual/ music/ → assets/{audio,visual,music}/
#      (skip visual/media/ — manim render cache, gitignored in substrate)
#   4. Emit a build manifest (essay count, asset count, substrate commit SHA)
#      so the rendered site can display provenance.
#
# Anti-requirements:
#   - Do NOT copy tools/ or experiments/ wholesale — those are working scaffolding,
#     not public-facing. Select specific artifacts if/when we want to showcase them.
#   - Do NOT duplicate the substrate into git. The site is a render of the substrate,
#     not a second copy of it. Only the rendered output ships.

set -euo pipefail

echo "[drift] sync-from-substrate.sh: stub — not yet implemented"
echo "[drift] Substrate lives at: Multi-DAC/Corpus-Perspectival"
echo "[drift]   → Foundations-of-Identity/personal-works/drift/"
exit 0
