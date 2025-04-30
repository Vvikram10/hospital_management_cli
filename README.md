# 🏥 Hospital Management System (Python Project)

This is a command-line based **Hospital Management System** implemented using **Object-Oriented Programming (OOP)** in Python. It allows management of doctors, patients, appointments, and bills in a simple interactive terminal interface.

---

## 📌 Features

- ➕ Add Doctors and Patients
- 📅 Schedule Appointments
- 📄 View Doctors, Patients, and Appointments
- 💵 Generate Bills
- ❌ Cancel Appointments
- 🔁 Interactive runtime loop until exit

---

## 🛠️ Technologies Used

Core Python
## 🚀 How to Run

1. **Clone this Repository:**

```bash
git clone https://github.com/your-username/hospital-management-system.git
cd hospital-management-system
python hospital_management.py

```
hospital-management-system/
│
├── hospital_management.py   # Main Python script
├── README.md                # Project documentation



## Outputs 


- Python 3.x
- OOP Concepts (`Classes`, `Inheritance`)
- UUID for unique ID generation
- CLI Input/Output

---
```
========== Hospital Management ==========

```
1. Add Doctor
2. Add Patient
3. Schedule Appointment
4. View Patients
5. View Doctors
6. Generate Bill
7. View Appointments
8. Cancel Appointment
9. Exit
 ```
=========================================
```
Enter your choice: 1
Enter doctor's name: vikram
Enter doctor's age: 23
Enter gender: male
Enter speciality: fever
Doctor vikram added with ID: 68f9d93f

```
========== Hospital Management ==========
```

Enter your choice: 5
------- Doctors -------
ID: 68f9d93f, Name: vikram, Age: 23, Gender: male, Speciality: fever

```
========== Hospital Management ==========
```
Enter your choice: 2
Enter patient's name: parikshit
Enter patient's age: 22
Enter gender: male
Enter illness: fever
Patient parikshit added with ID: c45fb345

```
========== Hospital Management ==========
```
Enter your choice: 4
------- Patients -------
ID: c45fb345, Name: parikshit, Age: 22, Gender: male, Illness: fever

```
========== Hospital Management ==========
```
Enter your choice: 3
Enter patient ID: c45fb345
Enter doctor ID: 68f9d93f
Enter appointment date (YYYY-MM-DD): 2025-04-30
Appointment scheduled for parikshit with Dr. vikram on 2025-04-30

```
========== Hospital Management ==========
```
Enter your choice: 7
------- Appointments -------
ID: e1ed6cf1, Patient: parikshit, Doctor: Dr. vikram, Date: 2025-04-30

```
========== Hospital Management ==========
```
Enter your choice: 6
Enter patient ID: e1ed6cf1
Invalid patient ID
```

========== Hospital Management ==========
```
Enter your choice: 6
Enter patient ID: c45fb345
Bill for parikshit: ₹500

```
========== Hospital Management ==========
```
Enter your choice: 8
Enter appointment ID: e1ed6cf1
Appointment with ID e1ed6cf1 cancelled

```
========== Hospital Management ==========
```
Enter your choice: 9
Exiting system. Goodbye!

