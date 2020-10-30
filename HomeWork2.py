import json

sample_dict = {
   "class_a":{
      "student1":{
         "name":"Misha",
         "marks":{
            "math":90,
            "history":85
         }
      }
   }
}


print(sample_dict["class_a"]["student1"]["name"])
print(sample_dict["class_a"]["student1"]["marks"]["history"])

sample_dict["class_a"]["student2"] = {
         "name":"Petya",
         "marks":{
            "math":14,
            "history":88
         }
      }

sample_dict["class_b"] = {
      "student1":{
         "name":"Vasya",
         "marks":{
            "math":42,
            "history":21
         }
      }
   }

sample_dict['class_a']['student1']['marks']['physics'] = 15
sample_dict['class_a']['student2']['marks']['physics'] = 67
sample_dict['class_b']['student1']['marks']['physics'] = 77

misha = list(sample_dict['class_a']['student1']['marks'].values())
petya = list(sample_dict['class_a']['student2']['marks'].values())
vasya = list(sample_dict['class_b']['student1']['marks'].values())
misha = round((sum(misha) / 3), 2)
petya = round((sum(petya) / 3), 2)
vasya = round((sum(vasya) / 3), 2)

print(misha, petya, vasya)

# print(json.dumps(sample_dict, indent=2))
# 1. Вывести значение ключа "name";
# 2. Вывести значение ключа "history";
# 3. Добавить нового студента в "class_a", соответственно его "name" и "marks";
# 4. Добавить новый класс со студентами;
# 5. Добавить каждому студенту в "marks" предмет "physics" с оценкой;
# 6. Подсчитать средний бал по каждому студенту (результат округлить до 2 знаков после запятой);
# 7. Создать словарь со средним баллом за каждого студента;
# 8. Определить лучшего студента по успеваемости;
# 9. Подсчитать средний бал по каждому классу (результат округлить до 2 знаков после запятой);
# 8. Создать словарь со средним баллом за классы;
# 9. Определить лучший класс по успеваемости.