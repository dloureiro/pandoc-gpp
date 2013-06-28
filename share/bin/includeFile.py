import sys
print '~~~'+sys.argv[1]
with open(sys.argv[2]) as f:
    print f.read()
print '~~~'