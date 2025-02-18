# Kylenn Rhyss Cortez
# ITELEC2
# Laboratory # 14 - Guided Coding Exercise: Nested for Loop to Print a Multiplication Table

def main():
    # Outer loop for rows (1 to 5)
    for i in range(1, 6):  
        # Inner loop for columns (1 to 5)
        for j in range(1, 6):  
            # Calculate the product
            product = i * j  
            # Print the product with formatting
            print(f"{product:4}", end="")  
        # New line after each row
        print()  

if __name__ == "__main__":
    main()

