import PySimpleGUI as sg
sg.theme('LightGrey3')

class User:
    accounts = {}
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def add_user(self):
        if self.username not in self.accounts:
            usersfile = open("accounts.txt", "a")
            usersfile.write(f"{self.username}:{self.password}\n")
            usersfile.close()
            self.accounts[self.username] = self.password
        else:
            return 1
        
    def display(self):
        print(self.accounts)

    def create_recipe(self,type,name,ingredients,nutritional_inst,cooking_time,preparation_inst):
        self.type = type
        self.name = name
        self.ingredients = ingredients
        self.nutritional_inst = nutritional_inst
        self.cooking_time = cooking_time
        self.preparation_inst = preparation_inst
        self.calories = nutritional_inst[0]
        self.fats = nutritional_inst[1]
        self.proteins = nutritional_inst[2]
        self.carbohydrates = nutritional_inst[3]
        self.ingredients = Ingredients(ingredients)
        self.nutritional_inst  = Nutrition(self.calories,self.fats,self.proteins,self.carbohydrates)
        if self.type == "Baking":
            self.recipeobj = Baking(self.name,self.cooking_time,self.preparation_inst)
            try:
                with open("accounts.txt", "r") as file:
                    lines = file.readlines()
                    content = f"{Recipe.recipe}-{Ingredients.ingredients}-{Nutrition.nutritional_inst}"
                    count = 0
                    print(lines)
                    for account in lines:
                        account = account.strip()
                        account = account.split(":")
                        if len(account) < 3:
                            s_username, s_password = account
                            if s_username == self.username:
                                useline = lines[count]
                                useline = useline.strip()
                                lines[count] = useline
                                lines[count] += f':{content}\n'
                            count += 1
                        else:
                            s_username, s_password, recipies = account
                            if s_username == self.username:
                                useline = lines[count]
                                useline = useline.strip()
                                lines[count] = useline
                                lines[count] = f'{self.username}:{self.password}:{content}\n'
                            count += 1
            except:
                pass
            try:
                with open("accounts.txt", "w") as file:
                    for line in lines:
                        file.write(line)
            except:
                pass
        elif self.type == "Mixing":
            self.recipeobj = Mixing(self.name,self.cooking_time,self.preparation_inst)
            try:
                with open("accounts.txt", "r") as file:
                    lines = file.readlines()
                    content = f"{Recipe.recipe}-{Ingredients.ingredients}-{Nutrition.nutritional_inst}"
                    count = 0
                    for account in lines:
                        account = account.strip()
                        account = account.split(":")
                        if len(account) < 3:
                            s_username, s_password = account
                            if s_username == self.username:
                                useline = lines[count]
                                useline = useline.strip()
                                lines[count] = useline
                                lines[count] += f':{content}\n'
                            count += 1
                        else:
                            s_username, s_password, recipies = account
                            if s_username == self.username:
                                useline = lines[count]
                                useline = useline.strip()
                                lines[count] = useline
                                lines[count] = f'{self.username}:{self.password}:{content}\n'
                            count += 1
            except:
                pass
            try:
                with open("accounts.txt", "w") as file:
                    for line in lines:
                        file.write(line)
            except:
                pass
        elif self.type == "Stove":
            self.recipeobj = Stove(self.name,self.cooking_time,self.preparation_inst)
            try:
                with open("accounts.txt", "r") as file:
                    lines = file.readlines()
                    content = f"{Recipe.recipe}-{Ingredients.ingredients}-{Nutrition.nutritional_inst}"
                    count = 0
                    for account in lines:
                        account = account.strip()
                        account = account.split(":")
                        if len(account) < 3:
                            s_username, s_password = account
                            if s_username == self.username:
                                useline = lines[count]
                                useline = useline.strip()
                                lines[count] = useline
                                lines[count] += f':{content}\n'
                            count += 1
                        else:
                            s_username, s_password, recipies = account
                            if s_username == self.username:
                                useline = lines[count]
                                useline = useline.strip()
                                lines[count] = useline
                                lines[count] = f'{self.username}:{self.password}:{content}\n'
                            count += 1
            except:
                pass
            try:
                with open("accounts.txt", "w") as file:
                    for line in lines:
                        file.write(line)
            except:
                pass
    
    def search_recipe(self,r_type,name):
        self.type = r_type
        self.name = name
        try:
            with open("accounts.txt", "r") as file:
                lines = file.readlines()
                count = 0
                for account in lines:
                    account = account.strip()
                    account = account.split(":")
                    if len(account) < 3:
                        s_username, s_password = account
                        if s_username == self.username:
                            useline = lines[count]
                            useline = useline.strip()
                            dishname = 0
                            cooking_time = 0
                            prepration_detail = 0
                            a_ingredients = 0
                            a_nutrition = 0
                            return dishname, cooking_time, prepration_detail, a_ingredients, a_nutrition
                        count += 1
                    else:
                        s_username, s_password, recipies = account
                        if s_username == self.username:
                            useline = lines[count]
                            useline = useline.strip()
                            useline = useline.split(":")
                            recipies_n = useline[2]
                            recipies_n = recipies_n.split("-")
                            recipe_details = recipies_n[0]
                            recipe_ingredients = recipies_n[1]
                            recipe_nutrition = recipies_n[2]
                            recipe_details = eval(recipe_details)
                            recipe_ingredients = eval(recipe_ingredients)
                            recipe_nutrition = eval(recipe_nutrition)
                            count1 = 0
                            for a_recipe in recipe_details:
                                if a_recipe[0] == r_type:
                                    if a_recipe[1] == name:
                                        dishname = a_recipe[1]
                                        cooking_time = a_recipe[2]
                                        prepration_detail = a_recipe[3]
                                        check = "positive"
                                        count2 = count1
                                count1 += 1
                            a_ingredients = recipe_ingredients[count2]
                            a_nutrition = recipe_nutrition[count2]
                            if check == "positive":
                                return dishname, cooking_time, prepration_detail, a_ingredients, a_nutrition
                            else:
                                dishname = 0
                                cooking_time = 0
                                prepration_detail = 0
                                a_ingredients = 0
                                a_nutrition = 0
                                return dishname, cooking_time, prepration_detail, a_ingredients, a_nutrition
                        count += 1
                        
        except:
            dishname = 0
            cooking_time = 0
            prepration_detail = 0
            a_ingredients = 0
            a_nutrition = 0
            return dishname, cooking_time, prepration_detail, a_ingredients, a_nutrition
    
    def delete_recipe(self,r_type,name):
        self.type = r_type
        self.name = name

        count_0 = 0
        for aa_recipe in Recipe.recipe:
            if aa_recipe[0] == self.type and aa_recipe[1] == self.name:
                del Recipe.recipe[count_0]
                del Ingredients.ingredients[count_0]
                del Nutrition.nutritional_inst[count_0]
                print("deleted from class list")
                print(Recipe.recipe)
                print(Ingredients.ingredients)
                print(Nutrition.nutritional_inst)
            count_0 += 1

        try:
            with open("accounts.txt", "r") as file:
                lines = file.readlines()
                count = 0
                for account in lines:
                    account = account.strip()
                    account = account.split(":")
                    if len(account) < 3:
                        s_username, s_password = account
                        if s_username == self.username:
                            useline = lines[count]
                            useline = useline.strip()
                            dishname = 0
                            return dishname
                    else:
                        s_username, s_password, recipies = account
                        if s_username == self.username:
                            useline = lines[count]
                            useline = useline.strip()
                            useline = useline.split(":")
                            recipies_n = useline[2]
                            recipies_n = recipies_n.split("-")
                            recipe_details = recipies_n[0]
                            recipe_ingredients = recipies_n[1]
                            recipe_nutrition = recipies_n[2]
                            recipe_details = eval(recipe_details)
                            recipe_ingredients = eval(recipe_ingredients)
                            recipe_nutrition = eval(recipe_nutrition)
                            count1 = 0
                            check = ""
                            for a_recipe in recipe_details:
                                if (r_type in a_recipe) and (name in a_recipe):
                                    del recipe_details[count1]
                                    del recipe_ingredients[count1]
                                    del recipe_nutrition[count1]
                                    check = "positive"
                                count1 += 1 
                            if check != "positive":
                                dishname = 0
                                return dishname 
                    count += 1

        except:
            dishname = 0
            return dishname
        try:
            with open("accounts.txt", "r") as file:
                lines = file.readlines()
                content = f"{recipe_details}-{recipe_ingredients}-{recipe_nutrition}"
                count = 0
                for account in lines:
                    account = account.strip()
                    account = account.split(":")
                    if len(account) < 3:
                        s_username, s_password = account
                        if s_username == self.username:
                            useline = lines[count]
                            useline = useline.strip()
                            lines[count] = useline
                            lines[count] += f':{content}\n'
                        count += 1
                    else:
                        s_username, s_password, recipies = account
                        if s_username == self.username:
                            useline = lines[count]
                            useline = useline.strip()
                            lines[count] = useline
                            lines[count] = f'{self.username}:{self.password}:{content}\n'
                        count += 1
        except:
            pass
        try:
            with open("accounts.txt", "w") as file:
                for line in lines:
                    file.write(line)
        except:
            pass

    def edit_recipe_part1(self,r_type,name):
        self.type = r_type
        self.name = name

        try:
            with open("accounts.txt", "r") as file:
                lines = file.readlines()
                count = 0
                for account in lines:
                    account = account.strip()
                    account = account.split(":")
                    if len(account) < 3:
                        s_username, s_password = account
                        if s_username == self.username:
                            useline = lines[count]
                            useline = useline.strip()
                            dishname = 0
                            return dishname
                    else:
                        s_username, s_password, recipies = account
                        if s_username == self.username:
                            useline = lines[count]
                            useline = useline.strip()
                            useline = useline.split(":")
                            recipies_n = useline[2]
                            recipies_n = recipies_n.split("-")
                            recipe_details = recipies_n[0]
                            recipe_ingredients = recipies_n[1]
                            recipe_nutrition = recipies_n[2]
                            recipe_details = eval(recipe_details)
                            recipe_ingredients = eval(recipe_ingredients)
                            recipe_nutrition = eval(recipe_nutrition)
                            count1 = 0
                            check = ""
                            for a_recipe in recipe_details:
                                if (r_type in a_recipe) and (name in a_recipe):
                                    check = "positive"
                                    self.recipe_details = recipe_details
                                    self.recipe_ingredients = recipe_ingredients
                                    self.recipe_nutrition = recipe_nutrition
                                    self.count1 = count1
                                count1 += 1 
                            if check != "positive":
                                dishname = 0
                                return dishname 
                    count += 1                                  
        except:
            dishname = 0
            return dishname

    def edit_ingredients(self,ingredients):
        self.recipe_ingredients[self.count1] = ingredients
        try:
            with open("accounts.txt", "r") as file:
                lines = file.readlines()
                content = f"{self.recipe_details}-{self.recipe_ingredients}-{self.recipe_nutrition}"
                count = 0
                for account in lines:
                    account = account.strip()
                    account = account.split(":")
                    if len(account) < 3:
                        s_username, s_password = account
                        if s_username == self.username:
                            useline = lines[count]
                            useline = useline.strip()
                            lines[count] = useline
                            lines[count] += f':{content}\n'
                        count += 1
                    else:
                        s_username, s_password, recipies = account
                        if s_username == self.username:
                            useline = lines[count]
                            useline = useline.strip()
                            lines[count] = useline
                            lines[count] = f'{self.username}:{self.password}:{content}\n'
                        count += 1
        except:
            pass
        try:
            with open("accounts.txt", "w") as file:
                for line in lines:
                    file.write(line)
        except:
            pass

    def edit_nutrition(self,nutritional_inst):
        self.recipe_nutrition[self.count1] = list(nutritional_inst)
        try:
            with open("accounts.txt", "r") as file:
                lines = file.readlines()
                content = f"{self.recipe_details}-{self.recipe_ingredients}-{self.recipe_nutrition}"
                count = 0
                for account in lines:
                    account = account.strip()
                    account = account.split(":")
                    if len(account) < 3:
                        s_username, s_password = account
                        if s_username == self.username:
                            useline = lines[count]
                            useline = useline.strip()
                            lines[count] = useline
                            lines[count] += f':{content}\n'
                        count += 1
                    else:
                        s_username, s_password, recipies = account
                        if s_username == self.username:
                            useline = lines[count]
                            useline = useline.strip()
                            lines[count] = useline
                            lines[count] = f'{self.username}:{self.password}:{content}\n'
                        count += 1
        except:
            pass
        try:
            with open("accounts.txt", "w") as file:
                for line in lines:
                    file.write(line)
        except:
            pass

    def edit_cookingtime_preprationinst(self,cooking_time,prepration_inst):
        self.recipe_details[self.count1] = [self.type,self.name,cooking_time,prepration_inst]
        try:
            with open("accounts.txt", "r") as file:
                lines = file.readlines()
                content = f"{self.recipe_details}-{self.recipe_ingredients}-{self.recipe_nutrition}"
                count = 0
                for account in lines:
                    account = account.strip()
                    account = account.split(":")
                    if len(account) < 3:
                        s_username, s_password = account
                        if s_username == self.username:
                            useline = lines[count]
                            useline = useline.strip()
                            lines[count] = useline
                            lines[count] += f':{content}\n'
                        count += 1
                    else:
                        s_username, s_password, recipies = account
                        if s_username == self.username:
                            useline = lines[count]
                            useline = useline.strip()
                            lines[count] = useline
                            lines[count] = f'{self.username}:{self.password}:{content}\n'
                        count += 1
        except:
            pass
        try:
            with open("accounts.txt", "w") as file:
                for line in lines:
                    file.write(line)
        except:
            pass

