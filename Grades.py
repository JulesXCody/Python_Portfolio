#Make up last semesters grades
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#make up this semesters grades
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)

#Add computer science and that you got a 100 in it
gradebook.append(["computer science", 100])
print(gradebook)

#Add visual arts and that you got a 93 in it
gradebook.append(["visual arts", 93])
print(gradebook)

#You made a mistake add 5 points to visual arts grade
gradebook[-1][-1] = 98
print(gradebook)

#Remove your grade for Poetry
gradebook[2].remove(85)
print(gradebook)

#Add pass to your grade in Poetry
gradebook[2].append("Pass")
print(gradebook)

#What was your grades for last semester and this semester in one gradebook called "full_gradebook"
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
