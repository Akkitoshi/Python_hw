full_name = input("Введите ФИО: ")
if full_name.isalpha():
    technology = input("Введите желаемую технологию: ")
    if technology.isalpha():
        framework = input("Введите фреймворк: ")
        if framework.isalpha():
            dbms = input("Введите субд: ")
            try:
                w_experience = float(input("Введите свой опыт работы: "))
                assert w_experience > 0, 'Опыт работы не может быть отрицательным числом'
                if w_experience >= 5:
                    if full_name.isalpha() and technology.isalpha() and framework.isalpha() and dbms.isalpha():
                        if technology.lower() == "python":
                            if (framework.lower() in ("django", "flask")) and (dbms.lower() in ("postgres", "mysql")):
                                print(full_name,
                                      ", вы подходите на вакансию программист " + technology + " в компанию Медиасофт!")
                            else:
                                print(full_name,
                                      ", вы не подходите на вакансию программист " + technology + " в компанию Медиасофт")
                    else:
                        print(full_name,
                              ", вы не подходите на вакансию программист " + technology + " в компанию Медиасофт")

                    if technology.lower() == "java":
                        if (framework.lower() in ("spring", "spark")) and (dbms.lower() in ("oracle", "mssql")):
                            print(full_name,
                                  ", вы подходите на вакансию программист " + technology + " в компанию Медиасофт!")
                        else:
                            print(full_name,
                                  ", вы не подходите на вакансию программист " + technology + " в компанию Медиасофт")
                    else:
                        print(full_name,
                              ", вы не подходите на вакансию программист " + technology + " в компанию Медиасофт")
                else:
                    print(full_name,
                          ", вы не подходите на вакансию программист " + technology + " в компанию Медиасофт")
            except ValueError:
                print("Введены некорректные данные.")
        else:
            print("Введены некорректные данные.")
    else:
        print("Введены некорректные данные.")
else:
    print("Введены некорректные данные.")
