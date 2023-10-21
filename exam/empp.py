import csv


class hr:

    def add_details(self):
        emp_id = input("enter employee id:")
        name = input("enter the name of employee:")
        __salary = input("enter the salary:")
        department = input("enter the department :")
        place = input("enter the employee place:")
        data = {"emp_id": emp_id, "name": name, "salary": __salary, "department": department, "place": place}
        with open("emp_data.csv", 'a', newline='') as csvfile:
            header = ["emp_id", "name", "salary", "department", "place"]
            csv_writter = csv.DictWriter(csvfile, fieldnames=header)
            if csvfile.tell() == 0:
                csv_writter.writeheader()
            csv_writter.writerow(data)
            print("data updated to data base")

    def emp_details(self):
        emp_id = input("enter the id:")
        with open("emp_data.csv", 'r', newline="") as csvfile:
            cs = csv.DictReader(csvfile)
            data = list(cs)
            for i in data:
                if i["emp_id"] == emp_id:
                    print("emp_id:", i["emp_id"], "emp_name:", i["name"], "salary:", i["salary"], "department:",
                          i["department"], "place:", i["place"])
                    return
            else:
                print("employee not found")

    def deletion(self):
        emp_id1 = input("enter employee id:")
        with open("emp_data.csv", 'r', newline="") as csvfile:
            cs = csv.DictReader(csvfile)
            data = list(cs)
            for i, j in enumerate(data):
                if j["emp_id"] == emp_id1:
                    del data[i]
                    print("deleted")
        with open("emp_data.csv", 'w', newline="") as csvfile:
            header = ["emp_id", "name", "department", "place", "salary"]
            delt = csv.DictWriter(csvfile, fieldnames=header)
            delt.writeheader()
            delt.writerows(data)
            # print("data deleted")