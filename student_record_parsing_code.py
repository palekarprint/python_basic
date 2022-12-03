math_marks_A = []
for line in open("D:\Palekar sir data\Python Workshop, Mumbai\Parsing Data\student_record.txt"):
	fields = line.split(";")
	region_code = fields[0]
	region_code_stripped = region_code.strip()
	math_mark_str = fields[1]
	math_mark = float(math_mark_str)
	if region_code == "A":
		math_marks_A.append(math_mark)
math_marks_mean = sum(math_marks_A)/len(math_marks_A)
print(math_marks_mean)