class Recipe:
    recipe = []
    def __init__(self,name):
        self.name = name
        self.ingredients = Ingredients.ingredients
        self.nutritional_inst = Nutrition.nutritional_inst

class Baking(Recipe):
    recipe_b = []
    def __init__(self,name,cooking_time,preparation_inst):
        super().__init__(name)
        self.cooking_time = cooking_time
        self.preparation_inst = preparation_inst
        self.recipe_b.append(["Baking",name,cooking_time,preparation_inst])
        Recipe.recipe.append(["Baking",name,cooking_time,preparation_inst])
        
class Mixing(Recipe):
    recipe_m = []
    def __init__(self,name,cooking_time,preparation_inst):
        super().__init__(name)
        self.cooking_time = cooking_time
        self.preparation_inst = preparation_inst
        self.recipe_m.append(["Mixing",name,cooking_time,preparation_inst])
        Recipe.recipe.append(["Mixing",name,cooking_time,preparation_inst])

class Stove(Recipe):
    recipe_s = []
    def __init__(self,name,cooking_time,preparation_inst):
        super().__init__(name)
        self.cooking_time = cooking_time
        self.preparation_inst = preparation_inst
        self.recipe_s.append(["Stove",name,cooking_time,preparation_inst])
        Recipe.recipe.append(["Stove",name,cooking_time,preparation_inst])

