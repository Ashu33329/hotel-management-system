
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from patient_registration import register_patient


def test_valid_patient():
    assert register_patient("Rahul", 25, "Fever") == "Patient Rahul registered successfully"


def test_empty_name():
    assert register_patient("", 25, "Fever") == "Patient name is required"


def test_invalid_age():
    assert register_patient("Rahul", 0, "Fever") == "Age must be greater than zero"
