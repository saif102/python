#print("Enter your points:")

x = float(input("Enter your points:"))

if x>= 95:
    letterGrade = "1,0 (sehr gut / excellent)"
elif x>= 90:
    letterGrade = "1,3 (sehr gut / excellent)"
elif x>= 85:
    letterGrade = "1,7 (gut / good)"
elif x>= 80:
    letterGrade = "2,0 (gut / good)"
elif x>= 75:
    letterGrade = "2,3 (gut / good)"
elif x>= 70:
    letterGrade = "2,7 (befriedigend / satisfactory)"
elif x>= 65:
    letterGrade = "3,0 (befriedigend / satisfactory)"
elif x>= 60:
    letterGrade = "3,3 (befriedigend / satisfactory)"
elif x>= 55:
    letterGrade = "3,7 (ausreichend / sufficient)"
elif x>= 50:
    letterGrade = "4,0 (ausreichend / sufficient)"
else:
    letterGrade = "5,0 (nicht bestanden / failed)"

if x>= 50:
    print ("Congratulations! Your result is: " + letterGrade + ".")
else:
    print (letterGrade + ". Sorry! Your point is not enough. Better luck next time.")

