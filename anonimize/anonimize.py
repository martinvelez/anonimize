#can take a directory and remove all the comments in every file in that directory
from __future__ import print_function
import sys, re, os, time
from datetime import datetime

def replacer(match):
	s = match.group(0)
	if s.startswith('/'):
		return " " # note: a space and not an empty string
	else:
		return s


def comment_remover(text):
	pattern = re.compile(r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"', re.DOTALL | re.MULTILINE)
	r1 = re.sub(pattern, replacer, text)
	return os.linesep.join([s for s in r1.splitlines() if s.strip()])


def NoComment(infile, outfile):
	root, ext = os.path.splitext(infile) #I also googled this
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


'''if __name__ == "__main__": #I'm not 100% sure what this means but apparently this is how you do it
	if len(sys.argv) < 2:
		print("Oops, forgot to give it a directory name")
		sys.exit()
	root = sys.argv[1]
	if os.path.exists(root): 
		timeStamp =  datetime.fromtimestamp(time.time()).strftime("%m-%d-%y-%H:%M:%S")
		newdir = root + "_" + timeStamp
		os.makedirs(newdir)
		for root, folders, fns in os.walk(root):
			for fn in fns:
				infile = os.path.join(root, fn)
				outfile = os.path.join(newdir, fn)
				NoComment(infile, outfile)
	else:
		sys.exit('Directory does not exist')'''
