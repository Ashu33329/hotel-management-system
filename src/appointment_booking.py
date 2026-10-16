def book_appointment(patient_name, doctor_name, date):
    if not patient_name.strip():
        return "Patient name is required"
    if not doctor_name.strip():
        return "Doctor name is required"
    if not date.strip():
        return "Appointment date is required"

    return f"Appointment booked for {patient_name} with Dr. {doctor_name} on {date}"


if __name__ == "__main__":
    print(book_appointment("Rahul", "Kumar", "2026-10-20"))