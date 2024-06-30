import re

character_1 = "Dorothy"
character_2 = "Henry"

regular_expression = re.compile("[A-Za-z]{7}")  # compile a re object
result_1 = regular_expression.match(character_1)
match_1 = result_1.group(0)

result_2 = re.match("[A-Za-z]{7}", character_2)
