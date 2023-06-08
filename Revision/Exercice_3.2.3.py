#Exercices 3

#3.2.3 :
note = int(input("What note have you? /100 : "))
def gradeMyNote(note):
    if (note >= 80):
       print("Grade : A")
    elif (note >= 60 and note < 80):
       print("Grade : B")
    elif (note >= 50 and note < 60):
       print("Grade : C")
    elif (note >= 40 and note < 50):
       print("Grade : D")
    else:
       print("Grade : E")


gradeMyNote(note)