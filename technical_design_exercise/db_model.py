# Create a database model for tracking team sporting events.
# Your model must include a way to track athletes, teams, and players
# (athletes who are on teams). Additionally, your model must support
# tracking for match results over time. Use whatever notation you feel
# most comfortable.

# My clarifications/ process:
#   Can there be multiple matches in an event?
#   What if there is a tie?
#   I drew out a diagram of the database...


# The classes listed below are respresentations of a database model. They are in
# vanilla python. This is just a basic concept. Since these classes are not associated
# with a database joining/ connecting the tables would be done through class methods


class Team:
    """Sports team"""

    def __init__(self, name, wins=0, losses=0, ties=0, rank=None):
        """Creates an instance of a team from name."""
        self.name = name
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.rank = rank
        self.players = []

    def __repr__(self):
        """Returns a string representing instance."""
        return f"<Team name={self.name} wins={self.wins} losses={self.losses} ties={self.ties} rank={self.rank}>"

    def update_team_status(self, keyword):
        """Updates the status of win, loss or ties for a team."""
        if keyword == "win":
            self.wins += 1
        elif keyword == "loss":
            self.loss += 1
        elif keyword == "tie":
            self.ties += 1
        else:
            return f"Please use the keywords 'win', 'loss', or 'tie' to update the assocaited  status of the {self.name}"

    def add_player(self, player):
        """Adds a player instance to the set of team players and updates player instance with team."""

        if player not in self.players:
            self.players.append(player)
            player.add_team(self)

    def highest_ranking_team(cls, teams):
        """Returns highest ranking team"""
        highest = None
        for team in teams:
            if highest is None or (team.rank is not None and team.rank < highest.rank):
                highest = team
        return highest


class Event:
    """Creates an instance of an event."""

    def __init__(self, name):
        self.name = name
        self.location
        self.date
        self.start_time
        self.event_winner


class Player:
    """Sports player"""

    def __init__(self, name):
        """Creates an instance of a player. """
        self.name = name
        self.age = None
        self.team = None
        self.rank = None
        self.photo = None

    def add_to_team(self, team):
        """Updates a player instance with a team and team instance with the player."""

        if self.team is not team:
            self.team = team
            team.players.append(self)
