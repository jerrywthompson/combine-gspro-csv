/*

# Read the contents of the first CSV file
with open("file1.csv", "r") as file1:
    reader1 = csv.reader(file1)
    rows1 = [row for row in reader1]

# Read the contents of the second CSV file
with open("file2.csv", "r") as file2:
    reader2 = csv.reader(file2)
    rows2 = [row for row in reader2]

# Combine the data from both files
rows = rows1 + rows2

# Write the resulting data to a new CSV file
with open("result.csv", "w") as result:
    writer = csv.writer(result)
    writer.writerows(rows)

*/