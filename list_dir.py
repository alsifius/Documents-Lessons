import os, glob
print(os.listdir('.'))
#files = [f for f in os.listdir('.') if os.path.isfile(f) and re.match("\*.edf", f)]
files = [f for f in glob.glob('*.edf')]
print(files)
for subjectID in files:
    g = subjectID[0:8]
    print (f"edf-anonymize.exe \'{subjectID}\' \'DeID/{subjectID}\' Mae Jemison %s" % g)

print("done")
#os.system('ls -l')
