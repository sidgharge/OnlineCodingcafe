import subprocess
import sys
import os
from subprocess import STDOUT,PIPE

def compile_java(java_file):
	cmd = 'javac ' + java_file 
	proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = proc.communicate()
	print(out)
	print(err)
 
compile_java(sys.argv[1])