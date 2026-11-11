"""Unpack the historical Week 12 input transcripts beside portable code.

Only extracts the three peer/own numerical transcripts required by the
unmodified portable modelling routines. Saved JSON outputs, original dates
and source bytes remain in ../original/week12_original_assets.zip.

Run from anywhere:
    python journey/round_12/portable/bootstrap_assets.py

Extraction never changes the four original or four portable algorithms.
"""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parent
ARCHIVE = ROOT.parent / "original" / "week12_original_assets.zip"
EXPECTED = {
    "bbo_verified_F2.txt": "3ee22c76c8af2fc1e3c3d677dc052d3589c40d998f352bda9b124783a0e34ed4",
    "bbo_verified_F3.txt": "b2b8dfbfdc028c0d934b3bb8a6423e29ca91d52bfc89a833e7eb5b6d747c2c2e",
    "bbo_verified_F6.txt": "17dbb1ab48eca5ecf0c949a63d55a0e9c278a586321a89231c150eef99deda13",
}


def prepare():
    with ZipFile(ARCHIVE) as archive:
        for filename, expected_hash in EXPECTED.items():
            data = archive.read(filename)
            if sha256(data).hexdigest() != expected_hash:
                raise RuntimeError(f"Source checksum mismatch: {filename}")
            destination = ROOT / filename
            if destination.exists():
                if destination.read_bytes() != data:
                    raise RuntimeError(f"Refusing to overwrite a modified file: {destination}")
                print(f"Verified existing {filename}")
            else:
                destination.write_bytes(data)
                print(f"Extracted {filename}")
    print("Ready: portable Week 12 scripts share the exact archived numerical transcripts.")


if __name__ == "__main__":
    prepare()
