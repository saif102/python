grade = 76

if grade>= 95:
    letterGrade = "1,0 (sehr gut / excellent)"
elif grade>= 90:
    letterGrade = "1,3 (sehr gut / excellent)"
elif grade>= 85:
    letterGrade = "1,7 (gut / good)"
elif grade>= 80:
    letterGrade = "2,0 (gut / good)"
elif grade>= 75:
    letterGrade = "2,3 (gut / good)"
elif grade>= 70:
    letterGrade = "2,7 (befriedigend / satisfactory)"
elif grade>= 65:
    letterGrade = "3,0 (befriedigend / satisfactory)"
elif grade>= 60:
    letterGrade = "3,3 (befriedigend / satisfactory)"
elif grade>= 55:
    letterGrade = "3,7 (ausreichend / sufficient)"
elif grade>= 50:
    letterGrade = "4,0 (ausreichend / sufficient)"
else:
    letterGrade = "5,0 (nicht bestanden / failed)"

print (letterGrade)
