import uuid

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Patient(Person):
    def __init__(self, name, age, gender, illness):
        super().__init__(name, age, gender)
        self.illness = illness
        self.id = str(uuid.uuid4())[:8]

class Doctor(Person):
    def __init__(self, name, age, gender, speciality):
        super().__init__(name, age, gender)
        self.speciality = speciality
        self.id = str(uuid.uuid4())[:8]

class Appointment:
    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.id = str(uuid.uuid4())[:8]

class Hospital:
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.appointments = []

    def add_doctor(self, name, age, gender, speciality):
        doctor = Doctor(name, age, gender, speciality)
        self.doctors.append(doctor)
        print(f"Doctor {doctor.name} added with ID: {doctor.id}")
        return doctor

    def add_patient(self, name, age, gender, illness):
        patient = Patient(name, age, gender, illness)
        self.patients.append(patient)
        print(f"Patient {patient.name} added with ID: {patient.id}")
        return patient

    def schedule_appointment(self, patient_id, doctor_id, date):
        patient = next((p for p in self.patients if p.id == patient_id), None)
        doctor = next((d for d in self.doctors if d.id == doctor_id), None)
        if patient and doctor:
            appointment = Appointment(patient, doctor, date)
            self.appointments.append(appointment)
            print(f"Appointment scheduled for {patient.name} with Dr. {doctor.name} on {date}")
            return appointment
        else:
            print("Invalid patient or doctor ID")
            return None

    def view_patients(self):
        print('------- Patients -------')
        for p in self.patients:
            print(f"ID: {p.id}, Name: {p.name}, Age: {p.age}, Gender: {p.gender}, Illness: {p.illness}")

    def view_doctors(self):
        print('------- Doctors -------')
        for d in self.doctors:
            print(f"ID: {d.id}, Name: {d.name}, Age: {d.age}, Gender: {d.gender}, Speciality: {d.speciality}")

    def generate_bill(self, patient_id):
        patient = next((p for p in self.patients if p.id == patient_id), None)
        if patient:
            bill = 500  # Fixed amount for simplicity
            print(f"Bill for {patient.name}: ₹{bill}")
            return bill
        else:
            print("Invalid patient ID")
            return None

    def view_appointments(self):
        print('------- Appointments -------')
        for a in self.appointments:
            print(f"ID: {a.id}, Patient: {a.patient.name}, Doctor: Dr. {a.doctor.name}, Date: {a.date}")

    def cancel_appointment(self, appointment_id):
        appointment = next((a for a in self.appointments if a.id == appointment_id), None)
        if appointment:
            self.appointments.remove(appointment)
            print(f"Appointment with ID {appointment.id} cancelled")
        else:
            print("Invalid appointment ID")

# --- Runtime Menu ---

if __name__ == "__main__":
    hospital = Hospital()

    while True:
        print("\n========== Hospital Management ==========")
        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. Schedule Appointment")
        print("4. View Patients")
        print("5. View Doctors")
        print("6. Generate Bill")
        print("7. View Appointments")
        print("8. Cancel Appointment")
        print("9. Exit")
        print("=========================================")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter doctor's name: ")
            age = int(input("Enter doctor's age: "))
            gender = input("Enter gender: ")
            speciality = input("Enter speciality: ")
            hospital.add_doctor(name, age, gender, speciality)

        elif choice == '2':
            name = input("Enter patient's name: ")
            age = int(input("Enter patient's age: "))
            gender = input("Enter gender: ")
            illness = input("Enter illness: ")
            hospital.add_patient(name, age, gender, illness)

        elif choice == '3':
            patient_id = input("Enter patient ID: ")
            doctor_id = input("Enter doctor ID: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            hospital.schedule_appointment(patient_id, doctor_id, date)

        elif choice == '4':
            hospital.view_patients()

        elif choice == '5':
            hospital.view_doctors()

        elif choice == '6':
            patient_id = input("Enter patient ID: ")
            hospital.generate_bill(patient_id)

        elif choice == '7':
            hospital.view_appointments()

        elif choice == '8':
            appointment_id = input("Enter appointment ID: ")
            hospital.cancel_appointment(appointment_id)

        elif choice == '9':
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
