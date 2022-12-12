# NAME: Oladunni Opaleye 
# Program Purpose: This program uses PYTHON SETS to display PVCC
#       REQUIRED courses & TECHNICAL ELECTIVE courses for:
#       --CSC certificate in Computer & Network Support Technologies:
#               ---required courses 
#               ---plus 3 technical electives 
#       --AAS degree in Information Technology:
#               ---required courses 
#               ---plus 4 technical electives 

# create sets for CERTIFICATE, Computer & Network Support Technologies 
network_req = {'CSC 110', 'ETR 164', 'ITN 101',}

network_elect = {'CSC 201', 'CSC 202', 'CSC 205', 
        'ETR 113', 'ETR 149', 'ETR 203', 'ETR 290', 
        'ITN 106', 'ITN 120', 'ITN 151', 'ITN 170', 'ITN 260', 'ITN 290', 
        'ITP 120', 'ITP 132', 'ITP 200', 'ITP 220', 'ITP 290', 
        'MTH 131', 'MTH 161', 'MTH 162', 'MTH 263', }

#create sets for ASSOCIATE degree, Information Technology degree:
info_req = { 'CSC 110',  'ENG 111',  'ENG 112',  'ETR 149',  'ETR 164',  'ITD 110',
                 'ITD 132',  'ITE 182',  'ITE 215',  'ITN 101',  'ITN 106',  'ITN 111',
                 'ITP 120',  'MTH 131',}

info_elect ={'ITN 170', 'ITN 208', 'ITN 260', 'ITN 261',
                       'ITN 276', 'ITN 277', 'ITP 132', 'ITP 136', 'ITP 150', 'ITP 220',}

dash_line = "------------------------------------------------------"
filename = "pvcc.txt"
global out

def main():
        global out
        out = open(filename, "w")
        out.write("\n**********PIEDMONT     VIRGINIA COMMUNITY COLLEGE**********")
        process_network_courses()
        display_network_courses()
        
        process_info_courses()
        display_info_courses()
        
        process_courses_in_both()
        out.close()
        print("To see results open file: "+ filename)
    

def process_network_courses():
        global network_elect #this set must be global sine it is CHANGED in this function 
        global num_net_req, num_net_elect, tot_net, all_net_courses
        temp_set = set() #create a temporary set empty set
        
        for course in network_elect:
                asterisk_course = "*" + course #insert an asterisk in front of ELECTIVE course name
                temp_set.add(asterisk_course)   #then add the new course name to a temporart set
                
        network_elect.clear() #remove all courses from set of electivecourses 
        network_elect = temp_set.copy() #COPY all the courses from the temporary set back into the elective set 
        
        num_net_req = len(network_req)
        num_net_elect = len(network_elect)
        tot_net = num_net_req + num_net_elect
        all_net_courses = network_req.union(network_elect) #UNION: create a new set with ALL network courses 
        
def display_network_courses():
        global out
        print("\nCERTIFICATE: Computer & Network Support Technologies")
        print(dash_line)
        print("Number of required courses       : " + str(num_net_req))
        print("Number of elective courses       : " + str(num_net_elect))
        print("Total number of Cert. courses: " + str(tot_net))
        print(dash_line)
        print("All Certificate courses: ")
        num = 1 
        for course in all_net_courses: #Display 5 courses per line
                print(course, end = " ")
                num += 1
                if num % 5 == 0:
                        print()
        print("\nNOTES:")
        print(" *Asterisk indicates ELECTIVE course")
        print(" Students chose 3 technical elective courses")
        print(dash_line)
        
def process_info_courses():
    # add code for processing inf course here 
        global info_elect #this set must be global sine it is CHANGED in this function 
        global num_info_req, num_info_elect, tot_info, all_info_courses
        temp_set = set() #create a temporary set empty set
        
        for course in info_elect:
                asterisk_course = "*" + course #insert an asterisk in front of ELECTIVE course name
                temp_set.add(asterisk_course)   #then add the new course name to a temporart set
                
        info_elect.clear() #remove all courses from set of electivecourses 
        info_elect = temp_set.copy() #COPY all the courses from the temporary set back into the elective set 
        
        num_info_req = len(info_req)
        num_info_elect = len(info_elect)
        tot_info = num_info_req + num_info_elect
        all_info_courses = info_req.union(info_elect) #UNION: create a new set with ALL info courses 
        
def display_info_courses():
        #student: add code for printing info course here 
        print("\n ")
        print("\nCERTIFICATE: Information Technology")
        print(dash_line)
        print("Number of required courses       : " + str(num_info_req))
        print("Number of elective courses       : " + str(num_info_elect))
        print("Total number of Cert. courses: " + str(tot_net))
        print(dash_line)
        print("All Certificate courses: ")
        num = 1 
        for course in all_info_courses: #Display 5 courses per line
                print(course, end = " ")
                num += 1
                if num % 5 == 0:
                        print()
        print("\nNOTES:")
        print(" *Asterisk indicates ELECTIVE course")
        print(" Students chose 4 technical elective courses")
        print(dash_line)
def process_courses_in_both():
    both_req = network_req.intersection(info_req)
    print(dash_line)
    print ("REQUIRED courses in both programs")
    num = 1
    for course in both_req: #Display 5 courses per line 
        print(course, end = " ")
        num += 1 
        if num % 5 == 0:
            print()
        #student: add code for electives in both courses here 
        
main()
