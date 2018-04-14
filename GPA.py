#Date: 2018.Apr.13
#Author: Yu-Sin Lin
#Convert hundred-point grade system to GPA system
#Version: 1.1

import sys

#read file
if len(sys.argv) < 2:
	print "Lack of argument, please add filename"
	sys.exit()

#check correctness of filename
filename = sys.argv[1]
try:
	f = open(filename,'r')
except IOError:
	print "cannot open %s, please check filename." % (sys.argv[1])

#read file and store no.credits and scores
credits = []
grades = []
for i, line in enumerate(f):
	try:
		credit, grade = line.split(',')
	except:
		print "An incorrect format in line %d in %s" %(i+1, filename)
		sys.exit()
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

print "The GPA is %f, AVG is %f" % (GPA, AVG_hundred)

