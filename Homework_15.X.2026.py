#ზუსტად ვიცი, არასწორი იქნება, მაგრამ ტერმინალიდან შეყვანით დაწერას უბრალოდ ვერ მივხვდი
EXTRA_PRICES = {"popcorn": 6, "cola": 3, "nachos": 7}

def book_tickets(movie, *seats, discount=0, **extras):
    is_valid = lambda s: len(s) >= 2 and s[0] in "ABCDE" and s[1:].isdigit() and 1 <= int(s[1:]) <= 10

    valid_seats = list(filter(is_valid, seats))
    rejected_count = len(seats) - len(valid_seats)

    get_price = lambda s: 15 if s[0] in "AB" else 10
    ticket_prices = list(map(get_price, valid_seats))

    total_tickets = sum(ticket_prices) * (1 - discount / 100)
    total_extras = sum(EXTRA_PRICES.get(item, 0) * count for item, count in extras.items())
    total_sum = round(total_tickets + total_extras, 2)

    return {
        "movie": movie,
        "seats": valid_seats,
        "rejected": rejected_count,
        "total": total_sum
    }

order1 = book_tickets("ოპენჰაიმერი", "A5", "C3", "Z1", "B12", "E10")
order2 = book_tickets("დიუნა", "B1", "B2", discount=20, popcorn=2, cola=2)
order3 = book_tickets("ინტერსტელარი", "D4", nachos=1)
order4 = book_tickets("ბარბი")

for order in [order1, order2, order3, order4]:
    print(f"{order['movie']}: ადგილები {order['seats']}, უარყოფილი: {order['rejected']}, სულ: {order['total']} ლარი")