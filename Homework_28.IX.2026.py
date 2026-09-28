# 1. მომხმარებლის სახელის ნორმალიზება (სფეისები ვერ მოვაშორე)
# raw_name=input("შეიყვანეთ მომხმარებლის სახელი: ")
#
# name=raw_name.strip().lower().replace("_", "-")
# print(f"მომხმარებლის სახელი: {name}")
# print(f"სიგრძე: {len(name)}")
# print(f"იწყება 'super'-ით: {name.startswith('super')}")
# print(f"ტირეების რაოდენობა: {name.count('-')}")
#
# is_alnum =name.replace("-", "").isalnum()
# print(f"მხოლოდ ასოები და ციფრები: {is_alnum}")


# 2. ბარათის შენიღბვა და ნომრის ფორმატირება
# card = input("შეიყვანეთ ბარათის ნომერი: ")
# phone = input("შეიყვანეთ ტელეფონის ნომერი: ")
#
# new_card = "**** **** **** " + card[-4:]
#
# digit4 = card[:4]
# len = len(card.strip())
# crd_reverse = card[::-1]
#
# output_phone = f"{phone[:3]} {phone[3:5]} {phone[5:7]} {phone[7:]}"
#
# print(f"შენიღბული: {new_card}")
# print(f"პირველი 4 ციფრი: {digit4}")
# print(f"ციფრების რაოდენობა: {len}")
# print(f"შემობრუნებული: {crd_reverse}")
# print(f"ტელეფონი: {output_phone}")