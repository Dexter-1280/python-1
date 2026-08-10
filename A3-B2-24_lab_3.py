C = {203, 204, 207, 216, 217, 219, 226, 227, 230, 233, 239, 248, 250, 254, 260, 262, 272, 279, 281, 282, 289, 291, 292, 293, 294, 298, 299, 304, 307, 308, 309, 315, 322, 324, 331, 332, 337, 343, 345, 346, 347, 348, 349, 350, 354, 358, 361, 368, 370, 371, 373, 374, 376, 379, 383, 385, 388, 392, 393, 395, 397, 406, 409, 412, 414, 416, 417, 420, 421, 427, 433, 444, 446, 448, 454, 455, 456, 457, 459, 461, 467, 469, 470, 473, 482, 487, 494, 499}

print(C)
print(len(C))

F = {200, 202, 203, 220, 222, 225, 226, 229, 237, 241, 252, 253, 260, 262, 264,
269, 270, 276, 282, 283, 289, 290, 293, 296, 298, 300, 302, 309, 311, 312, 313,
319, 320, 322, 325, 328, 329, 337, 342, 343, 353, 355, 357, 358, 363, 364, 370,
371, 374, 375, 381, 382, 390, 395, 400, 406, 415, 416, 418, 420, 421, 428, 432,
435, 436, 437, 438, 444, 452, 458, 461, 471, 472, 476, 478, 479, 484, 488, 490,
494, 497, 498, 499}

print(F)
print(len(F))

R = {203, 204, 205, 207, 211, 212, 213, 220, 223, 225, 226, 229, 233, 235, 244,
245, 246, 247, 248, 251, 252, 254, 256, 259, 261, 265, 267, 269, 270, 281, 283,
287, 289, 290, 295, 298, 302, 324, 332, 335, 336, 338, 344, 349, 350, 355, 356,
359, 362, 364, 367, 369, 374, 375, 377, 378, 382, 384, 392, 394, 395, 398, 401,
403, 406, 407, 410, 414, 416, 424, 426, 429, 431, 432, 435, 439, 442, 454, 460,
461, 462, 466, 467, 472, 473, 476, 496, 498}

print(R)
print(len(R))

all_three = C & F & R
print(all_three)
print(len(all_three))

only_C=C-F-R

only_F=F-C-R

only_R=R-C-F

only_one=only_C|only_F|only_R
print(len(only_one))

#2

Employee_data = {
101:['Shivay',24,'Content Strategist'],
102:['Udit naryan',25,'Content Strategist'],
103:['Sonam wanchuck',28,'Sr Manager'],
104:['Arsani malik',29,'Project Lead'],
105:['Huzefa ',32,'Project Manager']
}

oldest=max(Employee_data.values(),key=lambda x:x[1])
print(oldest)

if 159 in Employee_data:
    print(Employee_data[159])
else:
    print("NA")

print(len(Employee_data))

total = 0
for employee in Employee_data.values():
    total += employee[1]
mean = total / len(Employee_data)
print(mean)

for id in [104, 140, 164]:
    if id in Employee_data:
        Employee_data[id][1] = 27
total = 0
for employee in Employee_data.values():
    total += employee[1]
mean = total / len(Employee_data)
print(Employee_data)
print(mean)

#3

input_dict={'Jack Dorsey': 'Twitter','Tim Cook': 'Apple','Jeff Bezos': 'Amazon','Mukesh Ambani': 'RJIO'}
values=input_dict.values()
sorted_values=sorted(values)
print(sorted_values)

#4

Olympic= {'Great Britain':{'GBR':{'Gold':29,'Silver':17,'Bronze':19}},
'China':{'CHN':{'Gold':38,'Silver':28,'Bronze':22}},
'Russia':{'RUS':{'Gold':24,'Silver':25,'Bronze':32}},
'United States':{'USA':{'Gold':46,'Silver':28,'Bronze':29}},
'Korea':{'KOR':{'Gold':13,'Silver':8,'Bronze':7}},
'Japan':{'JPN':{'Gold':7,'Silver':14,'Bronze':17}},
'Germany':{'GER':{'Gold':11,'Silver':11,'Bronze':14}}}

max_gold = 0
for country in Olympic:
    gold = Olympic[country][list(Olympic[country].keys())[0]]['Gold']
    if gold > max_gold:
        max_gold = gold
        max_country = country
print(max_country)

for country in Olympic:
    gold = Olympic[country][list(Olympic[country].keys())[0]]['Gold']
    if gold > 20:
        print(country)

for country in Olympic:
    code = list(Olympic[country].keys())[0]
    gold = Olympic[country][code]['Gold']
    silver = Olympic[country][code]['Silver']
    bronze = Olympic[country][code]['Bronze']
    total = gold + silver + bronze
    print(country, gold, total)

#5

students = {}
def create_mail(name):
    names = name.split()
    mail = names[-1].lower()+names[0][0].lower()+names[1][0].lower()+"@rknec.edu"
    students[mail] = name
for i in range(5):
    name = input("Enter name: ")
    create_mail(name)
print(students)
