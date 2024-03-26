from main import create_engine, sessionmaker, Base, Care_taker, tenant
from faker import Faker
import random

engine = create_engine('sqlite:///houses.db')
Base.metadata.create_all(engine)

sessioncreator = sessionmaker(bind=engine)
mysession = sessioncreator()

fakedata = Faker()

if __name__=='__main__':

    print("seeding")
    mysession.query(Care_taker).delete()
    mysession.commit()

    for i in range(10):

        caretaker =  Care_taker(name = fakedata.name(), plot_no=random.randrange(10, 50))
        mysession.add(caretaker)
        mysession.commit()

    for i in range(30):

        tenants = tenant(name = fakedata.name(), hs_no=random.randrange(1, 300))
        mysession.add(tenants)
        mysession.commit()