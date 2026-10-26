#!/usr/bin/env python3
"""Application tracker on a plain CSV file (no dependencies).

  python3 tools/track.py add --company Acme --role "Backend Engineer" --link URL [--fit 4] [--status Found] [--notes ...]
  python3 tools/track.py update ID [--status Applied] [--next "check reply 2026-11-03"] [--notes ...]
  python3 tools/track.py list [--status Applied] [--due]
  python3 tools/track.py stats [--by source|location|fit|company|role] [--days 7]
"""
import argparse
import csv
import datetime as dt
import re
import sys
from pathlib import Path

FILE = Path(__file__).resolve().parent.parent / "applications.csv"
COLS = ["id", "date", "company", "role", "link", "location", "source", "fit", "status", "next", "notes", "updated"]
STATUSES = ["Found", "Skipped", "Suspicious", "Ready", "Applied", "Screen", "Interview", "Offer",
            "Rejected", "Withdrawn", "Ghosted"]


def load():
    if not FILE.exists():
        return []
    with FILE.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save(rows):
    tmp = FILE.with_suffix(".tmp")
    with tmp.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)
    tmp.replace(FILE)


def today():
    return dt.date.today().isoformat()


def check_status(s):
    if s and s not in STATUSES:
        sys.exit(f"status must be one of: {', '.join(STATUSES)}")


def cmd_add(a):
    rows = load()
    check_status(a.status)
    if a.link and any(r["link"] == a.link for r in rows):
        r = next(r for r in rows if r["link"] == a.link)
        sys.exit(f"already tracked: #{r['id']} {r['company']} — {r['role']} ({r['status']})")
    rid = max((int(r["id"]) for r in rows), default=0) + 1
    rows.append({"id": rid, "date": today(), "company": a.company, "role": a.role, "link": a.link or "",
                 "location": a.location or "", "source": a.source or "", "fit": a.fit or "",
                 "status": a.status, "next": a.next or "", "notes": a.notes or "", "updated": today()})
    save(rows)
    print(f"#{rid} added: {a.company} — {a.role} [{a.status}]")


def cmd_update(a):
    rows = load()
    check_status(a.status)
    for r in rows:
        if r["id"] == str(a.id):
            for k in ("status", "next", "fit", "location", "link"):
                if getattr(a, k):
                    r[k] = getattr(a, k)
            if a.notes:
                r["notes"] = (r["notes"] + " | " if r["notes"] else "") + f"{today()} {a.notes}"
            r["updated"] = today()
            save(rows)
            print(f"#{a.id} updated: {r['company']} [{r['status']}] next: {r['next'] or '—'}")
            return
    sys.exit(f"#{a.id} not found")


def due(r):
    m = re.search(r"\d{4}-\d{2}-\d{2}", r["next"])
    return bool(m) and m.group(0) <= today()


def cmd_list(a):
    rows = load()
    if a.status:
        rows = [r for r in rows if r["status"] == a.status]
    if a.due:
        rows = [r for r in rows if due(r)]
    for r in rows:
        print(f"{r['id']:>4} | {r['date']} | {r['status']:<10} | fit {r['fit'] or '-'} | {r['company']} — {r['role']}"
              f" | {r['location']} | next: {r['next'] or '—'}")
    if not rows:
        print("nothing here")


SENT = ("Applied", "Screen", "Interview", "Offer", "Rejected", "Withdrawn", "Ghosted")
TALKS = ("Screen", "Interview", "Offer")


def cmd_stats(a):
    rows = load()
    if a.days:
        since = (dt.date.today() - dt.timedelta(days=a.days)).isoformat()
        rows = [r for r in rows if r["date"] >= since]
    by = {s: sum(r["status"] == s for r in rows) for s in STATUSES}
    sent = sum(by[s] for s in SENT)
    talks = sum(by[s] for s in TALKS)
    print(f"tracked {len(rows)} · applied {sent} · conversations {talks} · offers {by['Offer']} · rejected {by['Rejected']}")
    print(" · ".join(f"{s} {n}" for s, n in by.items() if n))
    if a.by:
        groups = {}
        for r in rows:
            groups.setdefault(r.get(a.by) or "—", []).append(r)
        print(f"\nby {a.by}: applied → conversations (rejected)")
        for g, rs in sorted(groups.items(), key=lambda kv: -sum(r["status"] in SENT for r in kv[1])):
            s = sum(r["status"] in SENT for r in rs)
            if s:
                print(f"  {g[:40]:<40} {s:>4} → {sum(r['status'] in TALKS for r in rs):>3}  ({sum(r['status'] == 'Rejected' for r in rs)})")


def main():
    p = argparse.ArgumentParser(description="Application tracker (CSV)")
    sp = p.add_subparsers(dest="cmd", required=True)
    ad = sp.add_parser("add")
    ad.add_argument("--company", required=True)
    ad.add_argument("--role", required=True)
    ad.add_argument("--link")
    ad.add_argument("--location")
    ad.add_argument("--source")
    ad.add_argument("--fit")
    ad.add_argument("--status", default="Found")
    ad.add_argument("--next")
    ad.add_argument("--notes")
    up = sp.add_parser("update")
    up.add_argument("id", type=int)
    for k in ("status", "next", "fit", "location", "link", "notes"):
        up.add_argument(f"--{k}")
    ls = sp.add_parser("list")
    ls.add_argument("--status")
    ls.add_argument("--due", action="store_true")
    st = sp.add_parser("stats")
    st.add_argument("--by", choices=["source", "location", "fit", "company", "role"])
    st.add_argument("--days", type=int)
    a = p.parse_args()
    {"add": cmd_add, "update": cmd_update, "list": cmd_list, "stats": cmd_stats}[a.cmd](a)


if __name__ == "__main__":
    main()
