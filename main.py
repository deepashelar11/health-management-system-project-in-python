def getdate():
    import datetime
    return datetime.datetime.now()


lock_retrieve = int(input("want to lock or retrive - (1 for lock and 2 for retrive)\n"))

if lock_retrieve == 1:
    client = int(input("which client would you like to lock(press 1 or 2) - "
                       "\n client name - \n 1. deepa \n 2. pooja \n"))
    if client==1:
        diet_exercise = int(input("what would you like to lock diet or exercise "
                                  "(press 1 for diet and 2 for exercise -  )\n"))
        if diet_exercise == 1:
            with open("deepa_diet.txt", "a") as f:
                eat = input("what you eat - ")
                time = str(getdate())
                f.write(time)
                f.write("  ")
                f.write(eat)

        elif diet_exercise == 2:
            with open("deepa_exer.txt", "a") as f:
                exercise = input("which exercise you did - ")
                time = str(getdate())
                f.write(time)
                f.write("  ")
                f.write(exercise)

    elif client == 2:
        diet_exercise = int(input("what would you like to lock diet or exercise "
                                  "(press 1 for diet and 2 for exercise -   )\n"))
        if diet_exercise == 1:
            with open("pooja_diet.txt", "a") as f:
                eat = input("what you eat - ")
                time = str(getdate())
                f.write(time)
                f.write("\n")
                f.write(eat)

        elif diet_exercise == 2:
            with open("pooja_exer.txt", "a") as f:
                exercise = input("which exercise you did - ")
                time = str(getdate())
                f.write(time)
                f.write("\n")
                f.write(exercise)




elif lock_retrieve == 2:
    client = int(input("which client would you like to retrive(press 1 or 2) - "
                       "\n client name - \n 1. deepa \n 2. pooja  \n"))
    if client==1:
        diet_exercise = int(input("what would you like to retrive diet or exercise "
                                  "(press 1 for diet and 2 for exercise -  )\n"))
        if diet_exercise == 1:
            with open("deepa_diet.txt") as f:
                print(f.read())

        elif diet_exercise == 2:
            with open("deepa_exer.txt") as f:
                print(f.read())

    elif client == 2:
        diet_exercise = int(input("what would you like to retrive diet or exercise "
                                  "(press 1 for diet and 2 for exercise -  \n)"))
        if diet_exercise == 1:
            with open("pooja_diet.txt") as f:
                print(f.read())

        elif diet_exercise == 2:
            with open("pooja_exer.txt") as f:
                print(f.read())


