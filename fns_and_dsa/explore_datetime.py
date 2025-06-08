from datetime import date,datetime, timedelta
def display_current_datetime():
    current_date  = datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))
    
display_current_datetime()


def calculate_future_date():
    today = date.today()
    days_to_add = int(input("Enter the number of days to add to the current date:"))
    future_date = today + timedelta(days=days_to_add)
    print("Future date is:", future_date.strftime("%Y-%m-%d"))

calculate_future_date()    
