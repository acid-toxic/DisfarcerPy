import faker
import json
import sys

print(r"""
  _____  _      __                        _____       
 |  __ \(_)    / _|                      |  __ \      
 | |  | |_ ___| |_ __ _ _ __ ___ ___ _ __| |__) |   _ 
 | |  | | / __|  _/ _` | '__/ __/ _ \ '__|  ___/ | | |
 | |__| | \__ \ || (_| | | | (_|  __/ |  | |   | |_| |
 |_____/|_|___/_| \__,_|_|  \___\___|_|  |_|    \__, |
                                                 __/ |
                                                |___/ 
                                                
                                                by acid'
""")
def fakeus():
    fake = faker.Faker("en_US") # Fake Data EUA
    name = fake.first_name()
    last_name = fake.last_name()
    username = f"{name.lower().replace(' ', '')}_{last_name.lower().replace(' ', '')}"
    password = fake.password(length=12, special_chars=True, digits=True)
    email = f"{name.lower()}.{last_name.lower().replace(' ', '')}@gmail.com"
    job = f"{fake.job()}"
    date_birth = f"{fake.date_of_birth(minimum_age=18)}"
    ssn = f"{fake.ssn()}"
    address = f"{fake.address().replace('\n', ' ')}"
    user_agent = f"{fake.user_agent()}"
    phone = f"{fake.phone_number()}"

    return {
        "name": name,
        "last_name": last_name,
        "username": username,
        "password": password,
        "email": email,
        "job": job,
        "date_birth": str(date_birth),
        "ssn": ssn,
        "address": address,
        "user_agent": user_agent,
        "phone": phone
    }

def fakebr():
    fake = faker.Faker("pt_BR")
    name = fake.first_name()
    last_name = fake.last_name()
    username = f"{name.lower().replace(' ', '')}_{last_name.lower().replace(' ', '')}"
    password = fake.password(length=12, special_chars=True, digits=True)
    email = f"{name.lower()}.{last_name.lower().replace(' ', '')}@gmail.com"
    job = fake.job()
    date_birth = fake.date_of_birth(minimum_age=18)
    cpf = fake.cpf()
    rg = fake.rg()
    address = fake.address().replace('\n', ' ')
    user_agent = fake.user_agent()
    phone = fake.phone_number()

    return {
        "name": name,
        "last_name": last_name,
        "username": username,
        "password": password,
        "email": email,
        "job": job,
        "date_birth": str(date_birth),
        "cpf": cpf,
        "rg": rg,
        "address": address,
        "user_agent": user_agent,
        "phone": phone
    }
def show(perfil):
    print("===================================")
    print(f"Name: {perfil['name']} {perfil['last_name']}")
    print(f"Username: {perfil['username']}")
    print(f"Password: {perfil['password']}")
    print(f"Email: {perfil['email']}")
    print(f"Job: {perfil['job']}")
    print(f"Date of Birth: {perfil['date_birth']}")

    if "cpf" in perfil:
        print(f"CPF: {perfil['cpf']}")
        print(f"RG: {perfil['rg']}")
    else:
        print(f"SSN: {perfil['ssn']}")

    print(f"Address: {perfil['address']}")
    print(f"User-Agent: {perfil['user_agent']}")
    print(f"Phone: {perfil['phone']}")
    print("===================================")

print("——————————————————————————————————————————————————————")
lista_perfis = []
try:
    nacionality = int(input("""
    [1] — BR/Brazilian
    [2] — US/American

    > """))
except ValueError:
    print("Only numbers! (1 or 2)")
    sys.exit()
try:
    quant = int(input("How many? "))
    if quant <= 0:
        print("Numbers greater than 0!")
        sys.exit()
except ValueError:
    print("Only numbers!")
    sys.exit()
if nacionality == 2:
    for i in range(quant):
        perfil = fakeus()
        lista_perfis.append(perfil)
        show(perfil)
elif nacionality == 1:
    for i in range(quant):
        perfil = fakebr()
        lista_perfis.append(perfil)
        show(perfil)
else:
    print("Choose a valid option! (1-BR ou 2-US)")
    sys.exit()

save_json = str(input("Do you want to save the profiles in JSON? [Y/N]: "))
if save_json.upper() == "Y":
    with open("identities.json", "w", encoding="utf-8") as f:
        json.dump(lista_perfis, f, indent=4, ensure_ascii=False)
        print(f"File JSON identities.json created.")
