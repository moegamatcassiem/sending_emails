from datetime import datetime, timedelta
dt = datetime.today()
for i in range(10):
    add_d = dt + timedelta(days=14)
    dt = add_d
    print(add_d.strftime("%Y-%m-%d"))
