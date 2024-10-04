current_year = 2024
end_year = int(input("ENder the range of years from 2024 - "))
leap_year = []
for year in range(2024 , end_year+1):
    if(year % 4 ==0 and (year % 400 == 0 or year % 100 != 0)):
        leap_year.append(year)
print(leap_year)
