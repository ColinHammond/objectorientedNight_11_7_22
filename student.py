class Student:
    def __init__(self, name, number):
        self.name = name
        self.studentID = number
        self.class_taken = []

    def transfer_classes(selfself, other_classes):
        self.classes_taken.extend(other_classes)

    def can_graduate(self):
        if len(self.class_taken) > 40:
            return True
        else:
            return False