"""
Q5 - Functions, Parameters and Scope
Run: python q5_functions_scope.py
"""

def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):
    # Completed TODO 1: create a fresh list when no list is supplied.
    if order is None:
        order = []
    order.append(item)
    return order


def calculate_bill(amount, gst_rate=0.05):
    gst = amount * gst_rate
    total = amount + gst
    return total, gst


def scope_examples():
    global global_counter
    global_counter += 1
    local_message = "This name exists only inside this function."

    count = 10

    def inner():
        nonlocal count
        count += 1
        return count

    print("local:", local_message)
    print("nonlocal inner result:", inner())
    print("nonlocal updated value:", count)
    print("global counter updated:", global_counter)


global_counter = 0


def make_order_manager():
    """Closure alternative: each returned add function owns its own order list."""
    order = []

    def add(item):
        order.append(item)
        return order.copy()

    return add


def main():
    print("BUGGY DEFAULT LIST")
    print(add_item_buggy("Tea"), add_item_buggy("Vada"))
    print("defaults after calls:", add_item_buggy.__defaults__)

    print("\nCORRECTED FUNCTION")
    print(add_item("Tea"), add_item("Vada"))

    print("\nTHREE INDEPENDENT CUSTOMERS")
    customer_orders = []
    for customer, items in [
        ("Customer 1", ["Tea", "Vada"]),
        ("Customer 2", ["Coffee"]),
        ("Customer 3", ["Juice", "Sandwich"]),
    ]:
        order = []
        for item in items:
            order = add_item(item, order)
        customer_orders.append((customer, order))
    for customer, order in customer_orders:
        print(customer, "->", order)

    print("\nRETURNING TWO VALUES")
    total, gst = calculate_bill(200, gst_rate=0.05)
    print(f"Total = Rs{total:.2f}, GST = Rs{gst:.2f}")

    print("\nSCOPE")
    scope_examples()
    print("global_counter outside function:", global_counter)

    print("\nCLOSURE ALTERNATIVE")
    customer_a = make_order_manager()
    customer_b = make_order_manager()
    print("A:", customer_a("Tea"))
    print("B:", customer_b("Coffee"))
    print("A:", customer_a("Vada"))

    print("\nPARAMETER GUIDANCE")
    print("Positional: add_item('Tea')")
    print("Keyword: calculate_bill(200, gst_rate=0.05)")
    print("Default: calculate_bill(200) uses the default GST rate.")
    print("Explicit list passing and closures both keep customer orders independent.")
    print("Appending one item is O(1) amortised; each customer's list uses O(m) space for m items.")


if __name__ == "__main__":
    main()
