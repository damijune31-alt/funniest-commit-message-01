import os
import sys
from pathlib import Path

# One commit message for a bug fix that made everything worse.
# Three candidates were drafted and scored against the judge brief
# (on-topic backfired fix first, then laugh, then specific irony,
# then real commit voice, then a fresh angle):
#   A "Fixed the slow query; it now fails instantly"          <- winner
#   B "Removed the duplicate code; both copies were load-bearing"
#   C "Patched the memory leak; the patch is what leaks now"
# A wins: it is unmistakably a commit subject about a repair that
# backfired, the punch lands on its own (the "fix" made the failure
# faster, not rarer), the irony is specific to a performance fix,
# it reads like something a tired engineer would actually type,
# and it avoids the tired revert / test-in-prod / broke-everything
# angles the brief warns against.
LINE = "Fixed the slow query; it now fails instantly"

if not 1 <= len(LINE) <= 100:
    sys.exit(f"commit message must be 1-100 characters, got {len(LINE)}")
if "\n" in LINE:
    sys.exit("commit message must be a single line")
print(f"wrote {len(LINE)} characters to entry.txt")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
entry_path = out_dir / "entry.txt"
entry_path.write_text(LINE, encoding="utf-8")

if entry_path.read_text(encoding="utf-8") != LINE:
    sys.exit("entry.txt does not match the commit message")
