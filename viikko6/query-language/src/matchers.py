
class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value
class All:
    def __init__(self):
        pass

    def test(self,player):
        return True
class Not:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return True

        return False
class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

class QueryBuilder:
    def __init__(self, matchers = All())->None:
        self._matcher=matchers

    def playsIn(self, team):
        return QueryBuilder(And(self._matcher,PlaysIn(team)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matcher,HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matcher,HasFewerThan(value, attr)))
    
    def build(self):
        return self._matcher
    
    def oneOf(self, m1, m2):
        one_of = QueryBuilder(Or(m1, m2))
        return one_of