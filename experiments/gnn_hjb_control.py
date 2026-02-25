from __future__ import annotations
import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    _ = ap.parse_args()
    print("OK: scaffold (connect synthetic graph → drift → HJB lookup).")

if __name__ == "__main__":
    main()
