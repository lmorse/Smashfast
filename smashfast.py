from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finalscene')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [
        "Muwwah ha ha ha!  You die!!!  Ripley will be so disappointed!!!!",
        "Not a good choice and you're way too slow!!!  RIP Furiosa!!!",
        "Too bad, you die!  You will make a tasty treat Zombie Bunnies!!!",
        "Words can't describe your incompetence, so I'll just throw up and kill you!!!"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class Opening_Scene(Scene):

    def enter(self):
        print "The Tardis is spinning out of control in the cosmos. It explodes"
        print "unexpectedly ending our entire universe both real and imagined"
        print "into one cosmic paradox."
        print "Ready for an adventure? Press ENTER to continue, or CRTL + C to"
        print "turn back now..."
        raw_input("> ")
        
        print "Like waking up from a dream we see Furiosa from Mad Max opening"
        print "up and standing to see the island of Jurassic Park for the first"
        print "time.  Confused and fearful by the strange sounds and sights she"
        print "is pulled to a long lost familiar ring of a free-standing NYC"
        print "payphone. It's a little sticky and revolting, but she answers it"
        print "anyway..."
        print "\n"
        print "\"Hello? \""
        print "\n"
        print "The voice on the other end is authoritative and insistent."
        print "\" You don't know me but my name is Ripley. You need to move"
        print "fast and collect as many weapons as possible. There is a very"
        print "nasty alien stalking you with acid for blood and a tail that"
        print "will slice you in half. Get to me as fast as you can, there is a"
        print "thing called an iPhone on the ground next to you...it will help"
        print "you, bring it to me. Look ahead, do you see a Rock Candy"
        print "Mountain? I'm at the top, it is safe here! \""
        return 'scene1'

class Scene_1(Scene):

    def enter(self):
        print "Furiosa picks up the iPhone, and a nearby backpack that has"
        print "several weapons and some essentials. She looks at the iPhone and"
        print "is mesmerized momentarily by the game Candy Crush. Her attention"
        print "quickly shifts to the sky, because from overhead a pterodactyl"
        print "approaches and she reaches into her backpack to find a shotgun."
        print "\n"
        print "Choose: 'shoot', 'throw the iPhone' or 'run away'?"

        action = raw_input("> ")
        
        if action == "shoot":
            print "Furiosa fires away and blows the pterodactyl to pieces."
            print "She turns to see a strange looking machine called a Segway!"
            print "Looking closely at it, it's covered in blood and says"
            print "'Property of Segway Steve'. She shrugs and gets on the"
            print "segway and proceeds towards the forest."
            return 'scene2'

        elif action == "throw the iPhone":
            print "Furiosa winds up and hurls the iPhone at the pterodactyl."
            print "But it ends up being more of a easy lob in the dinosaur's"
            print "general direction. The pterodactyl laughs and screeches: \""
            print "ANDROID WILL PREVAIL!\" and eats Furiosa."
            return 'death'

        elif action == "run away":
            print "Furiosa sprints away from the pterodactyl but only makes it"
            print "three steps before the giant ancient pterosaur swoops down"
            print "and gobbles her up."
            return 'death'

        else:
            print "DOES NOT COMPUTE!"
            return 'scene1'

class Scene_2(Scene):

    def enter(self):
        print "As she rolls on her segway to the Forest she meets a friend. A life size Gummy "
        print "Bear peaks from around the tree and joins on her journey."  
        print "They soon hear a rustling up ahead in the trees. The Gummy runs"
        print "ahead thinking it's his friend. Furiosa rides to protect her"
        print "friend and the two are surprised to see an Alien standing in"
        print "front of them. The Alien jumps on the Gummy Bear and tries to eat it."
        print "The alien gets stuck in the GOO of the Gummy Bear, giving Furiosa"
        print "a chance to arm herself or run."
        print "\n"
        print "Choose: 'save' the Gummy Bear, 'shoot' the alien, 'drive' away on the segway" 

        action = raw_input("> ")

        if action == "drive":
            print "She drives away on the segway."
            return 'scene3'

        elif action == "shoot":
            print "She uses the shotgun and gets sprayed by acid."
            return 'death'

        elif action == "save":
            print "She tries to save her friend and gets sliced in half by the Alien's tail."
            return 'death'

        else:
            print "DOES NOT COMPUTE!"
            return 'scene2'

