

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
        """ Takes an applicant as a parameter and returns a boolean that indicates whether or not the applicant's 
                age is greater than 18.
                
        
            Returns:
                Bool: Indicates whether the applicant is greater than 18.
            
        """  
        if self.age >= 18:
            return True
        else:
            return False

    def is_active_applicant(self):
        """Takes an applicant as a parameter and returns
                a boolean that indicates whether or not the applicant's 
                program status is "Active
            
                Returns:
                    Bool: Indicates whether the applicant is active in the program.
            
        """
        if self.status == "Active":
            return True
        else:
            return False

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

class ApplicantTracker:
    def __init__(self, applicants):
        self.applicants = list(applicants)


    def filter_applicants_by_eligibility(self):
        """Returns a list of eligible applicants.
        """
        eligible_list = []
        for applicant in self.applicants:
            if applicant.is_eligble_applicant():
                eligible_list.append(applicant.name)
            else:
                pass
        return eligible_list

    def filter_active_applicants(self):
        """Returns a list of Applicant objects 
            currently in an "Active" status."""
        active_list = []
        for applicant in self.applicants:
            if applicant.is_active_applicant():
                active_list.append(applicant.name)
            else:
                pass
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
        return len(completed_list)

app_tracker_test = ApplicantTracker(applicant_fleet)

list_of_eligibles = app_tracker_test.filter_applicants_by_eligibility()
list_of_actives = app_tracker_test.filter_active_applicants()
number_of_completed = app_tracker_test.report_completed_applicants()
