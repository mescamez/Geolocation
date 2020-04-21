## Geolocation Project
The purpose of this Project is to find a perfect location for a Company following the next parameters:
- Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.
- 30% of the company have at least 1 child.
- Developers like to be near successful tech startups that have raised at least 1 Million dollars.
- Executives like Starbucks A LOT. Ensure there's a starbucks not to far.
- Account managers need to travel a lot
- All people in the company have between 25 and 40 years, give them some place to go to party.
- Nobody in the company likes to have companies with more than 10 years in a radius of 2 KM.
- The CEO is Vegan

To achieve this perfect location a database of MongoDB has been used and different datasets have been added:
- Companies dataset, which contains a huge number of companies located mostly in United States. 
- Starbucks dataset, downloaded from (www.kaggle.com) with information about Starbucks coffee shops.
- Additional information related with airports, bars and vegan restaurants extracted from the Foursquare API.


A detailed description of the work done with each source of information is shown below: 

# Companies

This dataset has been cleaned up to adapt it to our needs. It has been divided into technological and non-technological companies. 

In order to eliminate those companies with less than 1.000.000$ benefits, “total_money_raised” column has been homogenized by means of currency exchange and format standardization.

Furthermore, all the companies whose latitude or longitude was not correct or did not exist have been also discarded. 


# Starbucks

This dataset has been filtered in order to obtain the ones located only in United States, since the previous dataset contained mainly data from American companies.

# Foursquare

To be able to access to the data of this API it has been necessary to register and obtain a "client_id" and "client_secret", both have been saved in a .env file which has been hidden for safety reasons.
All the searches has been performed based on the categoryId offered by the API for each wanted data.
Moreover, the search has been limited geographically to the US. The information obtained has been stored in several datasets differentiated by type of information (airports, vegan restaurants and bars).

#
Once all the necessary information was collected, it was included in the MongoDB database in different collections. In order to work with geospatial queries it was necessary to create a column called "geolocation" in each dataframe and then import the information into the database to create a geospatial index. 

Finally, the information of the companies collection has been filtered through geoqueries, starting first with the most faraway locations (in this case airport) to gradually decrease the radius until reaching the ideal location for our company.



