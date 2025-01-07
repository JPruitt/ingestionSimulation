from datetime import datetime

def get_current_date():
    x = datetime.today()
    return x.strftime("%Y-%m-%d")

