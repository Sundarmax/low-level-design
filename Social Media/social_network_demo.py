
from facade.social_network_facade import SocialNetworkFacade

social_network = SocialNetworkFacade()

print("---creating users ------")
sundar  = social_network.create_user("max","max@ac.in")
bob     = social_network.create_user("bob","bob@ac.in")
alice   = social_network.create_user("alice","alice@ac.in")
print(f"creating users : {sundar.get_name() , bob.get_name(), alice.get_name()} ")

print("-------building friendship ----")
social_network.add_friend(sundar.get_id(),bob.get_id())
social_network.add_friend(bob.get_id(),alice.get_id())
print(f" {sundar.get_name() , bob.get_name()} are now friends")
print(f" {bob.get_name() , alice.get_name()} are now friends")

print("-------creating the post ------")
sundar_post = social_network.create_post(sundar.get_id(),"Hello from sundar")
bob_post = social_network.create_post(bob.get_id(), "Hello from bob")
sundar_post2 = social_network.create_post(sundar.get_id(), "Hello ! It's me SUNDAR")

print("-----user interaction with post ------")
social_network.like_post(bob.get_id(),sundar_post.get_id())
social_network.like_post(sundar.get_id(), bob_post.get_id())


print("------------viewing the news feed ----------")
bobs_feed = social_network.get_news_feed(bob.get_id())
bobs_feed = [b.get_content() for b in bobs_feed]
print("bobs feed - >", bobs_feed)
