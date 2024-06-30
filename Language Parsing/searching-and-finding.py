import re

text = "In the quiet town of Glenwood Springs, a peculiar event unfolded one warm summer evening. The townsfolk gathered in the central square, their eyes fixed on the sky, where an unusual array of lights flickered and danced. Whispers of alien encounters and secret government projects buzzed through the crowd, fueling both excitement and trepidation.Amid the spectators, an old clockmaker named Mr. Whitfield observed the phenomenon with keen interest. He had lived in Glenwood Springs for over fifty years and had never seen anything quite like it. The lights moved in synchronized patterns, creating intricate shapes and symbols that seemed almost deliberate. As the display continued, Mr. Whitfield’s curiosity grew. At the edge of the square, a young journalist named Emily Daniels took copious notes, determined to uncover the truth behind the spectacle. She had recently moved to Glenwood Springs, drawn by the town's rich history and mysterious allure. Her investigations had led her to discover that the area was once home to an ancient civilization, whose artifacts hinted at advanced astronomical knowledge."

# Check if the first word is the
the = re.match("the", text)
print(the)  # None
# Check if the first word is In
in_match = re.match("In", text)
print(in_match.group(0))

# Find the first occurence of the word quiet (search from left to right)
quiet = re.search("quiet", text)
print(quiet) 
print(quiet.group(0))

# Find all quiet 
all_quiet = re.findall("quiet", text)
print(all_quiet)

# Find all the
all_the = re.findall("the", text)
num_of_the = len(all_the)
print(all_the)
print(num_of_the)