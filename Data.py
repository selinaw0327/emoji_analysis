import pandas as pd
import emoji
import regex
from collections import Counter
from collections import OrderedDict
from itertools import combinations

# Keep tweets only
fields = ['tweet']
df = pd.read_csv('./files/tweets.csv', skipinitialspace=True, usecols=fields)


# Extract emojis from text
def extract_emojis(s):
    return ''.join(c for c in s if c in emoji.unicode_codes.EMOJI_DATA)


# Count the total number of tweets which contain emojis
new_df = df.reset_index()  # make sure indexes pair with number of rows
count = 0
emoji_list = []
emoji_df = pd.DataFrame(columns=['Tweet Emoji'])

for index, row in new_df.iterrows():
    emoji_str = extract_emojis(row['tweet'])
    if emoji_str != "":
        count = count + 1
        emoji_df.loc[index] = [emoji_str]

    # emoji_list.append(extract_emojis(row['tweet']))

print("Total number of tweets containing emojis: ", count)


#pd.DataFrame(emoji_df).to_csv(".files/out.csv", encoding='utf-8', index=False)


# Count emoji occurrences
def split_count(text):
    emoji_list = []
    for word in text:
        if any(char in emoji.unicode_codes.EMOJI_DATA for char in word):
            emoji_list.append(word)

    return emoji_list


text = df['tweet']
emoji_list = []
for t in text:
    emoji_list = emoji_list + split_count(t)

emoji_occurrences = Counter(emoji_list)
print(emoji_occurrences)

# Create node list
nodes = pd.DataFrame(columns=['Id', 'Label', 'Emoji', 'image'])
distinct_emojis = list(OrderedDict.fromkeys(emoji_list))

row_count = 0
for i in range(len(distinct_emojis)):
    result = emoji.demojize([distinct_emojis[i]], delimiters=("", ""))
    emoji_unicode = f'U+{ord(distinct_emojis[i]):X}'
    image_filename = emoji_unicode.strip("U+").lower() + ".png"
    nodes.loc[i] = [i, result, distinct_emojis[i], image_filename]

pd.DataFrame(nodes).to_csv(".files/nodes.csv", encoding='utf-8', index=False)

# Create edge list
edges = pd.DataFrame(columns=['Source', 'Target'])
df = emoji_df.reset_index()
i = 0
for index, row in df.iterrows():
    emojis = row['Tweet Emoji']
    if len(emojis) > 1:
        result = list(combinations(emojis, 2))
        for pair in result:
            if pair[0] != pair[1]:
                source = emoji.demojize(pair[0], delimiters=("", ""))
                target = emoji.demojize(pair[1], delimiters=("", ""))
                s_id = nodes.Label[nodes.Label == source].index.tolist()
                t_id = nodes.Label[nodes.Label == target].index.tolist()
                edges.loc[i] = [s_id[0], t_id[0]]
                i += 1

pd.DataFrame(edges).to_csv(".files/edges.csv", encoding='utf-8', index=False)
