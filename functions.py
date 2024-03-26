from seeds import mysession 
from main import Care_taker, tenant

def list_caretakers():
    mycaretaker = mysession.query(Care_taker).all()
    for caretaker in mycaretaker:
        print(caretaker.name)
    pass



def list_tenants():
    mytenants = mysession.query(tenant).all()
    for tenants in mytenants:
        print(tenants.name)
    pass

def add_caretaker():
    caretaker_name = input("Name.: ")
    caretaker_plot_no = input("Plot No.: ")
    caretaker = Care_taker(name=caretaker_name, plot_no=caretaker_plot_no)
    mysession.add(caretaker)
    mysession.commit()
    print(f"New Care Taker {caretaker_name} Created")



def add_tenant():
    tenant_name = input("Name.: ")
    tenant_hs_no = input("Plot No.: ")
    tenants = tenant(name=tenant_name, hs_no=tenant_hs_no)
    mysession.add(tenants)
    mysession.commit()
    print(f"New tenant {tenant_name} Created")


def ejject_caretaker():
    caretaker_plot_no=input("Enter the plot nu you want to delete: ")
    caretaker_delete = mysession.query(Care_taker).filter_by(plot_no=caretaker_plot_no).one()
    mysession.delete(caretaker_delete)
    mysession.commit()
    print(f"The CareTaker {caretaker_plot_no} has been ejected")



def ejject_tenant():

    tenant_hs_no=input("Enter the plot nu you want to delete: ")
    tenant_delete = mysession.query(tenant).filter_by(hs_no=tenant_hs_no).one()
    mysession.delete(tenant_delete)
    mysession.commit()
    print(f"The tenant {tenant_hs_no} has been ejected")


def exit_program():
    print("GOODBYE!!!! THANK YOU!!!")
    exit()     