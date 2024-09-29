class Students:
    
    #this function is to search for a student in the database txt
    def search_student(student_list, matric_number):
        
        for student, details in student_list.items():
            
            if student.lower() == matric_number.lower():
        
                return {
                    "First Name": details["First Name"],
                    "Last Name": details["Last Name"],
                    "Phone Number": details["Phone Number"],
                    "Matric Number": details["Matric Number"],
                    "Email Address": details["Email"]  
                }
        
        return None 
    
     #this function print student infomation
    def print_student_info(student):
        
        if student != None:
            
            print("Students Details:")
            print(f"First Name: {student['First Name']}")  
            print(f"Last Name: {student['Last Name']}")
            print(f"Phone Number: {student['Phone Number']}")
            print(f"Matric Number: {student['Matric Number']}")
            print(f"Email Address: {student['Email Address']}")  

        else:
            print("Student Not Found")
            
    #this function adds a new student to the student list and return the updated student list to the student database txt
    def add_new_student(new_student, student_list):
       
        matric_number = new_student["Matric Number"]
        student_list[matric_number] = new_student
        
        return student_list   
    
    #this function updates the student details in the student database txt
    def update_student(new_update, matric_number, student_list):
        
        student_list[matric_number]["Department"] = new_update
        
        return student_list
    
    #this function deletes the student details in the student database txt
    def delete_student(matric_number, student_list):
        
        del student_list[matric_number]
        
        return student_list
           
                
        
        
