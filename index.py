# importing libraries
import pathlib
import ast
from student_class import Students

def main():
    
     #find the path of the student database txt file
    path = pathlib.Path("C:/Users/User/OneDrive/Documents/Developer/Python/practice/Student_management_system/student_database.txt")

        #open and read the student database txt 
    with open(path, "r") as file:
        
            #read the student database txt as a string
            student_list_str = file.read() 
        
        #convert the student list string to a dictionary
    student_list = ast.literal_eval(student_list_str)
    
    #showing option to perform 
    print("what action do you want to perform?")
    print("1. Search for student")
    print("2. Add a new student")
    print("3. Update student details")
    print("4. Delete student details")
    choice = int(input("Enter an option: "))
       
    if choice == 1:
        
        #prompt for student matric number
        matric_number = input("Enter student matric number: ")
        
        #calling the search student function
        student = Students.search_student(student_list, matric_number)
        
        #print student infomation
        Students.print_student_info(student)
        
    elif choice == 2:
    
        #step 1 - ask for student details: first name, last name, phone number, matric number and email
        first_name = input("Enter student first name: ")
        last_name = input("Enter student last name: ")
        phone_number = input("Enter student phone number: ")
        matric_number = input("Enter student matric number: ")
        email = input("Enter student email: ")
        
        #step 2 - check if student already exist
        if matric_number in student_list:
            print("Student already exist")
            
        else:
        
            #step 3 - convert student details to a dictionary
            new_student = {
                "First Name":first_name,
                "Last Name": last_name,
                "Phone Number": phone_number,
                "Matric Number": matric_number,
                "Email" : email
            }
            
            #step 4 - get the student list dictionary
            
            #step 5- add new student details into the student list dictonary
            updated_student_list = Students.add_new_student(new_student, student_list) 
            
            #step 6 - print the new student list
            #print(updated_student_list)
            new_updated_student_list = str(updated_student_list)
            
            #step 7 - write the updated student list into the student database txt
            file = open(path, "w")
            file.write(new_updated_student_list)
        
        
            print("Student added successfully.")
    
    elif choice == 3:
        
        #prompt for student matric number
        matric_number = input("Enter student matric number: ")
        
        #check if matric number is in student list
        if matric_number not in  student_list:
            print("student not found")
            
        else:
        
            #prompt for the new update: department
            new_update = input("Enter student department: ")
            
            #add new update to the student list ditionary
            newest_update = Students.update_student(new_update, matric_number, student_list)
            
            #print the latest update
            #print(newest_update)
            latest_update = str(newest_update)
            
            #write the latest updated student list into the student database txt
            file = open(path, "w")
            file.write(latest_update)
            
            print("Student detail updated successfully.")
    
    elif choice == 4:
        
        #prompt for student matric number
        matric_number = input("Enter student matric number: ")
        
        #check if matric number is in student list
        if matric_number not in student_list:
            print("student not found")
            
        else:
        
            #delete student details
            new_delete = Students.delete_student(matric_number, student_list)
            
            #print the delete student
            #print(new_delete)
            newest_delete = str(new_delete)
            
            #write the newest delete of the student details into the student database txt
            file = open(path, "w")
            file.write(newest_delete)
            
            print("Successfully deleted student.")
            
    else:
        print("Invalid option")
            

    
                
    
            
    
           

        
       

        
        

        
        
        
        
main()