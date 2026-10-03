"""Reusable helpers for summarizing clinic systolic readings."""


def systolic_readings(encounters):
    """TODO: Places all systolic values of valid encounters into a list."""
    # TODO: collect the systolic value of every encounter into one list.
    readings = []
    for encounter in encounters:
        readings.append(encounter["systolic"]) 
    return readings


def mean_systolic(readings):
    """TODO: Returns average systolic reading, including for empty list."""
    # TODO: return None when there is nothing to average, then sum() / len().
    if not readings:
        return None
    return sum(readings)/len(readings)
    


def count_patients(encounters):
    """TODO: Retain only unique patient IDs."""
    # TODO: collect the patient IDs and keep only the distinct ones.
    patients = encounters 
    patients = set(patients)
    return len(patients)


def patients_at_or_above(encounters, cutoff):
    """TODO: Returns patient IDs with systolic readings at or above cutoff."""
    # TODO: keep each patient whose systolic reading is at or above cutoff.
    flagged_ids = []
    for encounter in encounters:
        if encounter["systolic"] >= cutoff:
            flagged_ids.append(encounter["patient_id"])
    return flagged_ids
