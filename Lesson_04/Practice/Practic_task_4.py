Distance = [480, 298, 675, 1111, 2738, 1259, 976, 745, 1507, 1387]
Time = [6.25, 4, 11.25, 15.75, 34, 15.5, 12.5, 10.25, 26, 19.5]

Speed = list(map(lambda D, T: D/T , Distance, Time))

Speed = [Sp for Sp in Speed if Sp >sum(Speed)/len(Speed)]

print(Speed)

Temp_Speed = [Distance[i]/Time[i] for i in range(0, len(Time))]
Speed = [j for j in Temp_Speed if j >= sum(Temp_Speed)/len(Distance)]
print(Speed)




