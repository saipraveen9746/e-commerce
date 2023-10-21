# import csv






import csv

class Admin:
    def  adddetails(self):

        Employee_id =(input("Enter the Employee id : "))
        Name = input("Enter the Name : ")
        Departement = input("Enter the Departement : ")
        Place = input("Enter the Place : ")
        Salary = (input("Enter the Salary : "))

        data = {"Emp_id": Employee_id ,"Name":Name,"Departement":Departement,"Place":Place,"Salary":Salary }
        with open("employeemgmt.csv","a",newline="") as csv_file:
            header = ["Emp_id", "Name", "Departement", "Place", "Salary"]
            writer = csv.DictWriter(csv_file, fieldnames=header)
            if csv_file.tell()==0:
                writer.writeheader()
            writer.writerow(data)
        print("Data updated successfully")

    def readlist(self):
        Emp_id = input("enter Employement id : ")
        with open("employeemgmt.csv","r",newline="") as csv_file:
            id = csv.DictReader(csv_file)
            data = list(id)
            for i in data:
                if i["Emp_id"] == Emp_id:
                    print("Emp_id:",i["Emp_id"],"Name:",i["Name"],"Departement:",i["Departement"],"Place:", i["Place"],"Salary:",i["Salary"])

                    return
            else:
                print("Emp_id not found")
    def deletion(self):
        dele = input("enter id you want to delete : ")
        with open("employeemgmt.csv","r",newline="") as csv_file:
            id = csv.DictReader(csv_file)
            data = list(id)
            for i,j in enumerate(data):

                if j["Emp_id"] == dele:
                    del data [i]
                    print("Deleted")
        with open("employeemgmt.csv", 'w', newline="") as csvfile:
            header = ["Emp_id", "Name", "Department", "Place", "Salary"]
            delt = csv.DictReader(csvfile, fieldnames=header)
            delt.writeheader
            delt.writerows(data)
            print("data deleted")

obj = Admin()
obj.deletion()

















