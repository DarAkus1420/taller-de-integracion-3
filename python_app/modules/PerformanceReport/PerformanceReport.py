import csv

f = open('test.csv', 'w')
writer = csv.writer(f)
writer.writerow(["SN", "Name", "Contribution"])
writer.writerow((1, "Linus Torvalds", "Linux Kernel"))
writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
writer.writerow([3, "Guido van Rossum", "Python Programming"])
