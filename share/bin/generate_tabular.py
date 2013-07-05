import sys
import csv

# This script is meant for tabular tables without long lines
# # input
# 1 file
# 2 title
# # output
# the code to integrate

# data loading
csv_reader = csv.reader(open(sys.argv[1]), delimiter=";")

# computing column max sizes
max_col = []
for row in csv_reader :
    for i in range(0,len(row)) :
        if len(max_col) <= i : max_col.append(0)
        if len(row[i]) > max_col[i] : max_col[i]=len(row[i])

# first line of dashed
#print max_col
sys.stdout.write("+")
for i in range(0,len(max_col)-1):
    sys.stdout.write("-"*(max_col[i] + 2))
    sys.stdout.write("+")
sys.stdout.write("-"*(max_col[-1] + 2))
sys.stdout.write("+\n")

csv_reader = csv.reader(open(sys.argv[1]), delimiter=";")

line_index=0
for row in csv_reader :

    if line_index == 1 :

        sys.stdout.write("+")
        for i in range(0,len(max_col)-1):
            sys.stdout.write("="*(max_col[i] + 2))
            sys.stdout.write("+")
        sys.stdout.write("="*(max_col[-1] + 2))
        sys.stdout.write("+\n")

    for i in range(0,len(row)) :
        sys.stdout.write("| ")
        sys.stdout.write(row[i])
        sys.stdout.write(" "*(max_col[i]-len(row[i])))
        sys.stdout.write(" ")
    sys.stdout.write("|\n")

    if not line_index == 0 :
        sys.stdout.write("+")
        for i in range(0,len(max_col)-1):
            sys.stdout.write("-"*(max_col[i] + 2))
            sys.stdout.write("+")
        sys.stdout.write("-"*(max_col[-1] + 2))
        sys.stdout.write("+\n")


    line_index +=1
print ""
print " : " + sys.argv[2]