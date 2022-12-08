#from Classes import Doctor, Facility, Laboratory
class Doctor:

    def __init__(self, ID, n, s, w_t, q, r_n):
        self.ID = ID
        self.name = n
        self.specialization = s
        self.working_time = w_t
        self.qualification = q
        self.room_number = r_n

    def formatDrInfo(self):
        return str(self.ID) + '_' + self.name + '_' + self.specialization + '_' + str(self.working_time) + '_' + self.qualification + '_' + str(self.room_number)

    def addDrToFile(self, file):
        fid = open(file0, 'a')
        fid.write(self.formatDrInfo() + '\n')
        fid.close()

class Facility:

    def __init__(self, f):
        self.facility_name = f

    def formatFacilities(self):
        return self.facility_name + '\n'

    def addFacilityToFile(self, file):
        fid2 = open(file, 'a')
        fid2.write(self.formatFacilities() + '\n')
        fid2.close()

    def displayFacilities(self, file):
        fid2 = open(file, 'r')
        facilitiesAsString = fid2.readline()
        listInfo = facilitiesAsString.split('_')
        for n in listInfo:
            print(n)
        fid2.close()

class Laboratory:

    def __init__(self, l_n, c):
        self.lab_name = l_n
        self.cost = c

    def formatLabInfo(self):
        return str(self.lab_name) + '_' + str(self.cost)
    
    def addLabToFile(self, file):
        fid3 = open(file, 'a')
        fid3.write(self.formatLabInfo() + '\n')
        fid3.close()

    def displayLabsList(self, file):
        fid3 = open(file3, 'r')
        labsAsString = fid3.readline()
        listInfo = labsAsString.split(' ')
        for n in listInfo:
            print(n)
        fid3.close()

class Patient:

    def __init__(self, pid, n, d, g, a):
        self.pid = pid
        self.name = n
        self.disease = d
        self.gender = g
        self.age = a

    def formatPatientInfo(self):
        return str(self.pid) + '_' + self.name + '_' + self.disease + '_' + self.gender + '_' + str(self.age)
    
    def addPatientToFile(self, file):
        fid4 = open(file, 'a')
        fid4.write(self.formatPatientInfo() + '\n')
        fid4.close()

# Function will not work because there is nothing being written to the file
    def displayPatientInfro(self, file):
        fid4 = open(file, 'r')
        patientAsString = fid4.readline()
        listInfo = patientAsString.split('_')
        for n in listInfo:
            print(n)
        fid4.close()

class Management:

    def __init__(self):
        return self

    def writeListOfDoctorsToFile(self):
        fid = open('Doctors.txt', 'a')
        for doctors in theDoctors:
            doctors.addDrToFile(file0)
        fid.close()

    def writeListOfFacilitiesToFile(self):
        fid2 = open('Facilities.txt', 'a')
        for facilities in theFacilities:
            facilities.addFacilityToFile(file2)
        fid2.close()
    
    def writeListOfLabsToFile(self):
        fid3 = open('Laboratory.txt', 'a')
        for laboratories in theLabs:
            laboratories.addLabToFile(file3)
        fid3.close()

    def writeListOfPatientsToFile(self):
        fid4 = open('Patients.txt','a')
        for patients in thePatients:
            patients.addPatientToFile(file4)
        fid4.close()

# Clears the file from any existing data so you can put more in
file0 = "Doctor.txt"
fid = open(file0, 'w')
fid.close()

# Initalizes theDoctors variable for the functions to use
theDoctors = [Doctor(369, 'Joey', 'Penis', '8:00-8:00', 'Harvard', 69), Doctor(370, 'Janet', 'Butthole', '9:00-9:00', 'Oxford', 70)]

# Clears the file from any existing data so you can put more in
file2 = "Facilities.txt"
fid2 = open(file2, 'w')
fid2.close()

# Initalizes theFacilities variable for the functions to use
theFacilities = [Facility('Hospital '), Facility('Emergency '), Facility('Penis '), Facility('Operating_Room')]


# Clears the file from any existing data so you can put more in
file3 = "Labs.txt"
fid3 = open(file3, 'w')
fid3.close()

# Initalizes theLabs variable for the function
theLabs = [Laboratory('Lab1', 800), Laboratory('Lab2', 1200)]

file4 = "Patients.txt"
fid4 = open(file4, 'w')
fid4.close()

thePatients = [Patient(69, 'Dick', 'Cancer', 'man', 75), Patient(96, 'Jon', 'Cancer', 'man', 45)]

<<<<<<< HEAD
Management.writeListOfPatientsToFile(file4)
=======
>>>>>>> parent of 199befc (Writing to file)
