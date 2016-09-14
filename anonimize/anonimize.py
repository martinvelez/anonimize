import sys, re, os, time
from datetime import datetime

def replacer(match):
	s = match.group(0)
	if s.startswith('/'):
		return " "
	else:
		return s

def comment_remover(text):
	pattern = re.compile(r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"', re.DOTALL | re.MULTILINE)
	r1 = re.sub(pattern, replacer, text)
	return os.linesep.join([s for s in r1.splitlines() if s.strip()])

def write_anonymized_file(infile, outfile):
	try:
		root, ext = os.path.splitext(infile)
		valid = [".c", ".h", "Makefile"]
		if ext.lower() in valid:
			inf = open(infile, "r")
			dirty = inf.read()
			clean = comment_remover(dirty)
			inf.close()
			outf = open(outfile, "w") 
			outf.write(clean)
			outf.close()
			print("Comments are removed in following:", infile, ">>>", outfile) #and this
		else:
			print("File not valid:     ", infile)
	except UnicodeDecodeError:
		print("Can't remove comments in: ", infile)

def make_dir_for_anonymized_files(target_dir):
	timeStamp =  datetime.fromtimestamp(time.time()).strftime("%m-%d-%y-%H:%M:%S")
	new_dir = target_dir + "_" + timeStamp
	os.makedirs(new_dir)
	return new_dir

def anonimize(target_dir, in_place):
	if os.path.exists(target_dir):
		new_dir = ''
		if not in_place:
			new_dir = make_dir_for_anonymized_files(target_dir)
		for root, dirs, files in os.walk(target_dir):
			for file in files:
				infile = os.path.join(root, file)
				outfile = os.path.join(new_dir, file)
				if in_place:
					outfile = infile
				write_anonymized_file(infile, outfile)
	else:
		sys.exit("Directory {0} doesn't exist".format(target_dir))