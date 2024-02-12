maths = int(input("maths: "))
eng = int(input("eng: "))
kis = int(input("kis: "))
bio = int(input("bio: "))

average = (maths+eng+kis+bio)/4
print(average)

if (average >=0 and average <= 39):
    print("E")
if average >= 40 and average <= 50:
        print("D")
if average > 50 and average <= 60:
            print("C")
if average > 60 and average <= 70:
                print("B")
if average > 70 and average <= 100:
                    print("A")
if average > 100:
    print("INVALID")

# if not maths > 60:
#     pass

# if maths != 60:
#     pass
