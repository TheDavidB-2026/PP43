# 1. მაღაზიის ფასდაკლება
# try:
#     amount = float(input("შეიყვანეთ ყიდვის თანხა: "))
# except (ValueError):
#     print("შეცდომა: გთხოვთ შეიყვანოთ სწორი რიცხვი.")
#     exit()
#
# promo= input("შეიყვანეთ პრომო-კოდი (თუ არ გაქვთ, დააჭირეთ Enter): ").strip()
#
# if amount >= 200:
#     discount= 20
# elif amount >= 100:
#     discount = 10
# elif amount >= 50:
#     discount = 5
# else:
#     discount= 0
#
# discount_amount = amount * (discount/ 100)
# final= amount - discount_amount
#
# if promo.lower() == "vip":
#     print("🎁 VIP კოდი: დამატებით -5 ლარი")
#     final-= 5
#
# final_amount = max(0.0, final)
#
# print(f"ფასდაკლების პროცენტი: {discount}%")
# print(f"გადასახდელი თანხა: {final:.2f} ლარი")

# 2. სტუდენტის შეფასების სისტემა
# try:
#     name = input("შეიყვანეთ სტუდენტის სახელი: ")
#     name2 = name.strip()
#
#     initial = name2[0]
#
#     score_input = input("შეიყვანეთ მიღებული ქულა (მთელი რიცხვი): ")
#     score = int(score_input)
#
#     max_score_input = input("შეიყვანეთ მაქსიმალური ქულა (მთელი რიცხვი): ")
#     max_score = int(max_score_input)
#
#     if max_score == 0:
#         raise ZeroDivisionError
#
#     if score < 0 or score > max_score:
#         raise ValueError("range_error")
#
# except IndexError:
#     print("❌ სახელი ცარიელი ვერ იქნება")
#
# except ValueError as verr:
#     if str(verr) == "range_error":
#         print("❌ ქულა არასწორ დიაპაზონშია")
#     else:
#         print("❌ ქულები მთელი რიცხვებით ჩაწერთ")
#
# except ZeroDivisionError:
#     print("❌ მაქსიმალური ქულა 0 ვერ იქნება")
#
# else:
#     percent = (score / max_score) * 100
#
#     if percent >= 91:
#         grade = "A"
#     elif percent >= 81:
#         grade = "B"
#     elif percent >= 71:
#         grade = "C"
#     elif percent >= 61:
#         grade = "D"
#     elif percent >= 51:
#         grade = "E"
#     elif percent >= 41:
#         grade = "FX"
#     else:
#         grade = "F"
#
#     print(f"\nსტუდენტის ინიციალი: {initial}")
#     print(f"პროცენტი: {percent:.2f}%")
#     print(f"შეფასება: {grade}")
#
# finally:
#     print("\nშეფასების სისტემამ მუშაობა დაასრულა")