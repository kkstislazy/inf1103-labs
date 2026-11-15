def get_positive_float(prompt: str) -> float: 
    while True: 
        try: 
            value = float(input(prompt))
            if value<= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number")