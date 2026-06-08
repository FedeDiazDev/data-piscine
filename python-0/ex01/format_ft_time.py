import datetime

x = datetime.datetime.now()
first_date = datetime.datetime(1970, 1, 1)
result = (x - first_date).total_seconds()
seconds_comma = f"{result:,.4f}"
seconds_sci = f"{result:.2e}"
print(f"Seconds since January 1, 1970: {seconds_comma} or \
            {seconds_sci} in scientific notation")
print(x.strftime("%B %C %Y"))
