from app.practice_centers.models import PracticeCenter
from instance.climates.fakes import climate1, climate2, climate3

center1 = PracticeCenter(None,
                         name='Mont-Orford National Park',
                         email='parc.mont-orford@sepaq.com',
                         web_site='https://www.sepaq.com/pq/mor/',
                         phone_number='819 843-9855',
                         climates=[climate2])
center2 = PracticeCenter(None,
                         name='Parc des Montagnards',
                         email='info@censhefford.ca',
                         web_site='https://www.cantonsdelest.com/quoi-faire/980'
                                  '/parc-des-montagnards',
                         climates=[])
center3 = PracticeCenter(None,
                         name='Gault Nature Reserve of McGill University',
                         climates=[climate1, climate3])
