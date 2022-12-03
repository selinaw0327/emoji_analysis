import pandas as pd
import emoji
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import statistics

# Keep tweets only
fields = ['tweet']
df = pd.read_csv('./files/tweets.csv', skipinitialspace=True, usecols=fields)

# Extract emojis from text
def extract_emojis(s):
    return ''.join(c for c in s if c in emoji.unicode_codes.EMOJI_DATA)

# Get tweets without emoji
def give_emoji_free_text(text):
    allchars = [str for str in text]
    emoji_list = [c for c in allchars if c in emoji.EMOJI_DATA]
    clean_text = ' '.join([str for str in text.split() if not any(i in str for i in emoji_list)])

    return clean_text

# Is the text written in English
def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


# Filter tweets with 1 emoji and store them into a csv file
new_df = df.reset_index()  # make sure indexes pair with number of rows
text_df = pd.DataFrame(columns=['Id', 'Emoji', 'Text'])
count = 0
for index, row in new_df.iterrows():
    emoji_str = extract_emojis(row['tweet'])
    if len(emoji_str) == 1:
        text = new_df.loc[index]
        clean_text = give_emoji_free_text(row['tweet'])
        if isEnglish(clean_text):
            text_df.loc[index] = [count, emoji_str, clean_text]
            count += 1

# pd.DataFrame(text_df).to_csv('./files/text.csv', encoding='utf-8', index=False)

# Create a table with tweets containing 😂 and calculate the sentiment score for each tweet
tears_of_joy_df = text_df[text_df['Emoji'] == '😂']
tears_of_joy_compound_score = []  # -1 means extremely negative, and +1 means extremely positive
tears_of_joy_positive_score = []
tears_of_joy_negative_score = []
tears_of_joy_neutral_score = []

tears_of_joy_df = tears_of_joy_df.reset_index()
for index, row in tears_of_joy_df.iterrows():
    sia = SentimentIntensityAnalyzer()
    ss = sia.polarity_scores(row['Text'])
    tears_of_joy_compound_score.append(ss.get("compound"))
    tears_of_joy_positive_score.append(ss.get("pos"))
    tears_of_joy_negative_score.append(ss.get("neg"))
    tears_of_joy_neutral_score.append(ss.get("neu"))

print(" Number of tweets containing 😂: " + str(len(tears_of_joy_df.index)))
print(" 😂 score: " + str(statistics.mean(tears_of_joy_compound_score)))
print(" 😂 positive score: " + str(statistics.mean(tears_of_joy_positive_score)))
print(" 😂 negative score: " + str(statistics.mean(tears_of_joy_negative_score)))
print(" 😂 neutral score: " + str(statistics.mean(tears_of_joy_neutral_score)))

# Create a table with tweets containing 🤣 and calculate the sentiment score for each tweet
rolling_laughing_df = text_df[text_df['Emoji'] == '🤣']
rolling_laughing_compound_score = []
rolling_laughing_positive_score = []
rolling_laughing_negative_score = []
rolling_laughing_neutral_score = []

rolling_laughing_df = rolling_laughing_df.reset_index()
for index, row in rolling_laughing_df.iterrows():
    sia = SentimentIntensityAnalyzer()
    ss = sia.polarity_scores(row['Text'])
    rolling_laughing_compound_score.append(ss.get("compound"))
    rolling_laughing_positive_score.append(ss.get("pos"))
    rolling_laughing_negative_score.append(ss.get("neg"))
    rolling_laughing_neutral_score.append(ss.get("neu"))

print(" Number of tweets containing 🤣: " + str(len(rolling_laughing_df.index)))
print(" 🤣 score: " + str(statistics.mean(rolling_laughing_compound_score)))
print(" 🤣 positive score: " + str(statistics.mean(rolling_laughing_positive_score)))
print(" 🤣 negative score: " + str(statistics.mean(rolling_laughing_negative_score)))
print(" 🤣 neutral score: " + str(statistics.mean(rolling_laughing_neutral_score)))

# Create a table with tweets containing 🤔 and calculate the sentiment score for each tweet
thinking_df = text_df[text_df['Emoji'] == '🤔']
thinking_compound_score = []
thinking_positive_score = []
thinking_negative_score = []
thinking_neutral_score = []

thinking_df = thinking_df.reset_index()
for index, row in thinking_df.iterrows():
    sia = SentimentIntensityAnalyzer()
    ss = sia.polarity_scores(row['Text'])
    thinking_compound_score.append(ss.get("compound"))
    thinking_positive_score.append(ss.get("pos"))
    thinking_negative_score.append(ss.get("neg"))
    thinking_neutral_score.append(ss.get("neu"))

print(" Number of tweets containing 🤔: " + str(len(thinking_df.index)))
print(" 🤔 score: " + str(statistics.mean(thinking_compound_score)))
print(" 🤔 positive score: " + str(statistics.mean(thinking_positive_score)))
print(" 🤔 negative score: " + str(statistics.mean(thinking_negative_score)))
print(" 🤔 neutral score: " + str(statistics.mean(thinking_neutral_score)))
