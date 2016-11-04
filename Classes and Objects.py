class Student(object):
    """
    Holds information about a student

    attributes: firstName, lastName, studentID, email,
    """

student1 = Student()

student1.firstName = "John"
student1.lastName = "Smith"
student1.studentID = "0003456"
student1.email = "johnsmith@email.com"

student2 = Student()

student2.firstName = "Jane"
student2.lastName = "Parker"
student2.studentID = "0003564"
student2.email = "janeparker@email.com"

student3 = Student()

student3.firstName = "Robert"
student3.lastName = "Waite"
student3.studentID = "0003578"
student3.email = "robertwaite@email.com"

print '%s %s %s %s' % (student1.firstName,student1.lastName,student1.studentID,student1.email)

print '%s %s %s %s' % (student2.firstName,student2.lastName,student2.studentID,student2.email)

print '%s %s %s %s' % (student3.firstName,student3.lastName,student3.studentID,student3.email)
