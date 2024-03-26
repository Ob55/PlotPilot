from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

Base = declarative_base()
class Care_taker(Base):
    __tablename__ = 'care-taker'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    plot_no = Column(Integer())




class tenant (Base):
    __tablename__ ='tenants'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    hs_no = Column(Integer)

# if __name__=='__main__':
#     engine = create_engine('sqlite:///houses.db')
#     Base.metadata.create_all(engine)

#     sessioncreater = sessionmaker(bind=engine)
#     mysession = sessioncreater()