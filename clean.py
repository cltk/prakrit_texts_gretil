import re

file_path = ""

file_name = ".txt"

single_side_single_digit_regex = re.compile(r"[|][|][*][0-9][.][0-9][|][|]")
left_side_single_digit_regex = re.compile(r"[|][|][*][0-9][.][0-9][0-9][|][|]")
right_side_single_digit_regex = re.compile(r"[|][|][*][0-9][0-9][.][0-9][|][|]")
double_side_double_digit_regex = re.compile(r"[|][|][*][0-9][0-9][.][0-9][0-9][|][|]")
triple_left_double_right_regex = re.compile(r"[|][|][*][0-9][0-9][0-9][.][0-9][0-9][|][|]")
triple_left_single_right_regex = re.compile(r"[|][|][*][0-9][0-9][0-9][.][0-9][|][|]")

single_digit_only_each_regex = re.compile(r"[|][|][0-9][.][0-9][|][|]")
left_single_digit_only_each_regex = re.compile(r"[|][|][0-9][.][0-9][0-9][|][|]")
right_single_digit_only_each_regex = re.compile(r"[|][|][0-9][0-9][.][0-9][|][|]")
double_digit_only_each_regex = re.compile(r"[|][|][0-9][0-9][.][0-9][0-9][|][|]")

single_digit_regex = re.compile(r"[|][|][0-9][|][|]")
double_digit_regex = re.compile(r"[|][|][0-9][0-9][|][|]")
triple_digit_regex = re.compile(r"[|][|][0-9][0-9][0-9][|][|]")

asterisk_double_regex = re.compile(r"[|][|][*][0-9][0-9][|][|]")
asterisk_single_regex = re.compile(r"[|][|][*][0-9][|][|]")

single_range_regex = re.compile(r"[|][|][0-9][-][0-9][|][|]")
double_range_regex = re.compile(r"[|][|][0-9][0-9][-][0-9][0-9][|][|]")
single_to_double_regex = re.compile(r"[|][|][0-9][-][0-9][0-9][|][|]")
double_to_single_regex = re.compile(r"[|][|][0-9][0-9][-][0-9][|][|]")

hadhut_single_regex = re.compile(r"[/][/][ ][H][a][D][h][_][0-9][.][0-9][ ][/][/]")
hadhut_double_regex = re.compile(r"[/][/][ ][H][a][D][h][_][0-9][.][0-9][0-9][ ][/][/]")
hadhut_triple_regex = re.compile(r"[/][/][ ][H][a][D][h][_][0-9][.][0-9][0-9][0-9][ ][/][/]")

halsatsu_single_regex = re.compile(r"[ ][H][S][S][_][0-9][a-d][a-d]")
halsatsu_double_regex = re.compile(r"[ ][H][S][S][_][0-9][0-9][a-d][a-d]")
halsatsu_triple_regex = re.compile(r"[ ][H][S][S][_][0-9][0-9][0-9][a-d][a-d]")
halsatsu_quadruple_regex = re.compile(r"[ ][H][S][S][_][0-9][0-9][0-9][0-9][a-d][a-d]")

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
	elif re.search(triple_digit_regex, line):
		p = re.search(triple_digit_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(triple_left_single_right_regex, line):
		p = re.search(triple_left_single_right_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(triple_left_double_right_regex, line):
		p = re.search(triple_left_double_right_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(hadhut_single_regex, line):
		p = re.search(hadhut_single_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(hadhut_double_regex, line):
		p = re.search(hadhut_double_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(hadhut_triple_regex, line):
		p = re.search(hadhut_triple_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(halsatsu_single_regex, line):
		p = re.search(halsatsu_single_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(halsatsu_double_regex, line):
		p = re.search(halsatsu_double_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(halsatsu_triple_regex, line):
		p = re.search(halsatsu_triple_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	elif re.search(halsatsu_quadruple_regex, line):
		p = re.search(halsatsu_quadruple_regex, line)
		x = line[:p.start()] + line[p.end():]
		print x
		out.write(x)
	else:
		out.write(line)