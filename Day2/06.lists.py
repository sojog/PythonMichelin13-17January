
## Definition of a list
collection =  [1, 2, 3, 4, 5]
print(collection, type(collection))


## Iteration of a list
for i in collection:
    print("i=", i)

## Indexing (READ) a value from a list
print("Position 0: ", collection[0])
print("Position 3: ", collection[3])
print("Position -3: ", collection[-3])
print("Position -5: ", collection[-5])

## Counting values
print("len=", len(collection))


## Updating values from a list
collection[2] = 33333
print(collection)


## Add at the end
collection.append(678)
print(collection)

# Erase the last element on the list
collection.pop()
print(collection)


## Insert at a specific index
collection.insert(0, "blue")
print(collection)


## Erase at a specific index e.g.: 0
collection.pop(0)
print(collection)
