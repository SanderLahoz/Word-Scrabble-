letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

letter_to_points = dict(zip(letters, points))
letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  word = word.upper()
  for letter in word:
    if letter in letter_to_points:
      point_total += letter_to_points.get(letter)
    else:
      point_total += 0
  return point_total


for players, values in player_to_words.items():
  points = 0
  for words in values:
    tmp = score_word(words)
    points += tmp

  player_to_points[players] = points

#print(player_to_points)
