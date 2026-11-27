"""Seven letters. That's the whole verdict."""

from pathlib import Path

OUT_DIR = Path("/output")
OUT_FILE = OUT_DIR / "entry.txt"


def spell_it():
    chunks = ("St", "op", "ga", "p")
    return "".join(chunks)


def main():
    word = spell_it()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_bytes(word.encode("utf-8"))


if __name__ == "__main__":
    main()
