import os

def save_scores(path: str, scores: dict[str, int]) -> None:


  with open(path, "w", encoding="utf-8") as file:
    for name, score in scores.items():
      file.write(f"{name}:{score}\n")

def add_score(path: str, name: str, score: int) -> None:


  with open(path, "a", encoding="utf-8") as file:
    file.write(f"{name}:{score}\n")

def read_scores(path: str) -> dict[str, int]:


  scores_dict = {}

  if not os.path.exists(path):
    print("⚠ ფაილი ვერ მოიძებნა")
    return scores_dict

  with open(path, "r", encoding="utf-8") as file:
    for line in file:
      line = line.strip()
      if not line:
        continue

      parts = line.split(":")
      if len(parts) == 2:
        name, score_str = parts
        scores_dict[name] = int(score_str)

  return scores_dict

os.makedirs("data", exist_ok=True)
save_scores("data/scores.txt", {"ნინო": 92, "გიორგი": 78, "ანა": 85})
add_score("data/scores.txt", "დათო", 64)
add_score("data/scores.txt", "მარიამი", 97)

with open("data/scores.txt", encoding="utf-8") as file:
  print(file.read(), end="")

scores = read_scores("data/scores.txt")
print(scores)


total_students = len(scores)
print(f"სტუდენტები: {total_students}")

if total_students > 0:
  avg_score = round(sum(scores.values()) / total_students, 1)
else:
  avg_score = 0.0
print(f"საშუალო ქულა: {avg_score}")

if scores:
  best_student = max(scores, key=scores.get)
  print(f"საუკეთესო: {best_student} {scores[best_student]}")

passed_students = []
for name, score in scores.items():
  if score >= 80:
    passed_students.append(name)

with open("data/passed.txt", "w", encoding="utf-8") as file:
  for name in passed_students:
    file.write(f"{name}\n")

read_passed = []
with open("data/passed.txt", "r", encoding="utf-8") as file:
  for line in file:
    cleaned_line = line.strip()
    if cleaned_line:
      read_passed.append(cleaned_line)

print(f"ჩააბარეს (80+): {read_passed}")