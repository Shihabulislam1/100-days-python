# Finding remaining number of days ,month, weeks and years left if you live until 90 years old


age=int(input("Enter your age:\n"))


remaining_age_year=90-age

remaining_age_month=remaining_age_year*12

remaining_age_week=remaining_age_year*52

remaining_age_day=remaining_age_year*365


print(f"You have {remaining_age_day} days, {remaining_age_week} weeks, {remaining_age_month} months and {remaining_age_year} years left.")
