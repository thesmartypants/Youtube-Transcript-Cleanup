file = input("file name: ")

f = open(file, "r")
lines = f.readlines()
f.close()
clean_lines = []
prev_line = ""
for line in lines:
  try:
    if 0 <= int(line[0]) <= 9:
      prev_line = line
      continue
  except:
    if prev_line == "\n" or line == "\n":
      prev_line = line
      continue
    clean_lines.append(line)
  prev_line = line

  clean_lines = [line.replace("\n", "") for line in clean_lines]

clean_lines = " ".join(clean_lines)
f = open("1" + file, "w")
f.write(clean_lines)
f.close()
print(clean_lines)
