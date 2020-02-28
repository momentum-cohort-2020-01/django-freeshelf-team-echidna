import csv

with open('sample_books.csv', newline='\n') as csvfile:
    dial = csv.Sniffer().sniff(csvfile)
    print(dial)