class Nutrition:
    nutritional_inst = []
    def __init__(self,calories,fats,proteins,carbohydrates):
        self.calories = calories
        self.fats = fats
        self.proteins = proteins
        self.carbohydrates = carbohydrates
        self.nutritional_inst.append([calories,fats,proteins,carbohydrates])

class Ingredients:
    ingredients = []
    def __init__(self,names):
        self.names = names
        self.ingredients.append(names)

def initial_interface():
    try:
        with open("accounts.txt", "r") as file:
            lines = file.readlines()
            for account in lines:
                account = account.strip()
                account = account.split(":")
                if len(account) < 3:
                    s_username, s_password = account
                    User.accounts[s_username] = s_password
                else:
                    s_username, s_password, recipies = account
                    User.accounts[s_username] = s_password
    except:
        pass

    layout = [
        [sg.Text("Recipe Management System", size=(30,1), font=("Harrington 50 italic"))],
        [sg.Text("Username:", size=(40,1), font=("Helvetica", 15))],
        [sg.Input(key = "Username", size=(40,1), font=("Helvetica", 15))],
        [sg.Text("Password:", size=(40,1), font=("Helvetica", 15))],
        [sg.Input(key = "Password", size=(40,1), font=("Helvetica", 15), password_char='*')],
        [sg.Button("Login", size=(10, 1), font=("Helvetica", 15))],
        [sg.Button("Register", size=(10, 1), font=("Helvetica", 15))],
        [sg.Button("Exit", size=(10, 1), font=("Helvetica", 15))]
    ]
    window = sg.Window("Recipe Management System", layout , size = (900,500))
    while True:
        event, values = window.read()
        if event == "Register":
            window.hide()
            registration()
        elif event == "Login":
            global username
            global password
            username = values["Username"]
            username = username.strip()
            password = values["Password"]
            password = password.strip()
            if username != "" and password != "":
                if username in User.accounts:
                    original_password = User.accounts[username]
                if username in User.accounts and password == original_password:
                    global userobj
                    userobj = User(username,password)
                    window.hide()
                    menu()
                else:
                    window.hide()
                    layout = [
                        [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
                        [sg.Text("Credentials doesn't match", size=(40,1), font=("Helvetica", 15))],
                        [sg.Button("Back", size=(10, 1), font=("Helvetica", 15))],
                        [sg.Button("Exit", size=(10, 1), font=("Helvetica", 15))]
                    ]
                    window = sg.Window("Recipe Management System", layout , size = (900,500))            
                    while True:
                        event, values = window.read()
                        if event == "Back":
                            window.hide()
                            initial_interface()
                        elif event == "Exit" or event == sg.WIN_CLOSED:
                            break
                    window.close()
        elif event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

def registration():
    layout = [
        [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
        [sg.Text("Create Username:", size=(40,1), font=("Helvetica", 15))],
        [sg.Input(key = "Username", size=(40,1), font=("Helvetica", 15))],
        [sg.Text("Create Password (atleast 5 characters):", size=(40,1), font=("Helvetica", 15))],
        [sg.Input(key = "Password", size=(40,1), font=("Helvetica", 15), password_char='*')],
        [sg.Button("Register", size=(10, 1), font=("Helvetica", 15))],
        [sg.Button("Exit", size=(10, 1), font=("Helvetica", 15))]
    ]
    window = sg.Window("Recipe Management System", layout , size = (900,500))
    while True:
        event, values = window.read()
        if event == "Register":
            username = values["Username"]
            username = username.strip()
            password = values["Password"]
            password = password.strip()
            if username != "" and password != "" and len(password)>4:
                global userobj
                userobj = User(username, password)
                check = userobj.add_user()
                userobj.display()
                if check == 1:
                    window.hide()
                    layout = [
                        [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
                        [sg.Text("Username already exists", size=(40,1), font=("Helvetica", 15))],
                        [sg.Button("Back", size=(10, 1), font=("Helvetica", 15))],
                        [sg.Button("Exit", size=(10, 1), font=("Helvetica", 15))]
                    ]
                    window = sg.Window("Recipe Management System", layout , size = (900,500))
                    while True:
                        event, values = window.read()
                        if event == "Back":
                            window.hide()
                            registration()
                        elif event == "Exit" or event == sg.WIN_CLOSED:
                            break
                    window.close()
                else:
                    window.hide()
                    layout = [
                        [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
                        [sg.Text("Account Created Sucessfully", size=(40,1), font=("Helvetica", 15))],
                        [sg.Button("Return to Login Page", size=(20, 1), font=("Helvetica", 15))],
                        [sg.Button("Exit", size=(10, 1), font=("Helvetica", 15))]
                    ]
                    window = sg.Window("Recipe Management System", layout , size = (900,500))
                    while True:
                        event, values = window.read()
                        if event == "Return to Login Page":
                            window.hide()
                            initial_interface()
                        elif event == "Exit" or event == sg.WIN_CLOSED:
                            break
                    window.close()
        elif event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

def menu():
    userobj = User(username,password)
    layout = [
        [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
        [sg.Button("Create Recipe", size=(15, 1), font=("Helvetica", 15))],
        [sg.Button("Delete Recipe", size=(15, 1), font=("Helvetica", 15))],
        [sg.Button("Edit Recipe", size=(15, 1), font=("Helvetica", 15))],
        [sg.Button("Search for a Recipe", size=(20, 1), font=("Helvetica", 15))],
        [sg.Button("Log Out", size=(15, 1), font=("Helvetica", 15))],
        [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
    ]
    window = sg.Window("Recipe Management System", layout , size = (900,500))
    while True:
        event, values = window.read()
        if event == "Create Recipe":
            window.hide()
            create_recipe()
        elif event == "Search for a Recipe":
            window.hide()
            search_recipe()
        elif event == "Delete Recipe":
            window.hide()
            delete_recipe()
        elif event == "Edit Recipe":
            window.hide()
            edit_recipe()
        elif event == "Log Out":
            window.hide()
            Recipe.recipe = []
            Baking.recipe_b = []
            Mixing.recipe_m = []
            Stove.recipe_s = []
            Ingredients.ingredients = []
            Nutrition.nutritional_inst = []
            initial_interface()
        elif event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

def create_recipe():
    layout = [
        [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
        [sg.Text("Enter dish name: ", size=(40,1), font=("Helvetica", 15))],
        [sg.Input(key = "Name", size=(40,1), font=("Helvetica", 15))],
        [sg.Text("Choose Recipe Type: ", size=(40,1), font=("Helvetica", 15))],
        [sg.Radio("Baking", 1, key = "baking", default= True), sg.Radio("Mixing", 1, key = "mixing"), sg.Radio("Stove", 1, key = "stove")],
        [sg.Button("Submit", size=(15, 1), font=("Helvetica", 15))],
        [sg.Button("Back", size=(15, 1), font=("Helvetica", 15))],
        [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
    ]
    window = sg.Window("Recipe Management System", layout , size = (900,500))
    while True:
        event, values = window.read()
        if event == "Submit":
            dish_name = values["Name"]
            dish_name = dish_name.strip()
            if values["baking"] == True:
                recipe_type = "Baking"
            elif values["mixing"] == True:
                recipe_type = "Mixing"
            elif values["stove"] == True:
                recipe_type = "Stove"
            if dish_name != "":
                window.hide()
                layout = [
                    [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
                    [sg.Text("Enter ingredients: ", size=(40,1), font=("Helvetica", 15))],
                    [sg.Input(key = "Ingredient1", size=(40,1), font=("Helvetica", 15))],
                    [sg.Input(key = "Ingredient2", size=(40,1), font=("Helvetica", 15))],
                    [sg.Input(key = "Ingredient3", size=(40,1), font=("Helvetica", 15))],
                    [sg.Input(key = "Ingredient4", size=(40,1), font=("Helvetica", 15))],
                    [sg.Input(key = "Ingredient5", size=(40,1), font=("Helvetica", 15))],
                    [sg.Input(key = "Ingredient6", size=(40,1), font=("Helvetica", 15))],
                    [sg.Input(key = "Ingredient7", size=(40,1), font=("Helvetica", 15))],
                    [sg.Input(key = "Ingredient8", size=(40,1), font=("Helvetica", 15))],
                    [sg.Input(key = "Ingredient9", size=(40,1), font=("Helvetica", 15))],
                    [sg.Input(key = "Ingredient10", size=(40,1), font=("Helvetica", 15))],
                    [sg.Button("Submit", size=(15, 1), font=("Helvetica", 15))],
                    [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
                ]
                window = sg.Window("Recipe Management System", layout , size = (900,500))
                while True:
                    event, values = window.read()
                    if event == "Submit":
                        ingredient1 = values["Ingredient1"]
                        ingredient2 = values["Ingredient2"]
                        ingredient3 = values["Ingredient3"]
                        ingredient4 = values["Ingredient4"]
                        ingredient5 = values["Ingredient5"]
                        ingredient6 = values["Ingredient6"]
                        ingredient7 = values["Ingredient7"]
                        ingredient8 = values["Ingredient8"]
                        ingredient9 = values["Ingredient9"]
                        ingredient10 = values["Ingredient10"]
                        ingredients = [ingredient1,ingredient2,ingredient3,ingredient4,ingredient5,ingredient6,ingredient7,ingredient8,ingredient9,ingredient10]
                        count = 0
                        rangee = 10
                        for i in range(rangee):
                            if ingredients[count] == "":
                                del ingredients[count]
                            else:
                                count += 1
                        window.hide()
                        layout = [
                            [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
                            [sg.Text("Enter Nutritional Instructions(in grams): ", size=(40,1), font=("Helvetica", 20))],
                            [sg.Text("Calories: ", size=(40,1), font=("Helvetica", 15))],
                            [sg.Input(key = "Calories", size=(40,1), font=("Helvetica", 15))],
                            [sg.Text("Fats: ", size=(40,1), font=("Helvetica", 15))],
                            [sg.Input(key = "Fats", size=(40,1), font=("Helvetica", 15))],
                            [sg.Text("Proteins: ", size=(40,1), font=("Helvetica", 15))],
                            [sg.Input(key = "Proteins", size=(40,1), font=("Helvetica", 15))],
                            [sg.Text("Carbohydrates: ", size=(40,1), font=("Helvetica", 15))],
                            [sg.Input(key = "Carbohydrates", size=(40,1), font=("Helvetica", 15))],
                            [sg.Button("Submit", size=(15, 1), font=("Helvetica", 15))],
                            [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
                        ]
                        window = sg.Window("Recipe Management System", layout , size = (900,500))
                        while True:
                            event, values = window.read()
                            if event == "Submit":
                                calories = values["Calories"]
                                calories = calories.strip()
                                fats = values["Fats"]
                                fats = fats.strip()
                                proteins = values["Proteins"]
                                proteins = proteins.strip()
                                carbohydrates = values["Carbohydrates"]
                                carbohydrates = carbohydrates.strip()
                                if calories != "" and fats != "" and proteins != "" and carbohydrates != "":
                                    nutritional_inst = calories,fats,proteins,carbohydrates
                                    window.hide()
                                    layout = [
                                        [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
                                        [sg.Text("Enter Cooking time (in minutes): ", size=(40,1), font=("Helvetica", 15))],
                                        [sg.Input(key = "Cooking_time", size=(40,1), font=("Helvetica", 15))],
                                        [sg.Text("Enter Prepration Instructions: ", size=(40,1), font=("Helvetica", 15))],
                                        [sg.Input(key = "Prepration_Instructions", size=(40,5), font=("Helvetica", 15))],
                                        [sg.Button("Submit", size=(15, 1), font=("Helvetica", 15))],
                                        [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
                                    ]
                                    window = sg.Window("Recipe Management System", layout , size = (900,500))
                                    while True:
                                        event, values = window.read()
                                        if event == "Submit":
                                            cooking_time = values["Cooking_time"]
                                            cooking_time = cooking_time.strip()
                                            prepration_inst = values["Prepration_Instructions"] 
                                            prepration_inst = prepration_inst.strip()
                                            if cooking_time != "" and prepration_inst != "":
                                                userobj.create_recipe(recipe_type,dish_name,ingredients,nutritional_inst,cooking_time,prepration_inst)
                                                window.hide()
                                                layout = [
                                                    [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
                                                    [sg.Text("Recipe added sucessfully: ", size=(40,1), font=("Helvetica", 15))],
                                                    [sg.Button("Main Menu", size=(15, 1), font=("Helvetica", 15))],
                                                    [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
                                                ]
                                                window = sg.Window("Recipe Management System", layout , size = (900,500))
                                        
                                                while True:
                                                    event, values = window.read()
                                                    if event == "Main Menu":
                                                        window.hide()
                                                        menu()
                                                    elif event == "Exit" or event == sg.WIN_CLOSED:
                                                        break
                                                window.close()
                                        elif event == "Exit" or event == sg.WIN_CLOSED:
                                            break
                                    window.close()
                            elif event == "Exit" or event == sg.WIN_CLOSED:
                                break
                        window.close()
                    elif event == "Exit" or event == sg.WIN_CLOSED:
                        break
                window.close()
        elif event == "Back":
            window.hide()
            menu()
        elif event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

def search_recipe():
    layout = [
        [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
        [sg.Text("Search for recipe", size=(40,1), font=("Helvetica", 15))],
        [sg.Radio("Baking", 1, key = "baking", default= True), sg.Radio("Mixing", 1, key = "mixing"), sg.Radio("Stove", 1, key = "stove")],
        [sg.Text("Enter dish name: ", size=(40,1), font=("Helvetica", 15))],
        [sg.Input(key = "Name", size=(40,1), font=("Helvetica", 15))],
        [sg.Button("Submit", size=(15, 1), font=("Helvetica", 15))],
        [sg.Button("Back", size=(15, 1), font=("Helvetica", 15))],
        [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
    ]
    window = sg.Window("Recipe Management System", layout , size = (900,500))
    while True:
        event, values = window.read()
        if event == "Submit":
            dish_name = values["Name"]
            dish_name = dish_name.strip()
            print(dish_name)
            if values["baking"] == True:
                recipe_type = "Baking"
            elif values["mixing"] == True:
                recipe_type = "Mixing"
            elif values["stove"] == True:
                recipe_type = "Stove"
            if dish_name != "":
                dishname, cooking_time, prepration_detail, a_ingredients, a_nutrition = userobj.search_recipe(recipe_type,dish_name)
                if dishname == 0:
                    window.hide()
                    layout = [
                        [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
                        [sg.Text("Such Recipe does not exist", size=(40,1), font=("Helvetica", 15))],
                        [sg.Button("Back", size=(15, 1), font=("Helvetica", 15))],
                        [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
                    ]
                    window = sg.Window("Recipe Management System", layout , size = (900,500))
                    while True:
                        event, values = window.read()
                        if event == "Back":
                            window.hide()
                            search_recipe()
                        elif event == "Exit" or event == sg.WIN_CLOSED:
                            break
                    window.close()
                else:
                    a_ingredients = ",".join(a_ingredients)
                    calories = a_nutrition[0]
                    fats = a_nutrition[1]
                    proteins = a_nutrition[2]
                    carbohydrates = a_nutrition[3]
                    window.hide()
                    layout = [
                        [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
                        [sg.Text(f"Dish name: {dishname}", size=(40,1), font=("Helvetica", 20))],
                        [sg.Text(f"Cooking Time: {cooking_time}", size=(40,1), font=("Helvetica", 13))],
                        [sg.Text(f"Ingredients: {a_ingredients}", font=("Helvetica", 13))],
                        [sg.Text(f"Nutrition:", size=(40,1), font=("Helvetica", 13))],
                        [sg.Text(f"Calories: {calories}, Fats: {fats}, Proteins: {proteins}, Carbohydrates: {carbohydrates}", font=("Helvetica", 10))],
                        [sg.Text(f"Prepration Instructions:", size=(40,1), font=("Helvetica", 13))],
                        [sg.Text(f"{prepration_detail}", font=("Helvetica", 10))],
                        [sg.Button("Main Menu", size=(15, 1), font=("Helvetica", 15))],
                        [sg.Button("Back", size=(15, 1), font=("Helvetica", 15))],
                        [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
                    ]
                    window = sg.Window("Recipe Management System", layout , size = (900,500))
                    while True:
                        event, values = window.read()
                        if event == "Main Menu":
                            window.hide()
                            menu()
                        elif event == "Back":
                            window.hide()
                            search_recipe()
                        elif event == "Exit" or event == sg.WIN_CLOSED:
                            break
                    window.close()
        elif event == "Back":
            window.hide()
            menu()
        elif event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

def delete_recipe():
    layout = [
        [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
        [sg.Text("Delete Recipe", size=(40,1), font=("Helvetica", 15))],
        [sg.Radio("Baking", 1, key = "baking", default= True), sg.Radio("Mixing", 1, key = "mixing"), sg.Radio("Stove", 1, key = "stove")],
        [sg.Text("Enter dish name you want to delete: ", size=(40,1), font=("Helvetica", 15))],
        [sg.Input(key = "Name", size=(40,1), font=("Helvetica", 15))],
        [sg.Button("Submit", size=(15, 1), font=("Helvetica", 15))],
        [sg.Button("Back", size=(15, 1), font=("Helvetica", 15))],
        [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
    ]
    window = sg.Window("Recipe Management System", layout , size = (900,500))
    while True:
        event, values = window.read()
        if event == "Submit":
            dish_name = values["Name"]
            dish_name = dish_name.strip()
            if values["baking"] == True:
                recipe_type = "Baking"
            elif values["mixing"] == True:
                recipe_type = "Mixing"
            elif values["stove"] == True:
                recipe_type = "Stove"
            if dish_name != "":
                answer = userobj.delete_recipe(recipe_type,dish_name)
                window.hide()
                if answer == 0:
                    layout = [
                        [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
                        [sg.Text("Such Recipe does not exist", size=(40,1), font=("Helvetica", 15))],
                        [sg.Button("Main Menu", size=(15, 1), font=("Helvetica", 15))],
                        [sg.Button("Back", size=(15, 1), font=("Helvetica", 15))],
                        [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
                    ]
                    window = sg.Window("Recipe Management System", layout , size = (900,500))
                    while True:
                        event, values = window.read()
                        if event == "Main Menu":
                            window.hide()
                            menu()
                        elif event == "Back":
                            window.hide()
                            delete_recipe()
                        elif event == "Exit" or sg.WIN_CLOSED:
                            break
                    window.close()
                else:
                    layout = [
                        [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
                        [sg.Text("Recipe Deleted Sucessfully", size=(40,1), font=("Helvetica", 15))],
                        [sg.Button("Main Menu", size=(15, 1), font=("Helvetica", 15))],
                        [sg.Button("Back", size=(15, 1), font=("Helvetica", 15))],
                        [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
                    ]
                    window = sg.Window("Recipe Management System", layout , size = (900,500))
                    while True:
                        event, values = window.read()
                        if event == "Main Menu":
                            window.hide()
                            menu()
                        elif event == "Back":
                            window.hide()
                            delete_recipe()
                        elif event == "Exit" or sg.WIN_CLOSED:
                            break
                    window.close()
        elif event == "Back":
            window.hide()
            menu()
        elif event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

def edit_recipe():
    layout = [
        [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
        [sg.Text("Delete Recipe", size=(40,1), font=("Helvetica", 15))],
        [sg.Radio("Baking", 1, key = "baking", default= True), sg.Radio("Mixing", 1, key = "mixing"), sg.Radio("Stove", 1, key = "stove")],
        [sg.Text("Enter dish name you want to edit: ", size=(40,1), font=("Helvetica", 15))],
        [sg.Input(key = "Name", size=(40,1), font=("Helvetica", 15))],
        [sg.Button("Submit", size=(15, 1), font=("Helvetica", 15))],
        [sg.Button("Back", size=(15, 1), font=("Helvetica", 15))],
        [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
    ]
    window = sg.Window("Recipe Management System", layout , size = (900,500))
    while True:
        event, values = window.read()
        if event == "Submit":
            dish_name = values["Name"]
            dish_name = dish_name.strip()
            if values["baking"] == True:
                recipe_type = "Baking"
            elif values["mixing"] == True:
                recipe_type = "Mixing"
            elif values["stove"] == True:
                recipe_type = "Stove"
            if dish_name != "":
                answer = userobj.edit_recipe_part1(recipe_type,dish_name)
                window.hide()
                if answer == 0:
                    layout = [
                        [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
                        [sg.Text("Such Recipe does not exist", size=(40,1), font=("Helvetica", 15))],
                        [sg.Button("Main Menu", size=(15, 1), font=("Helvetica", 15))],
                        [sg.Button("Back", size=(15, 1), font=("Helvetica", 15))],
                        [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
                    ]
                    window = sg.Window("Recipe Management System", layout , size = (900,500))
                    while True:
                        event, values = window.read()
                        if event == "Main Menu":
                            window.hide()
                            menu()
                        elif event == "Back":
                            window.hide()
                            edit_recipe()
                        elif event == "Exit" or sg.WIN_CLOSED:
                            break
                    window.close()
                else:
                    window.hide()
                    layout = [
                        [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
                        [sg.Text("Select what you want to edit:", size=(40,1), font=("Helvetica", 15))],
                        [sg.Button("Ingredients", size=(20, 1), font=("Helvetica", 15))],
                        [sg.Button("Nutritional Instructions", size=(20, 1), font=("Helvetica", 15))],
                        [sg.Button("Cooking Time & Prepration Instruction", size=(40, 1), font=("Helvetica", 15))],
                        [sg.Button("Back", size=(15, 1), font=("Helvetica", 15))],
                        [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
                    ]
                    window = sg.Window("Recipe Management System", layout , size = (900,500))
                    while True:
                        event, values = window.read()
                        if event == "Ingredients":
                            window.hide()
                            layout = [
                                [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
                                [sg.Text("Enter ingredients: ", size=(40,1), font=("Helvetica", 15))],
                                [sg.Input(key = "Ingredient1", size=(40,1), font=("Helvetica", 15))],
                                [sg.Input(key = "Ingredient2", size=(40,1), font=("Helvetica", 15))],
                                [sg.Input(key = "Ingredient3", size=(40,1), font=("Helvetica", 15))],
                                [sg.Input(key = "Ingredient4", size=(40,1), font=("Helvetica", 15))],
                                [sg.Input(key = "Ingredient5", size=(40,1), font=("Helvetica", 15))],
                                [sg.Input(key = "Ingredient6", size=(40,1), font=("Helvetica", 15))],
                                [sg.Input(key = "Ingredient7", size=(40,1), font=("Helvetica", 15))],
                                [sg.Input(key = "Ingredient8", size=(40,1), font=("Helvetica", 15))],
                                [sg.Input(key = "Ingredient9", size=(40,1), font=("Helvetica", 15))],
                                [sg.Input(key = "Ingredient10", size=(40,1), font=("Helvetica", 15))],
                                [sg.Button("Submit", size=(15, 1), font=("Helvetica", 15))],
                                [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
                            ]
                            window = sg.Window("Recipe Management System", layout , size = (900,500))
                            while True:
                                event, values = window.read()
                                if event == "Submit":
                                    ingredient1 = values["Ingredient1"]
                                    ingredient2 = values["Ingredient2"]
                                    ingredient3 = values["Ingredient3"]
                                    ingredient4 = values["Ingredient4"]
                                    ingredient5 = values["Ingredient5"]
                                    ingredient6 = values["Ingredient6"]
                                    ingredient7 = values["Ingredient7"]
                                    ingredient8 = values["Ingredient8"]
                                    ingredient9 = values["Ingredient9"]
                                    ingredient10 = values["Ingredient10"]
                                    ingredients = [ingredient1,ingredient2,ingredient3,ingredient4,ingredient5,ingredient6,ingredient7,ingredient8,ingredient9,ingredient10]
                                    count = 0
                                    rangee = 10
                                    for i in range(rangee):
                                        if ingredients[count] == "":
                                            del ingredients[count]
                                        else:
                                            count += 1
                                    userobj.edit_ingredients(ingredients)
                                    window.hide()
                                    layout = [
                                        [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
                                        [sg.Text("Ingredients sucessfully edited.", size=(40,1), font=("Helvetica", 15))],
                                        [sg.Button("Main Menu", size=(15, 1), font=("Helvetica", 15))],
                                        [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
                                    ]
                                    window = sg.Window("Recipe Management System", layout , size = (900,500))
                                    while True:
                                        event, values = window.read()
                                        if event == "Main Menu":
                                            window.hide()
                                            menu()
                                        elif event == "Exit" or sg.WIN_CLOSED:
                                            break
                                    window.close()
                                elif event == "Exit" or event == sg.WIN_CLOSED:
                                    break
                            window.close()            
                        elif event == "Nutritional Instructions":
                            window.hide()
                            layout = [
                                [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
                                [sg.Text("Enter Nutritional Instructions(in grams): ", size=(40,1), font=("Helvetica", 20))],
                                [sg.Text("Calories: ", size=(40,1), font=("Helvetica", 15))],
                                [sg.Input(key = "Calories", size=(40,1), font=("Helvetica", 15))],
                                [sg.Text("Fats: ", size=(40,1), font=("Helvetica", 15))],
                                [sg.Input(key = "Fats", size=(40,1), font=("Helvetica", 15))],
                                [sg.Text("Proteins: ", size=(40,1), font=("Helvetica", 15))],
                                [sg.Input(key = "Proteins", size=(40,1), font=("Helvetica", 15))],
                                [sg.Text("Carbohydrates: ", size=(40,1), font=("Helvetica", 15))],
                                [sg.Input(key = "Carbohydrates", size=(40,1), font=("Helvetica", 15))],
                                [sg.Button("Submit", size=(15, 1), font=("Helvetica", 15))],
                                [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
                            ]
                            window = sg.Window("Recipe Management System", layout , size = (900,500))
                            while True:
                                event, values = window.read()
                                if event == "Submit":
                                    calories = values["Calories"]
                                    calories = calories.strip()
                                    fats = values["Fats"]
                                    fats = fats.strip()
                                    proteins = values["Proteins"]
                                    proteins = proteins.strip()
                                    carbohydrates = values["Carbohydrates"]
                                    carbohydrates = carbohydrates.strip()
                                    if calories != "" and fats != "" and proteins != "" and carbohydrates != "":
                                        nutritional_inst = calories,fats,proteins,carbohydrates
                                        userobj.edit_nutrition(nutritional_inst)
                                        window.hide()
                                        layout = [
                                            [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
                                            [sg.Text("Nutritional Instructions sucessfully edited.", font=("Helvetica", 15))],
                                            [sg.Button("Main Menu", size=(15, 1), font=("Helvetica", 15))],
                                            [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
                                        ]
                                        window = sg.Window("Recipe Management System", layout , size = (900,500))
                                        while True:
                                            event, values = window.read()
                                            if event == "Main Menu":
                                                window.hide()
                                                menu()
                                            elif event == "Exit" or event == sg.WIN_CLOSED:
                                                break
                                        window.close()
                                elif event == "Exit" or event == sg.WIN_CLOSED:
                                    break
                            window.close()
                        elif event == "Cooking Time & Prepration Instruction":
                            window.hide()
                            layout = [
                                [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
                                [sg.Text("Enter Cooking time (in minutes): ", size=(40,1), font=("Helvetica", 15))],
                                [sg.Input(key = "Cooking_time", size=(40,1), font=("Helvetica", 15))],
                                [sg.Text("Enter Prepration Instructions: ", size=(40,1), font=("Helvetica", 15))],
                                [sg.Input(key = "Prepration_Instructions", size=(40,5), font=("Helvetica", 15))],
                                [sg.Button("Submit", size=(15, 1), font=("Helvetica", 15))],
                                [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
                            ]
                            window = sg.Window("Recipe Management System", layout , size = (900,500))
                            while True:
                                event, values = window.read()
                                if event == "Submit":
                                    cooking_time = values["Cooking_time"]
                                    cooking_time = cooking_time.strip()
                                    prepration_inst = values["Prepration_Instructions"] 
                                    prepration_inst = prepration_inst.strip()
                                    if cooking_time != "" and prepration_inst != "":
                                        userobj.edit_cookingtime_preprationinst(cooking_time,prepration_inst)
                                        window.hide()
                                        layout = [
                                            [sg.Text("Recipe Management System", size=(30, 1), font=("Harrington 50 italic"))],
                                            [sg.Text("Cooking time & Prepration Instructions edited sucessfully.", font=("Helvetica", 15))],
                                            [sg.Button("Main Menu", size=(15, 1), font=("Helvetica", 15))],
                                            [sg.Button("Exit", size=(15, 1), font=("Helvetica", 15))]
                                        ]
                                        window = sg.Window("Recipe Management System", layout , size = (900,500))
                                        while True:
                                            event, values = window.read()
                                            if event == "Main Menu":
                                                window.hide()
                                                menu()
                                            elif event == "Exit" or event == sg.WIN_CLOSED:
                                                break
                                        window.close()
                                elif event == "Exit" or event == sg.WIN_CLOSED:
                                    break
                            window.close()        
                        elif event == "Main Menu":
                            window.hide()
                            menu()
                        elif event == "Back":
                            window.hide()
                            delete_recipe()
                        elif event == "Exit" or event == sg.WIN_CLOSED:
                            break
                    window.close()
        elif event == "Back":
            window.hide()
            menu()
        elif event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

initial_interface()
