#!/usr/bin/env python3
"""Estimate G from already calibrated differential torques.

Input CSV columns:
  torque_Nm,geometry_factor,torque_unc_Nm
The geometry_factor has units kg²/m, so G * geometry_factor is a torque (N m).
IMPORTANT: This does NOT infer torque from raw angles. That requires an
independently calibrated torsion-balance forward model.
"""
import argparse
import csv
import json
import math


def estimate(rows):
    """Weighted fit through origin: torque_i = G * geometry_factor_i + noise_i."""
    numerator = denominator = 0.0
    count = 0
    for row in rows:
        y = float(row["torque_Nm"])
        k = float(row["geometry_factor"])
        sigma = float(row["torque_unc_Nm"])
        if not all(map(math.isfinite, (y, k, sigma))) or sigma <= 0:
            raise ValueError("Values must be finite and uncertainties positive")
        numerator += y * k / sigma**2
        denominator += k * k / sigma**2
        count += 1
    if not count or denominator <= 0 or not math.isfinite(denominator):
        raise ValueError("No identifiable G: missing or zero geometry factors")
    return {"G_estimate_SI": numerator / denominator,
            "statistical_standard_uncertainty_SI": math.sqrt(1 / denominator),
            "n": count,
            "warning": "Statistical uncertainty only; systematic and geometry uncertainties NOT included."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", help="CSV of calibrated torques and geometry factors")
    args = parser.parse_args()
    with open(args.csv_file, newline="", encoding="utf-8-sig") as handle:
        result = estimate(csv.DictReader(handle))
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
