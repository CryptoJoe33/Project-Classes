class Facility:

    def __init__(self):
        self.labs_name = "None"

    def addFacility(self):
        self.new_file = open("facilities.txt", "r")
        self.labs_list = self.new_file.readlines()
        self.new_file.close()

        self.labs_name = input("Enter Facility name: \n\n")

        self.labs_list.append(self.labs_name)

        self.writeListOffacilitiesToFile(self.labs_list)

    def displayFacilities(self):
        self.new_file = open("facilities.txt", "r")
        self.labs_list = self.new_file.readlines()
        self.new_file.close()
        self.labs_list[0] = "The " + self.labs_list[0]

        for i in range(len(self.labs_list)):
            if self.labs_list[i].endswith('\n') == False:
                print(self.labs_list[i]+'\n')
            else:
                print(self.labs_list[i])

    def writeListOffacilitiesToFile(self, write):
        self.new_file = open("facilities.txt", "w")
        self.index = 0

        for entries in write:
            if write[self.index].endswith('\n') == False:
                write[self.index] = write[self.index] + '\n'
            self.new_file.write(write[self.index])
            self.index += 1
        self.new_file.close()

class Laboratory:

    def __init__(self):
        self.lab_name = "None"
        self.cost = "None"

    def formatLabInfo(self):
        return str(self.lab_name) + '_' + str(self.cost)
    
    def addLaboratory(self):
        self.new_file = open("laboritories.txt", "r")
        self.labs_list = self.new_file.readlines()
        self.new_file.close()

        self.labs_name = input("Enter Facility name: \n")

        self.labs_list.append(self.labs_name)

        self.writeListOfLabsToFile(self.labs_list)

    def displayLabs(self):
        self.new_file = open("laboritories.txt", "r")
        self.labs_list = self.new_file.readlines()
        self.new_file.close()
        self.labs_list[0] = "The " + self.labs_list[0]

        for i in range(len(self.labs_list)):
            if self.labs_list[i].endswith('\n') == False:
                print(self.labs_list[i]+'\n')
            else:
                print(self.labs_list[i])

    def readLabsFile(self):
        self.new_file = open("laboritories.txt", "r")
        self.test_list = self.new_file.readlines()
        self.new_file.close()
        return self.test_list

    def enterLabInfo(self):
        self.lab_name = input("Enter the doctor's ID:\n\n")
        self.cost = input("Enter the doctor's name:\n\n")
        return [self.id,self.name,self.spec,self.hours,self.qual,self.room]

    def writeListOfLabsToFile(self,write):
        self.new_file = open("laboritories.txt", "w")
        self.index = 0

        for entries in write:
            if write[self.index].endswith('\n') == False:
                write[self.index] = write[self.index] + '\n'
            self.new_file.write(write[self.index])
            self.index += 1
        self.new_file.close()

Doctor = 0
Patient = 0

class Menu:
    
    def Display_Menu(self):
        self.repeat = True
        while self.repeat:
            self.option = input('Welcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 0 to stop:\n1 - 	Doctors\n2 - 	Facilities\n3 - 	Laboratories\n4 - 	Patients\n\n')
            
            if int(self.option) == 1:
                self.cycle = True
                self.obj_handle = Doctor()
                while self.cycle:
                    self.option = input('\nDoctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n\n')
                    if int(self.option) == 1:
                        self.obj_handle.displayDoctorsList()
                        print("\nBack to the prevoius Menu") 
                    elif int(self.option) == 2:
                        self.obj_handle.searchDoctorById()
                        print("\nBack to the prevoius Menu") 
                    elif int(self.option) == 3:
                        self.obj_handle.searchDoctorByName()
                        print("\nBack to the prevoius Menu")
                    elif int(self.option) == 4:
                        self.obj_handle.addDrToFile()
                        print("\nBack to the prevoius Menu")
                    elif int(self.option) == 5:
                        self.obj_handle.editDoctorInfo()
                        print("\nBack to the prevoius Menu")
                    elif int(self.option) == 6:
                        self.cycle = False
                        print("")

            elif int(self.option) == 2:
                self.cycle = True
                self.obj_handle = Facility()
                while self.cycle:
                    self.option = input('Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n\n')
                    if int(self.option) == 1:
                        self.obj_handle.displayFacilities()
                        print("Back to the prevoius Menu") 
                    elif int(self.option) == 2:
                        self.obj_handle.addFacility()
                        print("\nBack to the prevoius Menu") 
                    elif int(self.option) == 3:
                        self.cycle = False
                        print("")
            
                    else:
                        self.repeat = False   

            elif int(self.option) == 3:
                self.cycle = True
                self.obj_handle = Laboratory()
                while self.cycle:
                    self.option = input('Laboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n\n')
                    if int(self.option) == 1:
                        self.obj_handle.displayLabs()
                    elif int(self.option) == 2:
                        self.obj_handle.addLaboratory()
                    elif int(self.option) == 3:
                        self.cycle = False
                    print("Back to the prevoius Menu\n") 
            
            elif int(self.option) == 4:
                self.cycle = True
                self.obj_handle = Patient()
                while self.cycle:
                    self.option = input('Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n\n')
                    if int(self.option) == 1:
                        self.obj_handle.displayPatientsList()
                    elif int(self.option) == 2:
                        self.obj_handle.searchPatientById()
                    elif int(self.option) == 3:
                        self.obj_handle.addPatientToFile()
                    elif int(self.option) == 4:
                        self.obj_handle.editPatientInfo()
                    elif int(self.option) == 5:
                        self.cycle = False
                    print("Back to the prevoius Menu\n")  
        

run_obj = Menu()
run_obj.Display_Menu()

# Clears the file from any existing data so you can put more in

####################################################################################

