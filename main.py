from entity.model import Students,Courses,Teachers,Enrollment,Payments
from dao.db_interaction import DBInteraction
class MainModule:
    def __init__(self):
        self.db_interaction = DBInteraction()
    def run(self):
        while True:
            print("Student Information Menu")
            print("1. Create Student")
            print("2. Create Course")
            print("3. Create Enrollmet")
            print("4. Create Payments")
            print("5. Create Teachers")
            print("6. Update Student")
            print("7. Update Course")
            print("8. Update Enrollment")
            print("9. Update Payments")
            print("10. Update Teachers")
            print("11. Get Student by id")
            print("12. Get Course by Student id")
            print("13. Get Enrollment by Student id")
            print("14. Get Enrollment by Course id")
            print("15. Get Payment details by Student id")
            print("16. Get Teacher information by Teacher id")
            print("17. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.db_interaction.create_student()

            if choice =="2":
                self.db_interaction.create_course()

            if choice == "3":
                self.db_interaction.create_enrollment()

            if choice =="4":
                self.db_interaction.create_payment()

            if choice =="5":
                self.db_interaction.create_teacher()

            if choice =="6":
                self.db_interaction.update_student()

            if choice == "7":
                self.db_interaction.update_course()

            if choice =="8":
                self.db_interaction.update_enrollment()

            if choice == "9":
                self.db_interaction.update_payments()

            if choice =="10":
                self.db_interaction.update_teacher()

            if choice == "11":
                self.db_interaction.get_student_by_id()

            if choice =="12":
                self.db_interaction.get_course_by_id()

            if choice == "13":
                self.db_interaction.get_enrollments_for_student()

            if choice == "14":
                self.db_interaction.get_enrollments_for_course()

            if choice == "15":
                self.db_interaction.get_payments_for_student()

            if choice == "16":
                self.db_interaction.get_teacher_by_id()

            if choice =="17":
                print("Thanks for using the Student Information System Assignment")
                break






if __name__ == "__main__":
    main_module = MainModule()
    main_module.run()
