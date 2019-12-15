
## SOLUTION ==1 

def sorted_array(nums):
  if nums is None:
    raise Exception('Wrong list')
  results_list = []
  frequency_dictionary ={0:0, 1:0}
  for number in nums:
    if number == 0:
      frequency_dictionary[0] += 1 # frequency_dictionary[0]= frequency_dictionary[0]+1 ;  
    elif number ==1:
      frequency_dictionary[1] += 1 # frequency_dictionary[1] = frequency_dictionary[1]+1 ; 
    else:
      raise Exception('Not a bit value')
  item_value_0 = frequency_dictionary.get(0) 
  item_value_1 = frequency_dictionary.get(1)
  for i in range(0,item_value_0):
    results_list.append(0)
  for x in range(0, item_value_1):
    results_list.append(1)
  return results_list






 ## SOLUTION ==2 
  
def binary_search(lst):
  if lst is None:
    return "Aishwarya says Hi"
  l, s = len(lst), sum(lst)
  result = [0] * (l-s)+[1]*s
  return result 
  
 




## TEST CASES 

print(sorted_array([1,0,1,0,1]))
print(sorted_array([1,1,1]))
print(sorted_array([0,0]))
print(sorted_array([]))
print(sorted_array([1,2,3,4,5]))
print(sorted_array(None))



print(binary_search([1,0,1,0,1]))
print(binary_search([1,1,1]))
print(binary_search([0,0]))
print(binary_search([]))
print(binary_search(None))

