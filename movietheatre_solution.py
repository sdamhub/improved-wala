# defining a function
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

#I added to the purchase entry
