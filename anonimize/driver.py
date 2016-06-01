from __future__ import print_function
import sys, re, os, time
#import anonimize.anonimize.NoComment
from anonimize import NoComment
from datetime import datetime

if __name__ == "__main__": #I'm not 100% sure what this means but apparently this is how you do it
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
                sys.exit('Directory does not exist')
