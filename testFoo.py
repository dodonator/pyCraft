# coding: utf-8
import ast
def fileRead(dataname):
	file1 = open(dataname,"r")
	f1 = file1.read()
	file1.close()
	return f1

test = fileRead('mcL.logbuch')
for line in test:
	print line ,
	# print type(line)
	if line == ']':
		break
	
	
# erg = ast.literal_eval(test)
# print type(erg)
