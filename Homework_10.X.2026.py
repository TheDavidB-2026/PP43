# 1. სიტყვების მთვლელი
# txt = "Python არის მარტივი, Python არის ძლიერი და Python პოპულარულია."
# lower = txt.lower()
#
# for i in ",.":
#     lower = lower.replace(i,"")
# words = lower.split()
#
# wrd_count = {}
# for w in words:
#     wrd_count[w] = wrd_count.get(w,0) + 1
#
# for w, c in wrd_count.items():
#     print(f"{w}: {c}")
#
# frequent = None
# max = 0
# for w, c in wrd_count.items():
#     if c > max:
#         max = c
#         frequent = w
#
# print(f"ყველაზე ხშირი: '{frequent}' ({max}-ჯერ)")
#
# print(f"სხვადასხვა სიტყვა: {len(wrd_count)}")

# 2. ონლაინ მაღაზიის შეკვეთები
# prices = {"ლეპტოპი": 2500, "მაუსი": 40, "კლავიატურა": 120, "მონიტორი": 650}
# marag = {"ლეპტოპი": 2, "მაუსი": 10, "კლავიატურა": 1, "მონიტორი": 3}
#
# orders = [
#     ("ნინო", "ლეპტოპი", 1),
#     ("გიორგი", "მაუსი", 3),
#     ("ანა", "კლავიატურა", 1),
#     ("ნინო", "მაუსი", 2),
#     ("გიორგი", "კლავიატურა", 1),
#     ("ანა", "ტელეფონი", 1),
#     ("ლუკა", "ლეპტოპი", 1),
#     ("ლუკა", "მონიტორი", 5),
# ]
#
# expenses = {}
# failed = set()
# total = 0
#
# for customer, product, quantity in orders:
#     if product not in prices:
#         print(f"❌ {customer}: '{product}' არ იყიდება")
#         failed.add(customer)
#     elif marag[product] < quantity:
#         print(f"⚠️ {customer}: {product} – მარაგში მხოლოდ {marag[product]} ცალია")
#         failed.add(customer)
#     else:
#         marag[product] -= quantity
#         cost = prices[product] * quantity
#         total += cost
#         print(f"✅ {customer}: {product} x{quantity} = {cost} ლარი")
#         expenses[customer] = expenses.get(customer, 0) + cost
#
# no_products = sorted([p for p, s in marag.items() if s == 0])
# sorted_failed_customers = sorted(list(failed))
#
# print("--- ანგარიში ---")
# for customer, expense in expenses.items():
#     print(f"{customer}: {expense} ლარი")
#
# print(f"შემოსავალი: {total} ლარი")
# print(f"ამოიწურა: {no_products}")
# print(f"წარუმატებელი შეკვეთა ჰქონდათ: {sorted_failed_customers}")