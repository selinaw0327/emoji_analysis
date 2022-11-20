import twint
import datetime
since = datetime.datetime(2022, 11, 4)
until = datetime.datetime(2022, 11, 5)
print(since)
print(until)
# since = '2022-11-04 00:00:00'
# until = '2022-11-05 00:00:00'

# Configure
c = twint.Config()
# c.Limit = 100
c.Search = "elonmusk twitter"
c.Lang= "en"
c.Store_csv = True
# c.Since = since
# c.Until = until
c.Until = str(until)
# c.Since = str(since)
c.Output = "./tweets.csv"
# Run
twint.run.Search(c)
# Tweets_df = twint.storage.panda.Tweets_df
#
# df2 = Tweets_df[['tweet']]
# print(df2)