shekveta = ["ყავა", "ჩაი", "ყავა", "წვენი", "ჩაი", "ყავა", "წყალი"]

special = []
for i in shekveta:
    if i not in special:
        special.append(i)

frequencies = [(i, shekveta.count(i)) for i in special]

popular = None
max_count = 0

for i, count in frequencies:
    if count > max_count:
        max_count = count
        popular = i

bolo3 = shekveta[:-4:-1]

print(f"უნიკალური: {special}")
print(f"სიხშირე: {frequencies}")
print(f"ყველაზე პოპულარული: {popular} ({max_count}-ჯერ)")
print(f"ბოლო 3 შეკვეთა: {bolo3}")