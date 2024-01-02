# 1907: Count salary categories
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_salary = accounts[accounts.income < 20000]
    avg_salary = accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)]
    high_salary = accounts[accounts.income > 50000]

    category_cnt = pd.DataFrame({'category':['Low Salary', 'Average Salary', 'High Salary'], 
                                'accounts_count':[len(low_salary), len(avg_salary), len(high_salary)]})
    return category_cnt
