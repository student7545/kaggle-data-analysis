import math,statistics

data_list = []
header_list =[]

with open("Finance_data.csv", "r") as file:
    for k in file:
        data_list.append(k.strip())

for i,data in enumerate(data_list):
    data_list[i] = data.replace("\n","").split(",")

for data in data_list[0]:
    header_list.append([data])

for data in data_list[1::]:
    for k in range(len(data)):
        header_list[k].append([data[k]])

def Gender_processing():
    total_count=0
    female_count=0
    male=0
    for k in header_list[0]:
        if k[0] == "Female":
            female_count+=1
            total_count+=1
        elif k[0] == "Male":
            male+=1
            total_count+=1
    print(f"Total count is {total_count}, total Male {male}, total Female {female_count},Male to Female ratio {float(male)/float(female_count)}")

def age():
    total_age=0
    oldest_age=0
    youngest = 0
    deviation = 0
    ages = [int(k[0]) for k in header_list[1][1:]]
    total_age = sum(ages)
    average = statistics.mean(ages)
    youngest =min(ages)
    oldest_age = max(ages)
    deviation = statistics.stdev(ages)
    print(f"The average age is {average}, youngest is {youngest}, oldest age is {oldest_age},total age: {total_age} and the std deviation is {deviation}")

def header_list_contain():
    for k,head in enumerate(header_list):
        print(k,head[0])

def Investment_Avenues():
    investment_list = [l[0] for l in header_list[2][1::]]
    count = len(investment_list)
    yes_count = investment_list.count("Yes")
    no_count = investment_list.count("No")
    print(f"Total count is {count}, total yes count is {yes_count}, total no count is {no_count}, ratio of yes to no count is {float(yes_count)/float(no_count)}")

def auto_stats():
    head_list = [l[0] for l in header_list]
    selection = [k for k in head_list[3:10:]]
    for k in selection:
        for head in header_list:
            if k == head[0]:
                print(f"for {k} the stats are:")
                values=[int(l[0]) for l in head[1:]]
                average=statistics.mean(values)
                total=sum(values)
                lowest=min(values)
                heighest=max(values)
                stdev=statistics.stdev(values)
                print(f"The Average is {average}, Total is {total}, lowest is {lowest}, heighest {heighest} and stdev is {stdev} \n")

def other_data():
    data_list = [l[0] for l in header_list[10:]]
    for k in range(len(data_list)):
        print(f"Stats for {data_list[k]}: ")
        if data_list[k] == header_list[10:][k][0]:
            data_values = [l[0] for l in header_list[10:][k][1:]]
            set_count =list(set(data_values))
            for k in set_count:
                print(k+" "+str(data_values.count(k)))
            print()


Gender_processing()
age()
Investment_Avenues()
auto_stats()
# header_list_contain()
other_data()
