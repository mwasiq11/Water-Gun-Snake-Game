
import random
computer=random.choice([1,-1,0])

you=int(input("Enter the number:"))

you_dict={
1 :"s",
-1 :"w",
0 :"g",   
}

reverse_dict={

1 :"snake",
-1: "water",
0 :"gun",
}

try:

   if you not in you_dict:
      
      raise KeyError

   you1=you_dict[you]

   print(f"your choice:{reverse_dict[you]}\n computer choice:{reverse_dict[computer]}")

   if(computer==you):
      print("its draw")

   elif(computer==1 and you==-1):
      print("you lose")

   elif(computer==1 and you==0):
      print("you win")

   elif(computer==-1 and you==1):
      print("you win")

   elif(computer==-1 and you==0):
      print("lose")

   elif(computer==0 and you==-1):
      print("you win")
      
   elif(computer==0 and you==1):
      print("you lose")

except KeyError:

   print("Please enter the correct number.")