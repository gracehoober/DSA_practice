# Create a database model for tracking team sporting events.
# Your model must include a way to track athletes, teams, and players
# (athletes who are on teams). Additionally, your model must support
# tracking for match results over time. Use whatever notation you feel
# most comfortable.

# My clarifications:
#    Can there be multiple matches in an event?
#    What if there is a tie?



# from flask_sqlachemy import SQLAlchemy
class Team:
    """Sports team"""

    def __init__(self, name):
        """Creates an instance of a team from name."""
        self.name = name
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.rank = None

    def __repr__(self):
        """Returns a string representing instance."""
        return f"<Team name={self.name} wins={self.wins} losses={self.losses} ties={self.ties} rank={self.rank}>"

    @classmethod
    def update_team_status(self):
        """Updates the total wins for a team."""
        self.wins += 1

    @staticmethod
    def highest_ranking_team(cls, teams):
        """Returns highest ranking team"""
        highest = None
        # TODO:MORE CODE HERE
        return highest

class Events:
    """Creates an instance of an event."""
    def __init__(self, name):
        self.name = name


# class Athletes:
#     """Creates an instance of an athlete. """
#     def __init__(self, name):
#         self.name = name

class Players:
    """Creates an instance of a player. """

    def __init__(self, name):
        self.name = name

    is_on_a_team = False
