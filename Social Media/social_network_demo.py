
from facade.social_network_facade import SocialNetworkFacade


social_network = SocialNetworkFacade()

print("---creating users ------")
sundar  = social_network.create_user("max","max@ac.in")
bob     = social_network.create_user("bob","bob@ac.in")
alice   = social_network.create_user("alice","alice@ac.in")

print(f"creating users : {sundar.get_name() , bob.get_name(), alice.get_name()} ")
