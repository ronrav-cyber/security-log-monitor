# Automated Security Log Monitoring and Alert System

keywords = ["failed login", "unauthorized", "access denied"]

with open("sample_log.txt", "r") as log_file:
    for line in log_file:
        for keyword in keywords:
            if keyword.lower() in line.lower():
                print("ALERT:", line.strip())
                