print("=== AWS Server Cost Estimator===")
server_name=input("Enter sever profile name(e.g., ec2-large):")
hourly_rate=input("Enter the hourly cost of this server in dollars(e.g., 0.12):")
total_servers=input("How many instances of this server do you need?")
hourly_rate_num=float(hourly_rate)
total_servers_num=int(total_servers)
daily_cost=hourly_rate_num*24*total_servers_num
monthly_cost=daily_cost*30
print("\n--- BUDGET ESTIMATE SUMMARY---")
print(f"SERVER PROFILE:{server_name.upper()}")
print(f"Total Servers Action:{total_servers_num}")
print(f"DAily Infrastructure Cost:${daily_cost:.2f}")
print(f"Estimated Monthly Cost:${monthly_cost:.2f}")