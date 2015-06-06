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
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
         "Your mom would be proud...if she were smarter.",
         "Such a loser.",
         "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class Opening_Scene(Scene):

    def enter(self):
        print "opening scene text here"
        return 'scene1'

class Scene_1(Scene):

    def enter(self):
        print "description of scene 1"

        action = raw_input("> ")

        if action == "option_a":
            print "outcome of option_a"
            return 'scene2'

        elif action == "option_b":
            print "outcome of option_b"
            return 'death'

        elif action == "option_c":
            print "outcome of option c"
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
       print "Scene 4 description"

       action = raw_input("> ")

       if action == "option_a":
           print "Option A description"
           return 'finalscene'

       elif action == "option_b":
           print "Option B description"
           return 'death'

       elif action == "option_c":
           print "Option C description"
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
