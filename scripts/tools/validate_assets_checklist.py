#!/usr/bin/env python3
"""Valida assets_checklist.json para builds de desenvolvimento e release."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

VALID_STATUSES = {"PENDING", "GENERATED", "APPROVED"}


def load_checklist(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def validate_schema(data: dict) -> list[str]:
    errors: list[str] = []
    if "prototype_assets" not in data or not isinstance(data["prototype_assets"], list):
        errors.append("Campo 'prototype_assets' ausente ou inválido.")
        return errors

    for index, asset in enumerate(data["prototype_assets"]):
        if not isinstance(asset, dict):
            errors.append(f"Asset na posição {index} não é objeto.")
            continue

        asset_id = asset.get("id")
        status = asset.get("status")

        if not asset_id or not isinstance(asset_id, str):
            errors.append(f"Asset na posição {index} sem 'id' válido.")

        if status not in VALID_STATUSES:
            errors.append(
                f"Asset '{asset_id or index}' com status inválido '{status}'. "
                f"Use um de {sorted(VALID_STATUSES)}."
            )

    return errors


def validate_mode(data: dict, mode: str) -> list[str]:
    errors: list[str] = []
    assets = data.get("prototype_assets", [])

    if mode == "release":
        pending = [a["id"] for a in assets if a.get("status") != "APPROVED"]
        if pending:
            errors.append(
                "Build de release bloqueada: os seguintes assets não estão APPROVED: "
                + ", ".join(pending)
            )

    if mode == "dev":
        pending = [a["id"] for a in assets if a.get("status") == "PENDING"]
        if pending:
            errors.append(
                "Build de desenvolvimento bloqueada: existem assets PENDING: "
                + ", ".join(pending)
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validador de checklist de assets")
    parser.add_argument("--mode", choices=["dev", "release"], default="dev")
    parser.add_argument("--file", default="assets_checklist.json")
    args = parser.parse_args()

    checklist = load_checklist(Path(args.file))

    errors = validate_schema(checklist)
    errors.extend(validate_mode(checklist, args.mode))

    if errors:
        for error in errors:
            print(f"[ERRO] {error}")
        return 1

    print(f"[OK] Checklist válida para modo '{args.mode}'.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
