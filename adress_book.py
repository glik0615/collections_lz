# Создаем словарь
slovar= {
"Катя":" г.Минск",
"Маша":"г.Браслав",
"Оля":"г.Витебск"} 

while True:  # условие всегда будет истиным
    print("выберите действие:")
    print("1.показать все адреса")
    print("2.изменить адрес")
    print("3.удалить запись")
    v = input("введите номер: ")  
    #Выбор номера
    if v =="1":
        print("все адреса:")
        for name, addres in slovar.items():   
            print("{name}:{addres}")
    elif v =="2":
        name = input('введите имя:')
        if name in slovar: #Ecли имя в словоре
            new_addres = input("введите адресс:")
            slovar[name]= new_addres   #изменить адресс
            print(slovar)
    elif v == '3':
      name = input("Введите имя человека: ")
      if name in slovar:
          del slovar[name] # Удаляем человека из словаря
          print(slovar)
      else:
        print("Человека с именем {name} нет в словаре.")