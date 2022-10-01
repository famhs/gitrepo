def power_function(base_nb,power_nb):
    answer=1
    for i in range (power_nb):
      answer=answer * base_nb
    print("the result is: " + str(answer))  
    return answer
  

base_nb=int(input("Enter the base number: "))
power_nb=int(input("Enter the power number: "))
power_function(base_nb,power_nb)














