class ram:
    def project(self):
        print("Online Shopping Management System")

class sam(ram):
    def project(self):
        super().project()
        print("Online Voting System")

class kumar(sam):
    def project(self):
        super().project()
        print("Car Rental System")

obj=kumar()
obj.project()

