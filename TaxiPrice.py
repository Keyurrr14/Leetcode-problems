from tabulate import tabulate

def calculate_price(distance, rate_slabs):
    total_price = 0

    for slab in rate_slabs:
        lower_limit = slab['lower_limit']
        upper_limit = slab['upper_limit']
        price_per_km = slab['price_per_km']

        if upper_limit is None:
            distance_in_slab = max(0, distance - lower_limit)
        else:
            distance_in_slab = max(0, min(upper_limit, distance) - lower_limit)

        total_price += distance_in_slab * price_per_km

        if upper_limit is not None and distance <= upper_limit:
            break

    return total_price

def input_rate_slabs():
    rate_slabs = []
    while True:
        lower_limit = int(input("Enter lower limit for slab (Enter -1 to finish): "))
        if lower_limit == -1:
            break
        upper_limit_input = input("Enter upper limit for slab (Enter -1 for no upper limit): ")
        if upper_limit_input == "-1":
            upper_limit = None
        else:
            upper_limit = int(upper_limit_input)
        price_per_km = float(input("Enter price per km for this slab: "))
        rate_slabs.append({'lower_limit': lower_limit, 'upper_limit': upper_limit, 'price_per_km': price_per_km})
    return rate_slabs


trip_distance = int(input("Enter trip distance: "))
rate_slabs = input_rate_slabs()
table_data = []
for slab in rate_slabs:
    table_data.append([slab['lower_limit'], slab['upper_limit'], slab['price_per_km']])

head = ["Lower Limit", "Upper Limit", "Price per km"]
print(tabulate(table_data, headers=head, tablefmt="grid"))

price = calculate_price(trip_distance, rate_slabs)
print("Total Price:", price)