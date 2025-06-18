
def avg (marks) :
    return sum(marks.values())/len(marks)

def grade(avg) :
    if avg>=80 :
        return("GRADE A ")
    elif (avg>=60) and (avg<=79):
        return("GRADE B ")
    elif (avg>=40) and (avg<=59):
        return("GRADE C ")
    else :
        return("GRADE F ")

bonus_inp = input("DO YOU WANT TO GIVE BONUS IN EVERY SUBJECT ? ").strip().lower()
bonus = lambda marks : {subject: score + 5 for subject , score in marks.items()} if bonus_inp=="yes" else marks

name = input("ENTER THE NAME OF THE STUDENT: ")
age = input("ENTER THE AGE OF THE STUDENT: ")
marks = {"MATHS" : float(input("Enter marks (maths): ")) , "URDU" : float(input("Enter marks (urdu) : ")) , "ENGLISH" : float(input("Enter marks (english) : "))}

marks= bonus(marks)
average = avg(marks)
assign_grade = grade (average)
def create_report(name,age,marks,average,assign_grade) :
    with open("report1.txt", 'w') as file:
        file.write("\t\tSTUDENT REPORT CARD\n\n")
        file.write(f"Name: { name }\n")
        file.write(f"Age: { age }\n")
        file.write("SUBJECT SCORES\n")
        for subject, score in marks.items():
            file.write(f"{subject}:{score}\n")
        file.write(f"Average: {average:.2f}\n")
        file.write(f"Grade: {assign_grade}\n")
create_report(name,age,marks,average,assign_grade)
print("REPORT CARD GENERATED SUCCESSFULLY")
with open("report1.txt",'r') as file:
    print(file.read())
