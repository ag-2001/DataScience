##analyzing SAT data
import school_scores
list_of_record = school_scores.get_all()



#for i in range(len(list_of_record)):
    #print(list_of_record[i]['Academic Subjects']["English"]['Average GPA'])
for GPA in list_of_record:
        englishGPA = GPA['Academic Subjects']['English']['Average GPA']
        print(englishGPA)
