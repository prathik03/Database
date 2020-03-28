import pymongo
import os
import time

client = pymongo.MongoClient("mongodb://localhost:27017")


def create_collec(stat):

    collection_detail = []
    dbname = input("Enter your database name : ")
    collection_detail.append(dbname)
    db = client[dbname]
    collection_detail.append(db)
    cname = input("Enter the name for your collection : ")
    collection_detail.append(cname)
    col = db[cname]
    collection_detail.append(col)
    print("Collection created successfully in the database", dbname)
    collec = True
    stat[0]=1

    return (collection_detail)


def insert_data(stat):
    database_name=stat[0]
    database=client[database_name]
    collection_name=stat[2]
    column = database[collection_name]
    insdic = {}
    l = []
    n = int(input("enter the no. of columns to be added : "))
    flist = []
    fdic = {}

    for i in range(n):
        l.append(input(f"enter column {i + 1} name : "))
    ne = int(input("Enter the no. of elements to be added : "))

    for i in range(ne):
        for j in range(n):
            val = input(f"value for {l[j]} :")
            insdic[l[j]] = val
        column.insert_one(insdic)
    print(col)


if __name__ == '__main__':
    # insert_data()
    """
    print("HI,I AM DB AND I HELP PEOPLE TO MAINTAIN DATABASE \n")
    print("CAN I KNOW YOUR NAME? \n")
    ch = input("y/n:")
    if ch.lower() == 'y':
        namep = input("what is your name :")
        print("HI", namep.upper())
    elif ch.lower() == 'n':
        namep = 'user'
        print("HI", namep.upper())
        print("\n\n\n\n")
    print("1) create collection \n2) insert data \n3) delete data \n4) update data \n5) view data \n6) exit")
    print("\n\n")
    """
    iscreated = [0]

    flag = True
    while flag:
        ch1 = int(input("Enter your choice : "))
        if ch1 == 1:

            status = create_collec(iscreated)
            print(status)

        elif ch1 == 2:
            if iscreated[0] == 1:
                insert_data(status)

            else:
                print("You Have not created any collection!!")
                print("do you want to create a collection?\n")
                print("y/n")
                ch2 = input()
                if ch2.lower() == 'y':
                    status = create_collec(iscreated)

                    #insert_data(status)
                else:
                    break
