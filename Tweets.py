import twint
import datetime
since = datetime.datetime(2022, 11, 4)
until = datetime.datetime(2022, 11, 5)
print(since)
print(until)

# Configure
c = twint.Config()
c.Limit = 100
c.Search = "elonmusk twitter"
c.Lang= "en"
c.Store_csv = True
c.Until = str(until)
# c.Since = str(since)
c.Output = "./tweets.csv"
# Run
twint.run.Search(c)
