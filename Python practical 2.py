#User defined number of elements
def get_user_list(list_name):
    num_elements = int(input("Enter number of elements : "))
    user_list = []
    for i in range (num_elements):
        element = input("Enter element for the list :")
        user_list.append(element)
    return user_list

print("---FIRST LIST---")
list1 = get_user_list("List 1")

print("---SECOND LIST---")
list2 = get_user_list("List 2")

#Checking for common elements
def check_common(list1 , list2):
    for item in list1:
        if item in list2:
            return True
    return False
result = check_common(list1,list2)
 
#Final printing of lists and results
print ("List 1 :", list1)
print ("List 2 :", list2)
print("Has common element :", result)
