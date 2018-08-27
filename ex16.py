from sys import argv
#from os.path import exists

script,from_file,to_file = argv

#print ("Copying from %s to %s"%(from_file,to_file))

#一行完成代码，indata=open(from_file).read()
in_put = open(from_file)
indata = in_put.read()

#print ("The input file is %d bytes long "%len(indata))

#print ("Does the output file exists?%r"%exists(to_file))
#print ("Ready, hit RETURN to continue,CTRL-C to abort.")

#input()

#转一行 open(to_file,'w').write(indata)
output=open(to_file,'w')
output.write(indata)

#print ("Alright, all done")

#output.close()
#in_put.close()