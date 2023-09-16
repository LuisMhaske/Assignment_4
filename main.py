def main():
    # Initialize Constant variables
    MAX_PCK_WEIGHT = 20
    MIN_WEIGHT = 1
    MAX_WEIGHT = 10

    # Initialize variables
    pck_weight = 0
    num_of_pck_sent = 0
    idx_most_empty_pck = 0
    lightest_pck = MAX_PCK_WEIGHT
    weight_sent = 0
    unused_weight = 0

    correct_weight_item = 0

    # Prompt for the total number of items to be sent
    items_to_be_shipped = int(input("How many items do you wish to send: "))

    # Main loop to add items to packages
    while correct_weight_item < items_to_be_shipped:
        item_weight = int(input("Please add the weight of the item (0 to exit): "))

        # Check if the user wants to exit
        if item_weight == 0:
            print("Exiting. Summary:")
            break

        # Check if item weight is within the valid range
        if item_weight < MIN_WEIGHT or item_weight > MAX_WEIGHT:
            print("Please enter a weight between 1 and 10.")
            continue

        # Increment the count of correctly weighted items
        correct_weight_item += 1

        # Add item weight to the current package
        pck_weight += item_weight

        # Check if the current package is full
        if pck_weight > MAX_PCK_WEIGHT:
            # Deduct the current item weight from the current package
            pck_weight -= item_weight

            # Increase the count of packages sent
            num_of_pck_sent += 1

            # Update the total weight sent
            weight_sent += pck_weight

            # Check if the current package is the lightest
            if pck_weight < lightest_pck:
                lightest_pck = pck_weight
                idx_most_empty_pck = num_of_pck_sent

            # Start a new package with the current item
            pck_weight = item_weight

    # Check if there is a remaining package to send
    if pck_weight > 0:
        num_of_pck_sent += 1
        weight_sent += pck_weight
        idx_most_empty_pck = num_of_pck_sent

    # Calculate the unused capacity
    unused_capacity = num_of_pck_sent * MAX_PCK_WEIGHT - weight_sent

    # Display the summary
    print("\nNumber of packages sent:", num_of_pck_sent)
    print("Total weight of packages sent:", weight_sent)
    print("Total unused capacity:", unused_capacity)
    print("Package with the most unused kilograms:", idx_most_empty_pck)

if __name__ == "__main__":
    main()