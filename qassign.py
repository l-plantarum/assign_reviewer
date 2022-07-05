#qassign.py
# D-Wave hybrid solverで発表会の部屋割りを実施する

import pandas as pd
import dimod
from dwave.system import LeapHybridSampler, LeapHybridBQMSampler
from pyqubo import Array

classcsv = pd.read_csv("list.csv", encoding="UTF-8", sep=",")
#学生数
n_students = len(classcsv)
#教員数
teachers = []
for i in range(n_students):
  if classcsv.iloc[i]['ゼミ教員'] not in teachers:
    teachers.append(classcsv.iloc[i]['ゼミ教員'])
n_teachers = len(teachers)

NROOM = 4
n_room_student = n_students / NROOM
n_room_teacher = n_teachers / NROOM
x = Array.create("x", shape=(NROOM, n_students+n_teachers), vartype='BINARY')

p = 0

for i in range(NROOM):
  # 先生の人数の均等化
  p += (sum(x[i][j] for j in range(n_students, n_students + n_teachers)) - n_room_teacher) ** 2
  # 学生の人数の均等化
  p += (sum(x[i][j] for j in range(n_students)) - n_room_student) ** 2

# どの学生もどの先生も一か所の部屋にしかいない
for j in range(n_students+n_teachers):
  p += (sum(x[i][j] for i in range(NROOM)) - 1) ** 2
# 学生とゼミの先生は同じ部屋にはいない
for j in range(n_students):
  teacher = teachers.index(classcsv.iloc[j]["ゼミ教員"])
  for i in range(NROOM):
    p += x[i][j] * x[i][n_students + teacher]


model = p.compile()
bqm = model.to_bqm()
sampler = LeapHybridBQMSampler()
response = sampler.sample(bqm)
decoded = model.decode_sampleset(response)
results = decoded[0].sample

for i in range(NROOM):
  print("room", i+1)
  print("学生", end=":")
  for j in range(n_students):
    if results[f'x[{i}][{j}]'] == 1:
      print(classcsv.iloc[j]["学生名"], end=",")
  print("教員", end=":")
  for j in range(n_students, n_students + n_teachers):
    if results[f'x[{i}][{j}]'] == 1:
      print(teachers[j-n_students], end=",")
  print()
