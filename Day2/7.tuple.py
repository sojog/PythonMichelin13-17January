
## Definition of a tuple
collection =  (1, 2, 3, 4, 5)
print(collection, type(collection))

## Iteration of a tuple
for i in collection:
    print("i=", i)

## Indexing (READ) a value from a tuple
print("Position 0: ", collection[0])
print("Position 3: ", collection[3])
print("Position -3: ", collection[-3])
print("Position -5: ", collection[-5])

## Counting values
print("len=", len(collection))

## Updating values from a tuple
# collection[2] = 33333 # this will not work
# a tuple is immutable
print(collection)


## Add at the end - cannot append
# collection.append(678)
print(collection)

collection = "hello"
print(collection)

