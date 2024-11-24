@train_capacity
Feature: Train Capacity Assessment

  # This feature ensures we can assess the capacity of different trains
  # and their carriages to determine if they can accommodate passengers

  # Remember:
  # - Tube has 28 seats per carriage, so 6 x 28 = 168 max capacity
  # - SouthWestRail has 50 seats per carriage
  # - Eurostar has 80 seats per carriage

  Scenario: Calculate capacity for a single train

    # Initialize a Train object and store it in context.train
    Given a "Tube" train with 6 carriages

    # Calculate whether the train can accommodate 160 passengers using calculate_capacity
    When 160 passengers are onboard

    # Assert that the result matches the expected capacity ("Sufficient" in this case)
    Then the train should have "Sufficient" capacity

  Scenario Outline: Assess train capacity with different train types

    # Initialize a Train object with the specified train type and number of carriages
    Given a "<train_type>" train with <carriages> carriages

    # Calculate whether the train can accommodate the given number of passengers
    When <passengers> passengers are onboard

    # Assert that the train's capacity matches the expected outcome (e.g., "Sufficient" or "Insufficient")
    Then the train should have "<expected_capacity>" capacity

    Examples:
      | train_type      | carriages | passengers | expected_capacity |
      | Tube            | 6         | 168        | Sufficient        |
      | Tube            | 6         | 170        | Insufficient      |
      | SouthWestRail   | 4         | 200        | Sufficient        |
      | SouthWestRail   | 4         | 250        | Insufficient      |
      | Eurostar        | 2         | 150        | Sufficient        |
      | Eurostar        | 2         | 170        | Insufficient      |

  Scenario: Assess train capacity with additional conditions

    # We initialize a Train object and store it in context.train
    Given a "Tube" train with 6 carriages

    # Calculate whether the train can accommodate the passengers using calculate_capacity
    When 170 passengers are onboard

    # Assert that the result matches the expected capacity ("Insufficient" in this case)
    Then the train should have "Insufficient" capacity

    # Simulate adding one additional carriage and recalculate the capacity
    # to ensure it can accommodate the passengers
    But an additional carriage can be added to accommodate the passengers

  Scenario: Assess multiple train capacities
      Given the following train setups:
        | train_type      | carriages | passengers |
        | Tube            | 6         | 168        |
        | SouthWestRail   | 4         | 200        |
        | Eurostar        | 2         | 150        |    
      When the trains are assessed for capacity
      Then the results should be:
        | train_type      | capacity    |
        | Tube            | Sufficient  |
        | SouthWestRail   | Sufficient  |
        | Eurostar        | Sufficient  |