import pickle
fichero=open('databin.json','rb')
data=pickle.load(fichero)
for client in data['clients']:
    print('Fisrt name:', client['first_name'])
    print('Last name:', client['last_name'])
    print('Age:', client['age'])
    print('Amount:', client['amount'])
    print('')