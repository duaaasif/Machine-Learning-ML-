class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.grade={}
    
    def addmarks(self,subj,marks):
        self.grade[subj]=marks
    
    def calc_avg(self):
        sumval= sum(self.grade.values())
        avg=sumval/ len(self.grade)
        return avg
        
    def assign_grade(self) :
        avg=self.calc_avg()
        if avg>=80 :
            return("GRADE A ")
        elif (avg>=60) and (avg<=79):
            return("GRADE B ")
        elif (avg>=40) and (avg<=59):
            return("GRADE C ")
        else :
            return("GRADE F ")
        
    def apply_bonus(self, user_input):
        bonus_func = lambda marks: {
            subject: (score + 5 if score <= 95 else 100)
            for subject, score in marks.items()
        }
        if user_input.strip().lower() == "yes":
            self.grade = bonus_func(self.grade)
        
    def create_report(self) :
        report ="STUDENT REPORT CARD"
        report+=f"Name: {self.name}\n"
        report += f"Age: {self.age}\n"
        report += "SUBJECT SCORES:\n"
        for subject, score in self.grade.items():
            report += f"{subject}: {score}\n"
        avg = self.calc_avg()
        report += f"Average: {avg:.2f}\n"
        report += f"Grade: {self.assign_grade()}\n"
        return report
    def store_to_file(self):
        with open('result.txt','w') as f:
            f.write(self.create_report())
            
    @staticmethod
    def read_file():
        with open('result.txt','r') as f:
            df=f.read()
            print(df)
Name = input("ENTER THE NAME OF THE STUDENT: ")
Age = input("ENTER THE AGE OF THE STUDENT: ")
m1= float(input("Enter marks (maths): "))
m2= float(input("Enter marks (urdu): "))
m3= float(input("Enter marks (english): "))
apply=input("DO YOU WANT TO GIVE BONUS IN EVERY SUBJECT ? ").strip().lower()
student1=student(Name,Age)
student1.addmarks("Maths",m1)
student1.addmarks("Urdu",m2)
student1.addmarks("English",m3)
student1.apply_bonus(apply)
student1.create_report()
student1.store_to_file()
student1.read_file()