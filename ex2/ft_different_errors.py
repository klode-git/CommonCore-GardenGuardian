def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc") #ValueError

    elif operation_number == 1:
        x = 10 / 0 #ZeroDivisionError
    
    elif operation_number == 2:
        open("/non/existent/file") #FileNotFoundError

    elif operation_number == 3:
        result = "hello" + 5 #TypeError
    
    else:
        print("Operation completed successfully")

def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for i in range(5):
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
        
        except ValueError as e:
            print(f"Caught ValueError: {e}")

        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")

        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")

        except TypeError as e:
            print(f"Caught TypeError: {e}")

    print("All error types tested successfully!")

if __name__ == "__main__":
    test_error_types()