class Scene_3(Scene):

    def enter(self):
        print "She approaches a meadow at the edge of the forest.  She sees" 
        print "Hillary Clinton and Michelle Obama running to the doorway of the"
        print "White House in the middle of the meadow. The first ladies call" 
        print "Furiosa for help just as a family of Raptors fly in, catch them,"
        print "and rip them to pieces. As she approaches the White House she"
        print "loses control when her segway is cut in half under her feet."
        print "She falls to the side to look back and see a huge BuZZ SAW"
        print "monster coming up from under the ground. She reaches into the"
        print "backpack and finds a Nerf supersoaker filled with water."
        print "\n"
        print "Choose: 'supersoaker' to spray the monster, 'shoot' to use the shotgun,"
        print "'run' to run away"

        action = raw_input("> ")

        if action == "supersoaker":
            print "She sprays the monster and it rusts and crumbles."
            return 'scene4'

        elif action == "shoot":
            print "She ignores the nerf gun and tries to use the shotgun again."
            return 'death'

        elif action == "run":
            print "She runs away but the monster is too fast."
            return 'death'

        else:
            print "DOES NOT COMPUTE!"
            return 'scene3'

class Scene_4(Scene):

    def enter(self):
        print 'She runs to the White House and up to the roof where a Pod Racer sits on the helipad.'
        print 'She gets on and races towards Rock Candy Mountain. Ripley calls her and she sets the '
        print 'IPhone on a safe hands free driving holder.'
        print 'Ripley warns: "Be careful of the tunnel. Use the IPhone to locate me on the mountain."'
        print 'Furiosa: "I can\'t it seems to be stuck on some stupid Candy Crush game!"'
        print 'Ripley: "Don\'t touch it - I have a Sonic Screwdriver, that will fix it. Just keep moving"'
        print 'the Alien is on your tail!  Furiosa approaches the base of the Rock Candy Mountain and see\'s'
        print 'the tunnel. She looks back to see the Alien chasing her.'
        print '\n'
        print 'The Mountain is a towering formation of hard Rock Candy crystals with a tunnel at the base.'
        print 'She gets off the Pod Racer but notices a Bazooka gun that she thinks will come in handy so'
        print 'she takes it and proceeds into the tunnel.  The tunnel quickly splits into two paths.'
        print 'The Blue crystal tunnel is covered in cheesy spider webs, being lactose intolerant and a'
        print 'bit arachnophobic she hesitates. The Red Crystal tunnel seems clear so she proceeds.'
        print 'Around the bend she hears a robotic voice saying "EXTERMINATE" and she is confronted by a Darlek.'
        print "\n"
        print "Choose: 'run' the other way, 'shoot' at the Darlek, 'iPhone' for help"

       action = raw_input("> ")

       if action == "run":
           print "She runs the other way to the Blue Crystal tunnel."
           return 'finalscene'

       elif action == "shoot":
           print "She shoots at the Darlek but all it shoots is Blow Pops, so it\'s useless."
           return 'death'

       elif action == "iPhone":
           print "She pulls out the IPhone to see if there is another path, but gets mesmerized by Candy Crush and gets exterminated."
           return 'death'

       else:
           print "DOES NOT COMPUTE!"
           return 'scene4'

class Scene_5(Scene):

    def enter(self):
        print "She breaks through the Cheesy Spider webs and sees an elevator"
        print "at the end of the tunnel. She gets in and heads to the top of"
        print "the mountain not knowing that the Alien is hiding on the"
        print "elevator roof. Ripley and Furiosa come face to face at the top"
        print "of the Rock Candy Mountain. They share a snack of"
        print "Twizzlers and Pixie Sticks. Just then the Alien jumps down to"
        print "attack but Ripley pulls out a sniper rifle to fight back. It"
        print "only shoots pixie sticks and is useless. In desperation,"
        print "Furiosa throws the iPhone at the Alien who catches it and is"
        print "mesmerized by Candy Crush. The Alien eyes are so fixed on the"
        print "screen it starts to suck him into the phone and it sucks him in"
        print "to another dimension. With the Alien gone the two feel safe and"
        print "we think the game is won. HOWEVER..."
        print "\n"
        print "Choose: 'sonicscrewdriver' to fix the iPhone, 'play' Candy Crush"  

        action = raw_input("> ")

        if action == "sonicscrewdriver":
            print "Ripley pulls out a Sonic Screwdriver and points it at the"
            print "iPhone to fix it. This action creates a patch in the cosmic"
            print "rip caused by the Tardis and the Universe is repaired!"
            return 'finalscene'

        elif action == "play":
            print "Furiosa picks up the iPhone that has just sucked in the"
            print "Alien and presses “Invite” to Ripley so that they can play."
            print "Both are sucked into the phone and die."
            return 'death'

        else:
            print "DOES NOT COMPUTE!"
            return 'scene5'

class Final_Scene(Scene):

    def enter(self):
        print "The Universe is repaired! You saved the world! YOU WON!"
        f = open('image.txt', 'r')
        print f.read()
        exit()

class Map(object):

    scenes = {
        'openingscene': Opening_Scene(),
        'scene1': Scene_1(),
        'scene2': Scene_2(),
        'scene3': Scene_3(),
        'scene4': Scene_4(),
        'scene5': Scene_5(),
        'finalscene': Final_Scene(),
        'death': Death(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('openingscene')
a_game = Engine(a_map)
a_game.play()
