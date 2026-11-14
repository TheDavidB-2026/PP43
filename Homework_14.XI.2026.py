# #სავარჯიშო 1
# # import asyncio
# # import time
# #
# #
# # async def deliver(order, seconds):
# #     """კორუტინა, რომელიც ასახიერებს შეკვეთის გაგზავნას და მიტანას."""
# #     print(f"{order}: გაიგზავნა")
# #     await asyncio.sleep(seconds)
# #     print(f"{order}: მიტანილია")
# #
# #
# # async def main():
# #     orders = [
# #         ("შეკვეთა #1", 1.0),
# #         ("შეკვეთა #2", 1.5),
# #         ("შეკვეთა #3", 2.0)
# #     ]
# #
# #     start_time = time.perf_counter()
# #     for order, seconds in orders:
# #         await deliver(order, seconds)
# #     seq_time = time.perf_counter() - start_time
# #     print(f"ზედიზედ: {seq_time:.1f} წმ\n")
# #
# #     start_time = time.perf_counter()
# #     await asyncio.gather(*(deliver(order, seconds) for order, seconds in orders))
# #     conc_time = time.perf_counter() - start_time
# #     print(f"ერთდროულად: {conc_time:.1f} წმ")
# #
# #     speedup = seq_time / conc_time if conc_time > 0 else 0
# #     print(f"დაჩქარება: {speedup:.1f}x")
# #
# #     # 4. ყველა შეკვეთა პარალელურად მუშავდება და მთლიანი პროცესი დასრულდება მაშინ, როცა ყველაზე ხანგრძლივი შეკვეთა დასრულდება.
# #
# # if __name__ == "__main__":
# #     asyncio.run(main())
#
# #სავარჯიშო 2
# # import asyncio
# # import time
# #
# # async def square(number):
# #     await asyncio.sleep(1)
# #     return number * number
# #
# #
# # async def main():
# #     numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# #
# #     start_time = time.perf_counter()
# #
# #     squares = await asyncio.gather(*(square(n) for n in numbers))
# #
# #     end_time = time.perf_counter()
# #
# #     for n, s in zip(numbers, squares):
# #         print(f"{n}² = {s}")
# #
# #     print(f"ჯამი: {sum(squares)}")
# #     print(f"დრო: {end_time - start_time:.1f} წმ")
# # asyncio.run(main())
# #
# # # 4. asyncio.gather()-ით 8-ვე რიცხვის კვადრატი ერთდროულად გამოითვლება და არა ცალ-ცალკე
#
# #სავარჯიშო 3
# import asyncio
# import time
#
#
# async def load_user(user_id):
#     await asyncio.sleep(1)
# # შეცდომა 1: time.sleep(1)-ის ნაცვლად გამოყენებულია ასინქრონული await asyncio.sleep(1) (ლოდინის შეცდომა)
#     return {"id": user_id, "name": f"მომხმარებელი {user_id}"}
#
#
# async def main():
#     start_time = time.perf_counter()
#  # შეცდომა 2: ციკლის ნაცვლად ვიყენებთ asyncio.gather-ს, რომ სამივე მომხმარებელი ერთდროულად ჩაიტვირთოს (კორუტინის შეცდომა)
#     users = await asyncio.gather(*(load_user(user_id) for user_id in (1, 2, 3)))
#
#     end_time = time.perf_counter()
#
#     print(users)
#     print(f"დრო: {end_time - start_time:.1f} წმ")
#
# # შეცდომა 3: main() პირდაპირი გამოძახების ნაცვლად ვიყენებთ asyncio.run(main())-ს პროგრამის გასაშვებად (პროგრამის დაწყების შეცდომა)
# asyncio.run(main())