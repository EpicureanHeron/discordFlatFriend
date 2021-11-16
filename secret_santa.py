import random

def secret_santa():

    users = ['Joe', 'Quincy', 'Seth', 'Jordan', 'Kyle', 'Paul']

    user_copied = users.copy()

    end_result = []

    for gift_giver in users:
        print(gift_giver)
        random_index = random.randint(0,len(user_copied)-1)
        gift_reciever = user_copied[random_index]

        while gift_reciever == gift_giver:
            random_index = random.randint(0,len(user_copied)-1)
            gift_reciever = user_copied[random_index]
        
        pair = (gift_reciever, gift_giver)
        print("Matched: " + str(pair))
        end_result.append(pair)
        user_copied.remove(gift_reciever)
        print(user_copied)
        

    return end_result

if __name__ == "__main__":
    results = secret_santa()
    print('end results')
    print(results)