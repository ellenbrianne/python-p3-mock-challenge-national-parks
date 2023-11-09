class NationalPark:
    all = []
    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

        self._trips = []
        self._visitors = []

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if type(name) is str and 3 <= len(name) and not hasattr(self, "name"):
            self._name = name
        else:
            print("Name must be a string greater than or equal to 3 characters.")
        
    def trips(self):
        return self._trips
    
    def visitors(self):
        return list(set(self._visitors))
    
    def total_visits(self):
        return len(self._trips)
    
    def best_visitor(self):
        if len(self._visitors) == 0:
            return None
        
        return max(self._visitors, key=self._visitors.count)

    @classmethod
    def most_visited(cls):
        curr_park = None
        curr_max_visits = 0

        for national_park in cls.all:
            if len(national_park._trips) > curr_max_visits:
                curr_park = national_park 
                curr_max_visits = len(national_park._trips)
            
        return curr_park

class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
        
        visitor._trips.append(self)
        visitor._national_parks.append(national_park)

        national_park._trips.append(self)
        national_park._visitors.append(visitor)

    @property
    def visitor(self):
        return self._visitor
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            print("Visitor must be an instance of Visitor class.")

    @property
    def national_park(self):
        return self._national_park
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            print("National park must be an instance of NationalPark class.")

    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self, start_date):
        if type(start_date) is str and len(start_date) >= 7:
            self._start_date = start_date
        else:
            print("Start date must be a string greater than or equal to 7 characters.")
            
    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self, end_date):
        if type(end_date) is str and len(end_date) >= 7:
            self._end_date = end_date
        else:
            print("End date must be a string greater than or equal to 7 characters.")

class Visitor:
    all = []
    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)

        self._trips = []
        self._national_parks = []

    @property 
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if type(name) == str and 1 <= len(name) <= 15:
            self._name = name
        else:
            print("Name must be a string between 1 and 15 characters.") 
        
    def trips(self):
        return self._trips
    
    def national_parks(self):
        return list(set(self._national_parks))

    # not tested for but valuable to have
    # def total_visits_at_park(self, park):
    #     return len([trip for trip in self._trips if trip.national_park == park])