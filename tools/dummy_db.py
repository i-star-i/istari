from random import choice, randint, seed

seed(557)

names = [
    "Liam",
    "Noah",
    "William",
    "James",
    "Logan",
    "Benjamin",
    "Mason",
    "Elijah",
    "Oliver",
    "Jacob",
    "Emma",
    "Olivia",
    "Ava",
    "Isabella",
    "Sophia",
    "Mia",
    "Charlotte",
    "Amelia",
    "Evelyn",
    "Abigail",
]

surnames = ["Smith", "Jones", "Williams", "Brown", "Taylor"]

languages = ["python", "R", "C", "C++", "fortran", "julia"]

discipline = ["physics", "biology", "maths", "chemistry", "computing"]


def orcid_gen():
    return "{}-{}-{}-{}".format(
        randint(0, 9999), randint(0, 9999), randint(0, 9999), randint(0, 9999)
    )


def email_gen(name, surname):
    return "{}.{}@gmail.com".format(name, surname)


def create_dummies(records=10):

    global db

    values = []
    for i in range(records):

        fn = choice(names)
        sn = choice(surnames)

        profile = {
            "first_name": fn,
            "surname": sn,
            "email": email_gen(fn, sn),
            "language": [choice(languages), choice(languages)],
            "discipline": [choice(discipline), choice(discipline)],
            "orcid": orcid_gen(),
            "github": fn,
            "institution_url": "http://www.miskatonic-university.org",
        }
        values.append(profile)

    return values


# def reviewers(language, discipline):

if __name__ == "__main__":
    print(create_dummies(10))

