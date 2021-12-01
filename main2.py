x = input("Enter the adverbs using comas ")
y = input("Enter adjective using comas")

x2 = x.split(",")
y2 = y.split(",")

str = "An old man lived in the village. He was one of the most unfortunate people in the world. The whole village was tired of him; he was always gloomy, he constantly complained and was always in a bad mood."

q = str.replace('old', y2[0])
w = q.replace('unfortunate', y2[1])
e = w.replace('whole', y2[2])
r = e.replace('tired', y2[3])
t = r.replace('glommy', y2[4])
u = t.replace('bad', y2[5])

a = u.replace('most', x2[0])
s = a.replace('always', x2[1])
d = s.replace('constantly', x2[2])
f = d.replace('always', x2[3])

print(f)