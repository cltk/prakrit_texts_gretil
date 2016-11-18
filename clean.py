import re

file_path = ""

file_name = ""

single_side_single_digit_regex = re.compile(r"[|][|][*][0-9][.][0-9][|][|]")
left_side_single_digit_regex = re.compile(r"[|][|][*][0-9][.][0-9][0-9][|][|]")
right_side_single_digit_regex = re.compile(r"[|][|][*][0-9][0-9][.][0-9][|][|]")
double_side_double_digit_regex = re.compile(r"[|][|][*][0-9][0-9][.][0-9][0-9][|][|]")

single_digit_only_each_regex = re.compile(r"[|][|][0-9][.][0-9][|][|]")
left_single_digit_only_each_regex = re.compile(r"[|][|][0-9][.][0-9][0-9][|][|]")
right_single_digit_only_each_regex = re.compile(r"[|][|][0-9][0-9][.][0-9][|][|]")
double_digit_only_each_regex = re.compile(r"[|][|][0-9][0-9][.][0-9][0-9][|][|]")

single_digit_regex = re.compile(r"[|][|][0-9][|][|]")
double_digit_regex = re.compile(r"[|][|][0-9][0-9][|][|]")

asterisk_double_regex = re.compile(r"[|][|][*][0-9][0-9][|][|]")
asterisk_single_regex = re.compile(r"[|][|][*][0-9][|][|]")

single_range_regex = re.compile(r"[|][|][0-9][-][0-9][|][|]")
double_range_regex = re.compile(r"[|][|][0-9][0-9][-][0-9][0-9][|][|]")
single_to_double_regex = re.compile(r"[|][|][0-9][-][0-9][0-9][|][|]")
double_to_single_regex = re.compile(r"[|][|][0-9][0-9][-][0-9][|][|]")

inp = open(file_path+file_name, "rw+")
inp_dat = inp.readlines()
inp.close()
out = open(file_path+file_name, "w+")
x=""
for line in inp_dat:
	if re.search(single_side_single_digit_regex, line):
		p = re.search(single_side_single_digit_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(left_side_single_digit_regex, line):
		p = re.search(left_side_single_digit_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(right_side_single_digit_regex, line):
		p = re.search(right_side_single_digit_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(double_side_double_digit_regex, line):
		p = re.search(double_side_double_digit_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(single_digit_only_each_regex, line):
		p = re.search(single_digit_only_each_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(left_single_digit_only_each_regex, line):
		p = re.search(left_single_digit_only_each_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(right_single_digit_only_each_regex, line):
		p = re.search(right_single_digit_only_each_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(double_digit_only_each_regex, line):
		p = re.search(double_digit_only_each_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(single_digit_regex, line):
		p = re.search(single_digit_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(double_digit_regex, line):
		p = re.search(double_digit_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(asterisk_single_regex, line):
		p = re.search(asterisk_single_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(asterisk_double_regex, line):
		p = re.search(asterisk_double_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(single_range_regex, line):
		p = re.search(single_range_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(double_range_regex, line):
		p = re.search(double_range_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(single_to_double_regex, line):
		p = re.search(single_to_double_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(double_to_single_regex, line):
		p = re.search(double_to_single_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	else:
		out.write(line)