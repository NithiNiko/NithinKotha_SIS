from entity.model import Students,Courses,Teachers,Enrollment,Payments
from dao.db_interaction import DBInteraction
class MainModule:
    def __init__(self):
        self.db_interaction = DBInteraction()
    def run(self):
        self.db_interaction.create_student()



if __name__ == "__main__":
    main_module = MainModule()
    main_module.run()