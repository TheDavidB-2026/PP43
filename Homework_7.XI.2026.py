# # # ნომერი 1
# # import json
# # from json import JSONDecodeError
# #
# # def save_json(path, data):
# #     with open(path, 'w', encoding='utf-8') as f:
# #         json.dump(data, f, ensure_ascii=False, indent=2)
# #
# # def load_json(path, default=None):
# #     try:
# #         with open(path, 'r', encoding='utf-8') as f:
# #             return json.load(f)
# #     except (FileNotFoundError, JSONDecodeError):
# #         return default
# #
# # if __name__ == "__main__":
# #     data = {"name": "ნინო", "scores": [90, 85], "pair": (1, 2)}
# #     save_json("test.json", data)
# #     loaded_data = load_json("test.json")
# #     print(loaded_data)
# #     print(type(loaded_data["pair"]))
# #
# #     print(load_json("nonexistent.json", default={}))
# #
# #     with open("invalid.json", "w", encoding='utf-8') as f:
# #         f.write('{"name": "ნინო",}')
# #     print(load_json("invalid.json", default="არასწორი ფაილი"))
#
# #ნომერი 2
# from dataclasses import dataclass, field, asdict
# import json
#
#
# @dataclass
# class Movie:
#     title: str
#     year: int = 2000
#     rating: float = 0.0
#     genres: list = field(default_factory=list)
#
#     def __post_init__(self):
#         if not (0 <= self.rating <= 10):
#             raise ValueError("რეიტინგი უნდა იყოს 0-დან 10-მდე")
#
#
# def best_movies(movies, min_rating):
#     filtered = [m for m in movies if m.rating >= min_rating]
#     return sorted(filtered, key=lambda m: m.rating, reverse=True)
#
#
# m1 = Movie("მონანიება", 1984, 9.1, ["დრამა"])
# m2 = Movie("გზა", 2020, 7.5)
# m3 = Movie("მოგზაურობა", rating=8.2, genres=["თავგადასავალი"])
#
# movies = [m1, m2, m3]
#
# print(m1)
# print(m1 == Movie("მონანიება", 1984, 9.1, ["დრამა"]))
#
# m2.genres.append("კომედია")
# print(m2.genres, m3.genres)
#
# for movie in best_movies(movies, 8):
#     print(f"{movie.title} {movie.rating}")
#
# print(json.dumps(asdict(m1), ensure_ascii=False))
#
# try:
#     Movie("ცუდი", 2000, 11)
# except ValueError as e:
#     print(f"შეცდომა: {e}")