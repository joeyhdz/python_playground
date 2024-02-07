'''
Turning in this in just in case
'''
#################################
# append - adds a new element to a list
#################################

# example:
list_of_cats =['mango','scout','banksy','mr.kitty']
list_of_cats.append('miko')
print(list_of_cats)


#################################
# extend - similar, but adds all elements of one list to the end of the target list
#################################
# reset the list
list_of_cats.pop(-1)
# example:
target_cat_list = ['miko']
print('LIST OF CATS: ', list_of_cats)
target_cat_list.extend(list_of_cats)
print('TARGET CAT LIST WITH ALL CATS ADDED:',target_cat_list)


#################################
# index - returns the "index" of an element passed in
#################################


print(target_cat_list.index('miko'))


#################################
# insert - puts a value into a list based on a certain position
#################################

target_cat_list.insert(1,'senior Dos')
print('UPDATED TARGET CAT LIST: ', target_cat_list)


#################################
# remove - removes the first value from a list based on input value
#################################

target_cat_list.remove('senior Dos')
print("Senior Dos has left the chat:", target_cat_list)

#################################
# pop - used it above.. but it pops out a value at the desired index
#################################

print(target_cat_list)
target_cat_list.pop(0)
print('The first cat is gone', target_cat_list)

#################################
# count - gives the amt of times an input occurs
#################################

print(target_cat_list.count('scout'))


#################################
# reverse - the list will be backwards
#################################

list_of_cats.reverse()
print(list_of_cats)


#################################
# sort - sort the elements in a list
#################################

cat_ranking_at_competitions = [1,2,10,10,12,3]
cat_ranking_at_competitions.sort()
print(cat_ranking_at_competitions)


#################################
# [1] + [1] - list concat
#################################

new_list = cat_ranking_at_competitions + target_cat_list
print(new_list)

#################################
# [2]*2 - duplicate and concat the list  
#################################

twin_cats = target_cat_list*2
print(twin_cats)


#################################
# [1,2][i:] this returns everyting to the right of i 
#################################

print("these are the remaining twins:",twin_cats[2:])

#################################
# [x for x in list] list comprehension  
#################################

alpha_cats = []
[alpha_cats.append(x) for x in twin_cats[2:]]
print("Alpha Cats:",alpha_cats)


#################################
# [x for x in list] same as above but this adds a conditional  
#################################

specific_alpha_cat = []
[specific_alpha_cat.append(x) for x in twin_cats[2:] if x == 'mr.kitty']
print(specific_alpha_cat)


#################################
# [y*2 for x in [[1,2],[3,4]] for y in x]
#################################