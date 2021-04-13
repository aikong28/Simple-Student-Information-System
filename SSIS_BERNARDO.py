'''AIKO MARIELLE BERNARDO'''

import csv

StudAttributes = ['ID Number', 'Name', 'Course', 'Year Level', 'Gender']
SDatabase = 'LISTSTUDENTS.csv'

def main_menu():
    print("--------------------------------------------")
    print("      Simple Student Information System     ")
    print("--------------------------------------------")
    print("1. View Students")
    print("2. Add New Student")
    print("3. Edit Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Quit")

'''VIEW STUDENT'''
def ViewStudents():
    global StudAttributes
    global SDatabase
    
    print("---------------------")
    print("    Student List     ")
    print("---------------------")
    
    with open(SDatabase, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        for x in StudAttributes:
            print( x, end = "\n   ")
        print("\n----------------------------------------------------------")
        
        for row in reader:
            for item in row:
                print( item, end = "\n   ")
            print("\n")
            
    input("Press any key to continue: ")


'''ADD STUDENT'''
def AddStudent():
    print("---------------------")
    print("     Add Student     ")
    print("---------------------")
    
    global StudAttributes
    global SDatabase
    
    SData = []
    for field in StudAttributes:
        value = input("Enter " + field + ": ")
        SData.append(value)
        
    with open(SDatabase, "a", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([SData])
    
    print("Data saved successfully!")
    input("Press any key to continue: ")
    return


'''UPDATE STUDENT'''
def UpdateStudent():
    global StudAttributes
    global SDatabase
    
    print("------------------------")
    print("     Update Student     ")
    print("------------------------")
    
    IDnum = input("Enter ID Number of student to update: ")
    indexstud = None
    updatedData = []
    with open(SDatabase, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if IDnum == row[0]:
                    indexstud = counter
                    print("Student Found: at index ", indexstud)
                    SData = []
                    for field in StudAttributes:
                        value = input("Enter " + field + ": ")
                        SData.append(value)
                    updatedData.append(SData)
                else:
                    updatedData.append(row)
                counter += 1
                
    '''CHECK IF STUDENT IS/NOT FOUND'''
    if indexstud is not None:
        with open(SDatabase, "w", encoding = "utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updatedData)
            
            print("ID Number has been successfully updated")
    
    else:
        print("ID Number could not be found")
        
    input("Press any key to continue: ")
    
    
'''DELETE STUDENT'''
def DeleteStudent():
    global StudAttributes
    global SDatabase
    
    print("------------------------")
    print("     Remove student     ")
    print("------------------------")
    
    IDnum = input("Enter ID Number of student to remove: ")
    student_Found = False
    updated_data = []
    with open(SDatabase, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if IDnum != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_Found = True
    
    if student_Found is True:
        with open(SDatabase, "w", encoding = "utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("ID Number: ", IDnum, "has been removed successfully")
    
    else:
        print("Sorry but ID Number could not be found.")
    
    input("Press any key to continue: ")

    
'''SEARCH STUDENT BASED ON ID NUMBER'''
def SearchStudent():
    global StudAttributes
    global SDatabase
    
    print("------------------------")
    print("     Search Student     ")
    print("------------------------")
    
    IDnum = input("Enter ID Number to search: ")
    with open(SDatabase, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if IDnum == row[0]:
                    print("Student found!")
                    print("ID Number: ", row[0])
                    print("Name: ", row[1])
                    print("Course: ", row[2])
                    print("Year Level: ", row[3])
                    print("Course: ", row[4])
                    break
        
        else:
            print("Sorry but student does not exist.")
    input("Press any key to continue: ")




'''MAIN MENU'''
while True:
    main_menu()
    
    choice = input("Hello! Enter a number to start our productivity: ")
    if choice == '1':
        ViewStudents()
    elif choice == '2':
        AddStudent()
    elif choice == '3':
        UpdateStudent()
    elif choice == '4':
        DeleteStudent()
    elif choice == '5':
        SearchStudent()
    else:
        break



print("------------------------------------")
print("     System has been terminated     ")
print("------------------------------------")
