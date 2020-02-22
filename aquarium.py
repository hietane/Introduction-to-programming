# TIE-02101 Programming 1: Introduction
# Ari Hietanen

MAXPH = 8.0
MINPH = 6.0


def main():
    """
    This function calculates if the water of a tank is suitable for zebra fishes. For the
    fishes to survive, The pH must be between 6 and 8 and in addition the difference between
    two consecutive measurements must be lesser or equal to 1.
    :return: None
    """
    # Ask for the amount of measurements + checks if the amount given is greater than 0.
    amount = int(input("Enter the number of the measurements: "))
    if amount <= 0:
        print("Error: the number must be expressed as a positive integer.")

    else:
        # Ask for a new pH value of the water for "amount" times.
        results = []
        for i in range(0, amount):
            result_n = float(input(f"Enter the measurement result {i+1}: "))
            results.append(result_n)

            # If the difference between the previous and current measurement was >1 or a value was not within
            # [MAXPH, MINPH], the loop breaks.
            if result_n < MINPH or result_n > MAXPH or results[i]-results[i-1] > 1 or results[i-1]-results[i] > 1:
                print("The conditions are not suitable for zebra fishes.")
                break

        # If the loop was broken, the following message won't be printed
        if len(results) == amount and abs(results[amount-1] - results[amount-2]) <= 1:
            average = sum(results)/len(results)
            print(f"Conditions are suitable for zebra fishes. The average pH is {average:.2f}.")


main()
