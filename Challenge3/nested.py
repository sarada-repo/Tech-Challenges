def fun(object_variable, key): 
     key_list = key.split("/") 
     temp = object_variable 
     for key in key_list: 
         if temp.get(key): 
            temp = temp[key] 
         else: 
            return None 
     return temp 

object_variable_one = {"a":{"b":{"c":"d"}}} 
object_variable_value_one = fun(object_variable_one,"a/b/c") 
print("Value is",object_variable_value_one)
    
object_variable_two = {"x":{"y":{"z":"a"}}} 
object_variable_valuetwo = fun(object_variable_two,"x/y/z") 
print("Value is",object_variable_valuetwo) 
    