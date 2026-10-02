"""Reusable helpers for summarizing clinic systolic readings."""


def systolic_readings(encounters):
    """TODO: describe what this pulls out of the encounter records."""
    # TODO: collect the systolic value of every encounter into one list.
    readings = []
    for encounter in encounters:
        readings.append(encounter["systolic"]) 
    return readings


def mean_systolic(readings):
    """TODO: describe what this returns, including the empty-list result."""
    # TODO: return None when there is nothing to average, then sum() / len().
    if not readings:
        return None
    return sum(readings)/len(readings)
    


def count_patients(encounters):
    """TODO: describe what this counts."""
    # TODO: collect the patient IDs and keep only the distinct ones.
    patients = encounters 
    patients = set(patients)
    return len(patients)


def patients_at_or_above(encounters, cutoff):
    """TODO: describe which patient IDs come back."""
    # TODO: keep each patient whose systolic reading is at or above cutoff.
    flagged_ids = []
    for encounter in encounters:
        if encounter["systolic"] >= cutoff:
            flagged_ids.append(encounter["patient_id"])
    return flagged_ids
