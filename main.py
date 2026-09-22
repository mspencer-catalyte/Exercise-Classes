

status = ['Applied', 'Accepted', 'Active', 'Completed', 'Dismissed', 'Rejected']

class Applicant:
    def __init__(self,name,age,address,street,city,state,zip,status):
        self.name = name
        self.age = age
        self.address = address
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.status = status

    def is_eligble_applicant(self): 
        """Returns a boolean indicating if the 
            applicant's age is greater than 18."""  
        if self.age >= 18:
            return True
        else:
            return False

    def is_active_applicant(self):
        """Returns a boolean indicating if the program_status is 
            exactly "Active"."""
        if self.status == "Active":
            return True
        else:
            return False

    def display_info(self):
        dis
        print(str(self.name)+ ", " + str(self.age)+ ", " + str(self.address)+ ", " +
              str(self.street)+ ", " + str(self.city)+ ", " + str(self.state)+ ", " +
              str(self.zip)+ ", " + str(self.p_status))

applicant_01 = Applicant("Abigail Fontane", 44, "123", "Gibby St","Havalina", "NY", "94949", status[2])
applicant_02 = Applicant("Bruce Lee", 52, "1343 ", "IDK Ave", "Greer", "MO", "96969",status[1])
applicant_03 = Applicant("Charlie Foster", 13, "3343 ", "Hall Ln", "Nantucket", "NC", "84549", status[5])
applicant_04 = Applicant("Dean Withers", 16, "984 ", "Pace Ave", "Franklin", "IL", "07552", status[5])
applicant_05 = Applicant("Esteban Zanzabar", 18, "777", "Luck St", "Foster", "NY", "20209", status[4])
applicant_06 = Applicant("Florence Machine", 19, "656", "Calumm Dr", "Newark", "DE", "08312", status[2])
applicant_07 = Applicant("Giana Ovaltine", 99, "7535", "Not Way", "Wheaton", "MD", "02265", status[2])
applicant_08 = Applicant("Rock T. Cazbah", 73, "244", "Heart St", "Kensington", "CA", "84521", status[3])
applicant_09 = Applicant("Imogen Heap", 21, "782", "Boop Pl", "Haplern", "FL", "59643", status[4])
applicant_10 = Applicant("Jackie Robinson", 32, "789", "Funt Dr", "Greenbelt", "GA", "12548", status[1])

applicant_fleet = [applicant_01,applicant_02,applicant_03,applicant_04,applicant_05,applicant_06,applicant_07,
              applicant_08,applicant_09,applicant_10]

if applicant_01.is_eligble_applicant:
    print(f"{applicant_01.name} is eligible.")
else:
    print(f"{applicant_01.name} is ineligible.")

if applicant_01.is_active_applicant:
    print(f"{applicant_01.name} is active.")
else:
    print(f"{applicant_01.name} is inactive.")

class ApplicantTracker:
    def __init__(self, applicants):
        self.applicants = list(applicants)


    def filter_applicants_by_eligibility(self):
        """ Prints and returns a list of only those Applicant objects that meet 
            the age requirement."""
        eligible_list = []
        for applicant in self.applicants:
            if applicant.is_eligble_applicant():
                eligible_list.append(applicant.name)
            else:
                pass
        #return eligible_list
        print("\nApplicants that are eligble for the program:")
        print(*eligible_list, sep=", ")
        return eligible_list

    def filter_active_applicants(self):
        """Prints and returns a list of Applicant objects 
            currently in an "Active" status."""
        active_list = []
        for applicant in self.applicants:
            if applicant.is_active_applicant():
                active_list.append(applicant.name)
            else:
                pass
        print("\nApplicants that are active in the program.")
        print(*active_list, sep=", ")
        return active_list

    def report_completed_applicants(self):
        """Returns the total count (integer) of 
            all applicants whose status is "Completed"."""
        completed_list = []
        for applicant in self.applicants:
            if applicant.status == "Completed":
                completed_list.append(applicant.name)
            else:
                pass
        print("\nApplicants that have completed the program.")
        print(len(completed_list), sep=", ")
        return len(completed_list)

app_tracker_test = ApplicantTracker(applicant_fleet)

app_tracker_test.filter_applicants_by_eligibility()
app_tracker_test.filter_active_applicants()
app_tracker_test.report_completed_applicants()