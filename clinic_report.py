#!/usr/bin/env python3
"""Summarize one week of clinic encounters and save the two report files."""

from pathlib import Path

from vitals_tools import (
    count_patients,
    mean_systolic,
    patients_at_or_above,
    systolic_readings,
)


DATA_PATH = Path("data") / "clinic_encounters.csv"
OUTPUT_DIR = Path("output")


def read_encounters(data_path):
    """TODO: describe what one usable encounter looks like.

    Give back two values: the list of usable encounters, and how many data
    rows you skipped. `main()` unpacks them the way the lecture unpacks a
    tuple, with two names on the left of the `=`.
    """
    with data_path.open("r", encoding="utf-8") as data_file:
        rows = data_file.readlines()
    encounters = []
    skipped = 0
    for row in rows[1:]:
        if not row.strip():
            print("Skipping a blank row.")
            skipped +=1
            continue
        fields = row.strip().split(",")
        if len(fields) != 3:
            print(f"Skipping a row with {len(fields)} fields: {row.strip()}")
            skipped +=1
            continue
        patient_id, visit_date, raw_systolic = fields
        try: 
            systolic = int(raw_systolic)
        except ValueError as error:
            print(f"Skipping {patient_id}: {error}")
            skipped += 1
            continue
        if 60 <= systolic <= 250:
            encounters.append({"patient_id": patient_id, "date": visit_date, "systolic": systolic})
        else:
            print("Skipping a row with erroneous systolic")
            skipped += 1
            
    # TODO: read the rows and skip the header line.
    # TODO: keep a row only when it has three fields, int() can read the
    #       systolic field, and the reading is plausible.
    # TODO: count every other data row as skipped, the blank line included,
    #       and print one line per skipped row so you can see what dropped out.
    # TODO: end with `return encounters, skipped`.
    return encounters, skipped
    


def main():
    """TODO: describe the two artifacts this writes."""
    encounters, skipped = read_encounters(DATA_PATH)

    # TODO: build the six report lines and write them to output/vitals_report.txt.
    # TODO: read the file back and print it, so you can see what was saved.
    # TODO: choose your follow-up cutoff, then write output/followup_list.txt
    #       with the Cutoff line, the Reason line, and one patient ID per line.
    readings = systolic_readings(encounters)
    min_read = min(readings)
    max_read = max(readings)
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)           # no error when output/ already exists
    report_path = output_dir / "vitals_report.txt"
    with open(report_path, "w", encoding="utf-8") as report_file:
        report_file.write(f"Usable encounters: {len(encounters)}\n")
        report_file.write(f"Skipped rows: {skipped}\n")
        report_file.write(f"Patients seen: {count_patients(readings)}\n")
        report_file.write(f"Mean systolic: {mean_systolic(readings):.2f} mmHg\n")
        report_file.write(f"Highest systolic: {max_read} mmHg\n")
        report_file.write(f"Lowest systolic: {min_read} mmHg\n")
    followup_path = output_dir / "followup_list.txt"
    cutoff = 120
    followups = patients_at_or_above(encounters, cutoff)
    with open(followup_path, "w", encoding="utf-8") as followup_file:
        followup_file.write(f"Cutoff: {cutoff} mmHg\n")
        followup_file.write(f"Reason: I picked the lowest possible value to capture as many as possible for followup.\n")
        for followup in followups:
            followup_file.write(f"{followup}\n")


if __name__ == "__main__":
    main()
