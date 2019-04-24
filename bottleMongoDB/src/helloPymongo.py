import pymongo
import sys

# establish a connection to the database
client = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db_school = client.school
col_grades = db_school.grades


def find():

    print("find, reporting for duty")

    query = {'type': "exam"}

    try:
        cursor = col_grades.find(query).limit(10).skip(30)

    except:
        print("Unexpected error:", sys.exc_info()[0])

    sanity = 0
    for doc in cursor:
        print(doc)
        sanity += 1
        if (sanity > 10):
            break


def find_one():

    print("find one, reporting for duty")
    query = {'student_id': 10}

    try:
        doc = col_grades.find_one(query)

    except:
        print("Unexpected error:", sys.exc_info()[0])

    print(doc)


def main():
    find()
    find_one()


if __name__ == "__main__":
    main()
