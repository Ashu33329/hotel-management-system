
def register_patient(name, age, disease):
    if not name.strip():
        return "Patient name is required"
    if age <= 0:
        return "Age must be greater than zero"
    if not disease.strip():
        return "Disease is required"

    return f"Patient {name} registered successfully"


if __name__ == "__main__":
    print(register_patient("Rahul", 25, "Fever"))
