"""Emit exactly one word, 'Practice', into /output/entry.txt."""

from pathlib import Path


def main() -> None:
    out_path = Path("/output/entry.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("Practice", encoding="utf-8")


if __name__ == "__main__":
    main()
