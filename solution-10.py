with open("moby-dick.txt", "r") as f:
  for l in f.read().split("\n")[1::2]:
    print(l)   