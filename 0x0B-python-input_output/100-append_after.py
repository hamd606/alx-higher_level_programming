#!/usr/bin/python3
''' inserts a line of text to a file, after each line containing a specific string '''


def append_after(filename="", search_string="", new_string=""):
	''' inserts line of txt to a file, after 1 line has a specific string '''
	read = []
	with open(filename, "r", encoding="utf-8") as f:
		read = f.readlines()
		i = 0

		while i < len(read):
			if search_string in read[i]:
				read[i:i + 1] = [read[i], new_string]
				i += 1
			i += 1

	with open(filename, "w", encoding="utf-8") as file:
		file.writelines(read)
