Woodendot is an online site for the purchase of furniture products. In the application, users can select, buy and do so on.All data for the site is taken from the server(folder 'back')

Installation process:

clone the repository                                                                    
cd back                                                                                                   
create the virtualenv                                                                                                         
pip install djangorestframework,pip install djangorestframework-jwt,python -m pip install django-cors-headers                                           
python manage.py migrate                                                                                              
python manage.py createsuperuser                                                                
python manage.py runserver.
cd front                                                                                                                                          
ng serve --open
