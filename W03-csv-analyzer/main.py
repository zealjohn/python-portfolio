import csv
with open("students.csv", "r", encoding="utf-8") as file:
  reader = csv.DictReader(file)
  students = list(reader)

for s in students:
  chinese = int(s["chinese"])
  english = int(s["english"])
  math = int(s["math"])
  average = (chinese + english + math) / 3
  print(s["name"], average)
