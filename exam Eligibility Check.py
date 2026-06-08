#take input for the student that he can attend the exam or not
medical_cause=input("did you have a medical cause? (Y/N): ").strip() .upper()

#checking the user input and predicting output accordingly
if medical_cause=='Y': #condition 1
    print("YOU ARE ALLOWED")
else:
    #take input of the attendance
    atten=int(input("enter the attendance of the student: "))


    if atten >=75: #condition 2
        print("ALLOWED")
    else:
        print("NOT ALLOWED")