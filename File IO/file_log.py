my_list = list(input("Enter the list items: ").split())
   
try:
    file_obj = open("/home/adarshsingh/Anudip_Classes/File IO/error_log.txt", "a+")
 
    for item in my_list:
        try:
            if item.isdigit():
                val = int(item)
            else:
                val = item 

            result = 100 / val  
            file_obj.write(f"\n{result}")

        except ZeroDivisionError:
            err = "Division by '0' is not possible"
            file_obj.write(f"\n{err}")

        except TypeError:
            err = "'100' is only divisible by numbers."
            file_obj.write(f"\n{err}")
except FileNotFoundError:
    print("File does not exists")
else:
    file_obj.seek(0)
    content = file_obj.read()
    print(content)

finally:
    print("End of program.")
    file_obj.close()