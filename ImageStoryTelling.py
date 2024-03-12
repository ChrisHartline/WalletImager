import random

def switch_1():
    options = ['a magical kingdom', 'a futuristic city', 'a haunted forest']
    probabilities = [0.4, 0.35, 0.25]
    return random.choices(options, probabilities)[0]

def switch_2():
    options = ['a brave knight', 'a clever robot', 'a mischievous ghost']
    probabilities = [0.65, 0.25, 0.1]
    return random.choices(options, probabilities)[0]

# Generate the story
setting = switch_1()
character = switch_2()

story = f"Once upon a time, in {setting}, there lived {character}. "

if setting == 'a magical kingdom':
    story += "The kingdom was known for its enchanted castles and talking animals. "
elif setting == 'a futuristic city':
    story += "The city was filled with flying cars and towering skyscrapers. "
else:
    story += "The forest was rumored to be inhabited by spirits and mythical creatures. "

if character == 'a brave knight':
    story += "The knight was on a quest to save the land from an evil sorcerer. "
elif character == 'a clever robot':
    story += "The robot was programmed to solve complex puzzles and protect the city. "
else:
    story += "The ghost enjoyed playing pranks on unsuspecting visitors. "

story += "And so, the adventure began..."

with open('story.txt', 'w') as f:
    f.write(story)

# print(story)