def timeConversion(s):
    period = s[-2:]        
    hour = int(s[:2])
    rest = s[2:-2]       

    if period == "AM":
        if hour == 12:
            hour = 0
    else:  
        if hour != 12:
            hour += 12

    return f"{hour:02d}{rest}"


if __name__ == "__main__":
    s = input().strip()          
    result = timeConversion(s)   
    print(result)                

