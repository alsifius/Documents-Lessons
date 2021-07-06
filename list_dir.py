import os
print(os.listdir('.'))
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for subjecID in files:
    g = subjecID[0:8]
    print (f"edf-anonymize.exe {g}.edf DeID/{g}.edf Mae Jemison %s" % g)
