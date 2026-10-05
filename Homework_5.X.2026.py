# 1. სიმბოლოს დათვლა სიტყვაში
# wrd = input("შეიყვანე სიტყვა: ")
# smb = input("რომელი სიმბოლო დავთვალოთ: ")
#
# cnt = 0
#
# for smbfinal in wrd:
#     if smbfinal == smb:
#         cnt += 1
#
# print(f"სიმბოლო {smb} გვხვდება {cnt} -ჯერ")

# 2. პაროლის შემოწმება სამი მცდელობით
# correct = "python2024"
# att = 3
#
# while att > 0:
#     pwd = input("შეიყვანე პაროლი: ")
#
#     if pwd == "":
#         continue
#
#     elif pwd == correct:
#         print("წვდომა დაშვებულია")
#         break
#     else:
#         att -= 1
#         print(f"არასწორი პაროლი. დარჩენილი მცდელობა: {att}")
# else:
#     print("ანგარიში დაბლოკილია")