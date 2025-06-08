from datetime import date,datetime, timedelta
def display_current_datetime():
    current_date  = datetime.now()
    print(current_date)
    
display_current_datetime()


def calculate_future_date():
    today = date.today()
    future_date = int(input("Enter the number of days to add to the current date:"))
    new_date = today + timedelta(days=future_date)
    print("Future date is:", new_date.strftime("%Y-%m-%d"))

calculate_future_date()    
