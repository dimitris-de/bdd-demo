class Train:
    def __init__(self, train_type, carriages):
        self.train_type = train_type
        self.carriages = carriages
        
        # Dictionary storing the seating capacity of each carriage for different types of trains
        self.capacity_per_carriage = {
            "Tube": 28,
            "SouthWestRail": 50,
            "Eurostar": 80
        }

        # Validate the train type
        if train_type not in self.capacity_per_carriage:
            raise ValueError(f"Unknown train type: {train_type}. Valid types are: {', '.join(self.capacity_per_carriage.keys())}")

    def calculate_capacity(self, passengers):
        """
        Calculate the total capacity of the train and determine if it is sufficient
        for the number of passengers.
        """
        # Fetch capacity per carriage based on train type
        capacity_per_carriage = self.capacity_per_carriage[self.train_type]
        total_capacity = self.carriages * capacity_per_carriage
        
        # Return whether the train has sufficient or insufficient capacity
        return "Sufficient" if passengers <= total_capacity else "Insufficient"

    @staticmethod
    def calculate_carriage_capacity(seats, passengers):
        """
        Determine if a single carriage's capacity is sufficient for the given number of passengers.
        """
        return "Sufficient" if passengers <= seats else "Insufficient"
