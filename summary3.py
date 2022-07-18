list method:

Append(): add an element at the end of list.
clear(): method empties the list. The list still remains, but it has no content.
copy():copy of the list.
count():Return the number of elements with the specified value.
extend():add the element of a list to the end of the current list.
index():Return the index of the frist element with the specified.
insert():add an element at the specified position.
pop():remove the specified index from the list.
remove():remove the specified item.
reverse():Remove the item with the specified value/reverse order of list.
sort():method that will sort the list alphanumerically, ascending by default.



Set: 
  a set s an unordered collection of item. every set element is unique (no duplicate) and must be immutable (cannot be changed).
set itself is mutable we can add or remove item from it.set can also be used to perform mathematical set operation like union, intersection, symmetric difference etc.we cannot have one more set inside it.
   set cannot contain a list and one more set inside it. if it is their them answer is type error:unhashable type:'set'

Frozenset operation:
   like normal set, frozonset can also perfer different operation like copy,difference, intersection,symmetric difference.
 in frozenset we cannot add or remove the element.frozenset is immutable.


Set method: [add, clear, copy, difference, difference_update, discard, intersection, intersection_update, isdisjoint, issubset, issuperset, pop, remove,symmetric_difference, symmetric_difference_update, union, update]

add(): add an element to the set.
clear():removes all the element from the set. 
copy():Return a copy of the set.
difference():Return a set containing the difference between two or more set.
difference update():remove the items in this set that are also included in another,spcified set.
discard():Remove the specified item.
intersection():Returns a set, that is the intersection of two other set.
intersection_update():Remove the items in this set that are not present in other specified set(s).
isdisjoint():Return whether two set have a intersection or not.
issubset():Return whether another set contain this set or not.
issuperset():Return whether this set contain another set or not.
pop():remove an element from the set.
remove():Remove the specified element.
Symmetric_difference():Return a set with the symmetric difference of two set.
Symmetric_difference_update():insert the symmetric difference from this set and another.
union():Return a set containing the union of set.
Update():update the set with the union of this set and others.


Dictionary:
dictionaries are used to store data values in key:value pairs.
dictionary is a collection which is ordered, changeable and do not allow duplicate.
dictionaries are written with curly barckets and have keys and value.
order-the items have a defined order and that order will not charge.
unorder-the items doesnot have a defined order.
changeable- we can change, add or remove item after dicitionary has been created.
dictionary cannot have two item with the same key.
dictionary items can be of any data type.


Dictionary Method:

clear():Remove all the elements from the dictionary.
copy():Returns a copy of the dictionary.
fromkeys():Returns a dictionary with the specified key and value.
get(): Returns the value of the specified key.
items():Returns a list containing a tuple for each key value pair.
keys(): Returns a list containing the dictionary's keys.
pop():Remove the element with the specified key.
popitem()-Remove the last inserted key value pair.
setdefault():Returns the value of the specified key if the key doesnot exist insert the key with the specified value.
update():update the dictionary with the specified value pairs.
values():Returns a list of all the value in the dictionary


Tuple:
tuple contain two method index and count.
