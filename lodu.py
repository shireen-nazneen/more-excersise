# import random
# user=(input("enter how many plears::::"))
# if user=="4":
#     player1=0
#     player2=0
#     player3=0
#     player4=0
#     while True:
#         enter=input("touch")
#         dise=[1,2,3,4,5,6]
#         output1=(random.choice(dise))
#         print(output1)
#         player1+=output1
#         print(player1,"plear1")
#         enter=input("touch")
#         output2=random.choice(dise)
#         print(output2)
#         player2+=output2
#         print(player2,"plear2")
#         enter=input("touch")
#         output3=random.choice(dise)
#         player3+=output3
#         print(output3)
#         player3+=output3
#         print(player3,"player3")
#         output4=random.choice(dise)
#         nter=input("touch")
#         print(output4)
#         player4+=output4
#         print(player4,"player")
#         if player1>=50:
#             print("player1 *****won****")
#             if player2>player3 and player2>player4:
#                 print("second rank is player2" )
#             elif player1>player3 and player1>player4:
#                 print("third rank is  player1")
#             elif player3>player4 and player3>player1:
#                 print("fourt rank is palyer3")
#             else:
#                 print("fourt rank is player4")
#             break
#         elif player2>=50:
#             if player2>player3 and player2>player4 and player2>player1:
#                 print("first rank is player2" )
#             elif player1>player3 and player1>player4:
#                 print("second rank is  player1")
#             elif player3>player4 and player3>player1:
#                 print("third rank is palyer3")
#             else:
#                 print("fourt rank is player4")
#             break
# a=[2,4,5,3,6,7,9,2,1]
# b=a.sort(reverse=True)
# print(a)

from typing import Dict

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
x=lambda x:2*5
print(x(3))
def fun():
    a=1
    print(a)
    fun()
fun

            


