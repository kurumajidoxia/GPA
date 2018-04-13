#Date: 2018.Apr.13
#Author: Yu-Sin Lin
#Convert hundred-point grade system to GPA system
#Version: 1.0

import sys

#read file
if len(sys.argv) < 2:
	print "Lack of argument"
	sys.exit()

#read file to get credits and grades
credits = []
grades = []
f = open(sys.argv[1],'r')
for line in f:
	credit, grade = line.split(',')
	credit = credit.strip()
	grade = grade.strip()
	credits.append(credit)
	grades.append(grade)

f.close()

#convert to gpa and convert grades from string to int
gpa = []
sum_grade = 0
for i, g in enumerate(grades):
	g = int(g)
	grades[i] = g
	if g >= 90:
		gpa.append(4.3)
	elif g >= 85:
		gpa.append(4.0)
	elif g >= 80:
		gpa.append(3.7)
	elif g >= 77:
		gpa.append(3.3)
	elif g >= 73:
		gpa.append(3.0)
	elif g >= 70:
		gpa.append(2.7)
	elif g >= 67:
		gpa.append(2.3)
	elif g >= 63:
		gpa.append(2)
	elif g >= 60:
		gpa.append(1.7)
	else:
		gpa.append(0.0)

#caluclate GPA
weightedGPA = 0
weightedGrade = 0
total_credit = 0
for i, c in enumerate(credits):
	c = int(c)
	weightedGPA += c*gpa[i]
	weightedGrade += c*grades[i]
	total_credit += c
GPA = weightedGPA/total_credit
AVG_hundred = weightedGrade/float(total_credit)

print "Your GPA is %f, AVG is %f" % (GPA, AVG_hundred)

