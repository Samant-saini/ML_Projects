from flask import Flask, render_template, request
import pickle
from tensorflow.keras.models import load_model

app = Flask(__name__)
# import joblib

# model = joblib.load('hotel3.pkl')


model= pickle.load(open('main.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html',**locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    rating=float(request.form['rating'])
    review=float(request.form['review'])
    rooms=int(request.form['rooms'])
    night=int(request.form['night'])
    Adult=int(request.form['Adult'])
    child=int(request.form['child'])

    hotel = request.form["hotel"]
    if (hotel == 'Himalayan_Nature_Walk_Resort_Manali'):
        Himalayan_Nature_Walk_Resort_Manali=1
        Hill_Queen_Resort_Manali=0
        Shree_Ram_Cottage_Manali_Bedroom_Luxury_Cottages_Available=0
        The_14_Gables_A_Boutique_Stay=0
        Hotel_The_North_Wind=0
        Vashisht_valley_hotel=0
        The_Hosteller_Manali=0
        Hotel_Mountain_Meadows=0
    elif (hotel == 'Hill_Queen_Resort_Manali'):
        Himalayan_Nature_Walk_Resort_Manali=0
        Hill_Queen_Resort_Manali=1
        Shree_Ram_Cottage_Manali_Bedroom_Luxury_Cottages_Available=0
        The_14_Gables_A_Boutique_Stay=0
        Hotel_The_North_Wind=0
        Vashisht_valley_hotel=0
        The_Hosteller_Manali=0
        Hotel_Mountain_Meadows=0

    elif (hotel == 'Shree_Ram_Cottage_Manali_Bedroom_Luxury_Cottages_Available'):
        Himalayan_Nature_Walk_Resort_Manali=0
        Hill_Queen_Resort_Manali=0
        Shree_Ram_Cottage_Manali_Bedroom_Luxury_Cottages_Available=1
        The_14_Gables_A_Boutique_Stay=0
        Hotel_The_North_Wind=0
        Vashisht_valley_hotel=0
        The_Hosteller_Manali=0
        Hotel_Mountain_Meadows=0
    elif (hotel == 'The_14_Gables_A_Boutique_Stay'):
        Himalayan_Nature_Walk_Resort_Manali=0
        Hill_Queen_Resort_Manali=0
        Shree_Ram_Cottage_Manali_Bedroom_Luxury_Cottages_Available=0
        The_14_Gables_A_Boutique_Stay=1
        Hotel_The_North_Wind=0
        Vashisht_valley_hotel=0
        The_Hosteller_Manali=0
        Hotel_Mountain_Meadows=0
    elif (hotel == 'Hotel_The_North_Wind'):
        Himalayan_Nature_Walk_Resort_Manali=0
        Hill_Queen_Resort_Manali=0
        Shree_Ram_Cottage_Manali_Bedroom_Luxury_Cottages_Available=0
        The_14_Gables_A_Boutique_Stay=0
        Hotel_The_North_Wind=1
        Vashisht_valley_hotel=0
        The_Hosteller_Manali=0
        Hotel_Mountain_Meadows=0
    elif (hotel == 'Vashisht_valley_hotel'):
        Himalayan_Nature_Walk_Resort_Manali=0
        Hill_Queen_Resort_Manali=0
        Shree_Ram_Cottage_Manali_Bedroom_Luxury_Cottages_Available=0
        The_14_Gables_A_Boutique_Stay=0
        Hotel_The_North_Wind=0
        Vashisht_valley_hotel=1
        The_Hosteller_Manali=0
        Hotel_Mountain_Meadows=0
    elif (hotel == 'The_Hosteller_Manali'):
        Himalayan_Nature_Walk_Resort_Manali=0
        Hill_Queen_Resort_Manali=0
        Shree_Ram_Cottage_Manali_Bedroom_Luxury_Cottages_Available=0
        The_14_Gables_A_Boutique_Stay=0
        Hotel_The_North_Wind=0
        Vashisht_valley_hotel=0
        The_Hosteller_Manali=1
        Hotel_Mountain_Meadows=0
    elif (hotel == 'Hotel_Mountain_Meadows'):
        Himalayan_Nature_Walk_Resort_Manali=0
        Hill_Queen_Resort_Manali=0
        Shree_Ram_Cottage_Manali_Bedroom_Luxury_Cottages_Available=0
        The_14_Gables_A_Boutique_Stay=0
        Hotel_The_North_Wind=0
        Vashisht_valley_hotel=0
        The_Hosteller_Manali=0
        Hotel_Mountain_Meadows=1
    else:
        Himalayan_Nature_Walk_Resort_Manali=0
        Hill_Queen_Resort_Manali=0
        Shree_Ram_Cottage_Manali_Bedroom_Luxury_Cottages_Available=0
        The_14_Gables_A_Boutique_Stay=0
        Hotel_The_North_Wind=0
        Vashisht_valley_hotel=0
        The_Hosteller_Manali=0
        Hotel_Mountain_Meadows=0
    

    city = request.form["city"]
    if (city == 'Manāli'):
       Manāli=1
       New_Manali_Manāli=0

    elif (city== 'New Manali, Manāli'):
       Manāli=0
       New_Manali_Manāli=1
        
        
           
    
    result=model.predict([[rating,
    review,
    rooms,
    night,
    Adult,
    child,
    Himalayan_Nature_Walk_Resort_Manali,
    Hill_Queen_Resort_Manali,
    Shree_Ram_Cottage_Manali_Bedroom_Luxury_Cottages_Available,
    The_14_Gables_A_Boutique_Stay,
    Hotel_The_North_Wind,
    Vashisht_valley_hotel,
    The_Hosteller_Manali,
    Hotel_Mountain_Meadows,
    Manāli,
    New_Manali_Manāli]])# Replace with your actual prediction result
    # return render_template('index.html',**locals())
        # return render_template('result.html', result=result)

        # return render_template('result.html', result=result)
    return render_template('index.html',result="Your hotel price will be Rs. {}".format(result))


  

if __name__ == '__main__':
    app.run(debug=True)
