full_name = input("Введите ФИО: ")
if full_name.isalpha():
    technology = input("Введите желаемую технологию: ")
    if technology.isalpha():
        framework = input("Введите фреймворк: ")
        if framework.isalpha():
            dbms = input("Введите субд: ")
            try:
                w_experience = float(input("Введите свой опыт работы: "))
                if full_name.isalpha() and technology.isalpha() and framework.isalpha() and dbms.isalpha():
                    if (technology == "Python") and (w_experience >= 5):
                        if (framework == "Django" or framework == "flask") and (dbms == "postgres" or dbms == "mysql"):
                            print(full_name,
                                  ", вы подходите на вакансию программист " + technology + " в компанию Медиасофт!")
                        else:
                            print(full_name,
                                  ", вы не подходите на вакансию программист " + technology + " в компанию Медиасофт")
                else:
                    print(full_name,
                          ", вы не подходите на вакансию программист " + technology + " в компанию Медиасофт")

                if (technology == "Java") and (w_experience >= 5):
                    if (framework == "Spring" or framework == "Spark") and (dbms == "Oracle" or dbms == "MSSQL"):
                        print(full_name,
                              ", вы подходите на вакансию программист" + technology + "в компанию Медиасофт!")
                    else:
                        print(full_name,
                              ", вы не подходите на вакансию программист " + technology + " в компанию Медиасофт")
                else:
                    print(full_name,
                          ", вы не подходите на вакансию программист " + technology + " в компанию Медиасофт")

            except ValueError:
                print("Введены некорректные данные об опыте работы.")
        else:
            print("Введены некорректные данные.")
    else:
        print("Введены некорректные данные.")
else:
    print("Введены некорректные данные.")
