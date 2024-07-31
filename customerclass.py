from personclass import Person

class Customer(Person):
    def __init__(self, name, address, age, phone_number, cust_number, on_list):
        # Call superclass __init__ method

        Person.__init__(self, name, address, age, phone_number)
        # super().__init__(self, name, address, age, phone_number)

        # Initialize the cust_number and on_list attributes
        self.__cust_number = cust_number
        self.__on_list = on_list

    # Mutator functions for cust_number and on_list
    def set_cust_number(self, cust_number):
        self.__cust_number = cust_number

    def set_on_list(self, on_list):
        self.__on_list = on_list

    # Accessor functions for cust_number and on_list
    def get_cust_number(self):
        return self.__cust_number

    def get_on_list(self):
        return self.__on_list

    def __str__(self):
        disp_string=super().__str__()
        on_list = ""
        disp_string += '\nCustomer number:  ' + self.__cust_number
        if self.__on_list == 1:
            ol_flag = 'Yes'
        else:
            ol_flag = 'No'
        disp_string += '\nMailing List:  ' + (ol_flag)
        return disp_string