#!/usr/bin/env python3
"""Auto-configure repository URL placeholders across metadata files."""
import argparse, json, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def infer_repo():
    try:
        url = subprocess.check_output(["git","config","--get","remote.origin.url"], cwd=ROOT, text=True).strip()
    except Exception:
        return None
    m = re.search(r"github\.com[/:]([^/]+)/([^/]+?)(?:\.git)?$", url)
    return f"{m.group(1)}/{m.group(2)}" if m else None

def replace_in_file(path: Path, pattern: str, repl: str):
    txt = path.read_text(encoding="utf-8")
    path.write_text(re.sub(pattern, repl, txt, flags=re.M), encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=None, help="org/repo; inferred from git origin if omitted.")
    args = ap.parse_args()

    repo = args.repo or infer_repo()
    if not repo:
        raise SystemExit("Could not infer repo. Use --repo ORG/REPO.")
    url = f"https://github.com/{repo}"

    cff = ROOT/"CITATION.cff"
    if cff.exists():
        replace_in_file(cff, r'^repository-code:\s*".*"$', f'repository-code: "{url}"')
    bib = ROOT/"CITATION.bib"
    if bib.exists():
        replace_in_file(bib, r'url\s*=\s*\{https://github\.com/[^}]*\}', f'url          = {{{url}}}')
    cm = ROOT/"codemeta.json"
    if cm.exists():
        data = json.loads(cm.read_text(encoding="utf-8"))
        data["codeRepository"] = url
        cm.write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    rd = ROOT/"README.md"
    if rd.exists():
        txt = rd.read_text(encoding="utf-8").replace("<ORG>/<REPO>", repo).replace("https://github.com/<ORG>/<REPO>", url)
        rd.write_text(txt, encoding="utf-8")

    print("Updated repo metadata to:", repo)

if __name__ == "__main__":
    main()
