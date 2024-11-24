from behave import given, when, then  # type: ignore
from src.service.MyTrainApp import Train

# Create a Train instance for the specified type of train and number of carriages
@given('a "{train_type}" train with {carriages:d} carriages')
def step_given_train(context, train_type, carriages): 
    # We create an instance of a Train and store it in context.train
    context.train = Train(train_type, carriages)

# Calculate train capacity with the specified number of passengers
@when('{passengers:d} passengers are onboard')
def step_when_passengers_onboard(context, passengers):
    # Calculate whether the train can accommodate the passengers using calculate_capacity
    context.result = context.train.calculate_capacity(passengers)
    context.passengers = passengers  # Store passengers for use in subsequent steps


# Verify if the train has sufficient or insufficient capacity
@then('the train should have "{expected_capacity}" capacity')
def step_then_train_capacity(context, expected_capacity):
    # Assert that the result matches the expected capacity (e.g., "Sufficient" or "Insufficient")
    assert context.result == expected_capacity, f"Expected {expected_capacity} but got {context.result}"

# Verify if adding a carriage would make capacity sufficient
@then('an additional carriage can be added to accommodate the passengers')
def step_then_add_carriage(context):
    print("Train:", vars(context.train))
    print("Passengers:", context.passengers)
    # Simulate adding one additional carriage and recalculate the capacity
    additional_carriages = 1
    train = context.train
    total_capacity = (train.carriages + additional_carriages) * train.capacity_per_carriage[train.train_type]
    assert context.passengers <= total_capacity, (
        "Even with an additional carriage, capacity is insufficient"
    )

# Store train setups from a table
@given('the following train setups')
def step_given_train_setups(context):
    print("Context Table:", context.table)
    context.trains = []
    for row in context.table:
        train = Train(row['train_type'], int(row['carriages']))
        passengers = int(row['passengers'])
        context.trains.append((train, passengers))


# Assess capacity for multiple trains
@when('the trains are assessed for capacity')
def step_when_assess_multiple_trains(context):
    # We iterate over the stored train configurations, calculate the capacity for each, and store the results
    context.results = []
    for train, passengers in context.trains:
        result = train.calculate_capacity(passengers)
        context.results.append({"train_type": train.train_type, "capacity": result})

# Verify capacity results for multiple trains using a table
@then('the results should be')
def step_then_assess_results(context):
    print("Actual Results:", context.results)
    print("Expected Results Table:", context.table)
    # Compare the actual results with the expected results
    # The zip function in Python is a built-in utility that allows you to iterate over 
    # multiple iterables (like lists, tuples, etc.) in parallel, pairing up elements 
    # from each iterable based on their positions
    for actual, expected in zip(context.results, context.table):
        assert actual["capacity"] == expected["capacity"], (
            f"Expected {expected['capacity']} but got {actual['capacity']} for train type {actual['train_type']}"
        )
