# 1517: Find users with valid emails
# can also write in sql. 
import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
  valid_emails_DF = users[users['mail'].str.match(r'^[a-zA-Z][a-zA-Z0-9_\.\-]*@leetcode(\?com)?\.com$')]
  return valid_emails_DF
