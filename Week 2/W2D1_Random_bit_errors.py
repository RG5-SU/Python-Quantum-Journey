import random


original_bit = int(input("Enter a bit to transmit, 0 or 1: "))
error_probability = float(
    input("Enter the probability of an error, from 0 to 1: ")
)

number_of_transmissions = 10


if (
    (original_bit == 0 or original_bit == 1)
    and error_probability >= 0
    and error_probability <= 1
):
    error_count = 0

    for transmission_number in range(1, number_of_transmissions + 1):
        received_bit = original_bit
        random_number = random.random()

        if random_number < error_probability:
            received_bit = received_bit ^ 1
            status = "FLIPPED"
            error_count = error_count + 1
        else:
            status = "NO ERROR"

        print(
            "Transmission", transmission_number,
            "| Random number:", round(random_number, 3),
            "| Received bit:", received_bit,
            "|", status
        )

    observed_error_rate = error_count / number_of_transmissions

    print()
    print("Total transmissions:", number_of_transmissions)
    print("Total errors:", error_count)
    print("Observed error rate:", round(observed_error_rate * 100, 1), "%")

else:
    print("Invalid input.")







            
