# Movie Theatre
# Problem

# A concession stand at a movie theatre sells two products: popcorn for $7 and soda for $2.50.
# If someone buys both on the same day, they get a bundle price of $9 for the two items.
# A customer can purchase any number of bundles on the same day. Customers can run a tab, and
# when settling the bill, we need to calculate how much they owe using the list of past purchases.

# Provide a function that, given the list of past purchases as input (string “<date>,<item>“)
# returns the amount owed.

# Here is a list of input/output examples:

# > tally( [ "2022-06-01,soda",
#   ] )
# => 2.5

# > tally( [
#     "2021-11-15,popcorn",
#     "2021-11-15,popcorn",
#     "2021-11-15,soda",
#     "2021-11-15,soda",
#   ] )
# => 18

# (7 + 7 + 2 + 2) = 18

# > tally( [
#     "2019-12-29,popcorn",
#     "2020-01-03,popcorn",
#     "2020-01-03,soda",
#     "2020-01-03,soda",
#     "2020-02-22,popcorn",
#     "2020-02-22,soda",
#   ] ) => 27.5

# (7) + (7 + 2 + 2.5) + (7 + 2) = 27.5

# > tally( [
#     "2019-12-29,soda",
#     "2020-01-03,popcorn",
#     "2020-01-03,soda",
#     "2020-01-03,soda",
#     "2020-02-22,popcorn",
#     "2020-02-22,soda",
#  ] ) => 23

<<<<<<< HEAD
#The Solution
=======

>>>>>>> c3e33551b44379dbc487f4fab37f105a832e364f

def movie_cost(purchase_enter):
    purchase_enter.sort()


    cost = []

    for index, elem in enumerate(purchase_enter):
        if (index+1 < len(purchase_enter) and index - 1 >= 0):
            prev_word = str(purchase_enter[index-1])
            curr_word = str(elem)
            next_word = str(purchase_enter[index+1])

            if ("popcorn" in prev_word):
                cost.append(7.5)
            elif ("soda" in prev_word):
                cost.append(2)

            if curr_word[0:10] == next_word[0:10] and "popcorn" in curr_word and "soda" in next_word:
                cost.append(9)



    #print(next_word)
    print(cost)
    total_cost = sum(cost)
    print("The total Amount is "+ str(total_cost))
            #print(prev_word, elem, next_word)

purchase_enter = ["2021-11-15,popcorn",
                  "2021-11-15,soda",
                  "2021-11-16,soda",
                  "2021-11-17,popcorn",
                  "2020-12-14,soda",
                  "2020-12-15,soda",
                  "2021-01-31,popcorn"]

movie_cost(purchase_enter)

