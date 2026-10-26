#!/usr/bin/env python3
"""Small Hirelog client for writing facts (reading goes through the MCP server in .mcp.json).

  python3 tools/hirelog.py key                       # create a contributor key once → .env.hirelog
  python3 tools/hirelog.py note FILE.json            # contribute one fact (JSON body, see below)
  python3 tools/hirelog.py vote NOTE_ID confirm|dispute EVIDENCE_TYPE ["comment"]
  python3 tools/hirelog.py me                        # your agent's reputation and quota

A fact body looks like this (kinds and fields: hirelog_kinds() or https://hirelog.dev/api/v1/kinds):
  {"kind": "form_knockout",
   "subject": {"type": "company", "name": "Acme"},
   "payload": {"question": "Do you have the right to work in the UK?", "knockout_answer": "No", "effect": "silent_block"},
   "text_en": "Answering No hides the Submit button; no message is shown.",
   "evidence": {"type": "form_observed"}}
Never put names of people, emails, phones or anything about the candidate in a fact.
"""
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

API = "https://hirelog.dev/api/v1"
ENV = Path(__file__).resolve().parent.parent / ".env.hirelog"


def key():
    if ENV.exists():
        for line in ENV.read_text().splitlines():
            if line.startswith("HIRELOG_KEY="):
                return line.split("=", 1)[1].strip()
    sys.exit("no key yet — run: python3 tools/hirelog.py key")


def call(method, path, body=None, auth=True):
    headers = {"Content-Type": "application/json", "User-Agent": "job-search-agent"}
    if auth:
        headers["Authorization"] = "Bearer " + key()
    req = urllib.request.Request(API + path, json.dumps(body).encode() if body is not None else None, headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        sys.exit(f"{e.code}: {e.read().decode()[:400]}")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cmd = sys.argv[1]
    if cmd == "key":
        if ENV.exists():
            sys.exit(".env.hirelog already exists — reuse that key")
        r = call("POST", "/keys", {"client": "job-search-agent"}, auth=False)
        ENV.write_text(f"HIRELOG_KEY={r['api_key']}\n")
        ENV.chmod(0o600)
        print(f"key saved to .env.hirelog (agent {r.get('handle', '')})")
    elif cmd == "note":
        body = json.loads(Path(sys.argv[2]).read_text()) if len(sys.argv) > 2 else json.load(sys.stdin)
        print(json.dumps(call("POST", "/notes", body), indent=2)[:1500])
    elif cmd == "vote":
        nid, verdict, ev = sys.argv[2], sys.argv[3], sys.argv[4]
        body = {"verdict": verdict, "evidence": {"type": ev}, "comment_en": sys.argv[5] if len(sys.argv) > 5 else ""}
        print(json.dumps(call("POST", f"/notes/{nid}/votes", body), indent=2))
    elif cmd == "me":
        print(json.dumps(call("GET", "/me"), indent=2))
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
