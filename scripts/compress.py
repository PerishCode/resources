#!/usr/bin/env python3

from __future__ import annotations

import argparse
import pathlib
import tarfile
import zipfile


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("version")
    args = parser.parse_args()

    root = pathlib.Path(__file__).resolve().parent.parent
    source_dir = root / "sources" / args.source
    if not source_dir.is_dir():
        raise SystemExit(f"missing source directory: {source_dir}")

    dist_dir = root / "dist" / args.version
    dist_dir.mkdir(parents=True, exist_ok=True)
    tarball = dist_dir / f"{args.source}-{args.version}.tar.gz"
    zipball = dist_dir / f"{args.source}-{args.version}.zip"

    with tarfile.open(tarball, "w:gz") as archive:
        archive.add(source_dir, arcname=args.source)

    with zipfile.ZipFile(zipball, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in source_dir.rglob("*"):
            if path.is_file():
                archive.write(path, arcname=path.relative_to(source_dir.parent))

    print(tarball)
    print(zipball)


if __name__ == "__main__":
    main()
