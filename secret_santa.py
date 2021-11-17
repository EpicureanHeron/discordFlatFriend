import random

def secret_santa(users):

    # users = ['Joe', 'Quincy', 'Seth', 'Jordan', 'Kyle', 'Paul']

    user_copied = users.copy()

    end_result = []

    for gift_giver in users:
       
        random_index = random.randint(0,len(user_copied)-1)
        gift_reciever = user_copied[random_index]

        while gift_reciever == gift_giver:
            random_index = random.randint(0,len(user_copied)-1)
            gift_reciever = user_copied[random_index]
        
        pair = (gift_reciever, gift_giver)
      
        end_result.append(pair)
        user_copied.remove(gift_reciever)
       
        
        

    return end_result

def save_results(list_of_tuples):
    file=open('f1.txt','w')
    for pair in list_of_tuples:
        gift_reciever = pair[0]
        gift_giver = pair[1]

        line = gift_giver + " is giving a present to " + gift_reciever + '\n'
     

        file.writelines(line)

    file.close()

if __name__ == "__main__":
    test_list = ['Joe', 'Quincy', 'Seth', 'Jordan', 'Kyle', 'Paul']
    results = secret_santa(test_list)
    save_results(results)
