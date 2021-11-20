import random
import pandas as pd

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

def load_excel_pandas():
    df = pd.read_excel("./data/secret_santa.xlsx")
   
    return df

def create_gift_receiver_message(gift_reciever, df):

    # print(df)
    # print(df['Username'])

    row = df.loc[df['Username'] == gift_reciever]
    message = "Hail! You have received as you secret satan: " + str(row['Nickname'].values[0]) + " AKA " + str(row['Username'].values[0]) + '\n'
    message += 'They supposedly like, "' + str(row['Likes'].values[0]) + '."' + '\n'
    message += 'They fucking hate, "'+ str(row['Hates'].values[0]) + '", so, not that.' + '\n'
    message += "If you are sending something physically, their address is: " +  str(row['Address'].values[0]) + '\n'
    message += "Digital stuff could probably be emailed to " +  str(row['Email'].values[0]) + '\n'
    message += "HAIL SATAN (tis the season)"
  
    return message

if __name__ == "__main__":
    # test_list = ['Joe', 'Quincy', 'Seth', 'Jordan', 'Kyle', 'Paul']
    # results = secret_santa(test_list)
    # save_results(results)

    df = load_excel_pandas()
    message = create_gift_receiver_message('Aufy', df)
    print(message)