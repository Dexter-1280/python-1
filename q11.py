processed_orders = [1152,1154,1155,1136,1137,1160,1161,1166,1169,1170,1068,1176,1050,1178,1051,1052,1054,1058,1060,1061,1062,1065,1066,1057,1068,1069,1076,1077,1080,1081,1083,1091,1085,1089,1131,1092,1094,1095,1099,1102,1103,1104,1106,1107,1108,1109,1111,1117,1119,1121,1150,1128,1129,1136,1137,1139,1140,1141,1144,1148,1124]
returned_orders = [1153,1158,1159,1163,1164,1165,1167,1168,1171,1173,1174,1175,1177,1053,1055,1056,1057,1059,1063,1064,1070,1071,1072,1073,1074,1075,1078,1079,1082,1084,1086,1087,1090,1093,1096,1097,1098,1100,1101,1105,1110,1112,1113,1114,1115,1116,1118,1120,1122,1125,1126,1127,1130,1132,1135,1138,1142,1143,1145,1146,1147,1149,1151]

processed_count = len(processed_orders)
returned_count = len(returned_orders)
total_orders = processed_count + returned_count

print("processed Orders:", processed_count)
print("returned Orders:", returned_count)
print("Total Orders:", total_orders)
orders=processed_orders+returned_orders
orders.sort()
orders[49]
if orders[49] in processed_orders:
   print("This is in processed order")
else:
   print("This is in returned order")

print("First four of processed",orders[:4])
vowels = ['s','h','r','i','r','a','m','d','e','o','b','a','b','a','c','o','l','l','e','g','e']
count=0
for i in vowels:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count=count+1
print("Total count",count)
items=[23,23,45,57,234,54,34,443,54,]
count=0
target=23
for i in items:
     if i == target:
        count += 1

print(f"The item {target} is repeated {count} times.")