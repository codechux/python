# a = "a a boy"
# print(a.rindex("a"))
# print(a.index("a"))


# my_sentense = "A quick brown fox jumps over the lazy bone"

# a = my_sentense.split(",")
# print(a)

# num = ["0", "4", "5", "6"]

# otp = "".join(num)

# print(otp)


# # s1 = "Ault"
# # s2 = "Kelly"

# # ans = s1[0:2] + s2 + s1[2:4]

# # print(ans)

# s1 = "Ault"
# s2 = "kelly"

# mi = len(s1) // 2

# x = s1[:mi] + s2 + s1[mi:]

# print(x)


# str1 = "welcome to USA, usa awesome, isn't it?"

# str2 = str1.lower().count("usa")

# print(f"the Usa count is:{str2}")

# em = "Emma is a data scientist who knows Python. Emma works at google."

# em2 = em.rindex("Emma")

# print(f"the index number of Emma is:{em2}")


# sc = "Emma-is-a-data-scientist"
# print(sc.replace("-", " "))

# jon = "/*jon is @developer & musician"

# jon1 = jon.replace("/", "").replace("*", "").replace("@", "").replace("& ", "")

# print(jon1)


# ###### list ######

# my_list = ["i", "am", "good"]
# a_list = ["she", "is", "a", "queen"]

# list1 = my_list + a_list

# print(list1[0::2])

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# get 5000 and 500 out of the list and add them together.

num1 = list1[2][2][0]
num2 = list1[2][3]

print(num1 + num2)
