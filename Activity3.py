print("ExamEligibility...")
Attendance= int(input("Enter Attendance: "))
medical_cause=input("Enter yes/no for medical cause: ")
if Attendance>= 75:
    print("Eligible for Exam")
else:
   if medical_cause=="yes":
       print("Eligible for Exam")
   else:
      print("Not Eligible for exam")