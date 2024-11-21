image doll1 = Transform("images/minigames/dolls/bluebell.png",zoom=.25)
image doll2 = Transform("images/minigames/dolls/cubie.png",zoom=.25)
image doll3 = Transform("images/minigames/dolls/dustirian.png",zoom=.25)
image doll4 = Transform("images/minigames/dolls/honey.png",zoom=.25)
image doll5 = Transform("images/minigames/dolls/manta.png",zoom=.25)
image doll6 = Transform("images/minigames/dolls/huangyang.png",zoom=.25)
image P_pan = Transform("images/minigames/dolls/p_pan.png",zoom=.25)
image claw = Transform("images/minigames/dolls/doll_claw.png",zoom=.75)

init python:
    import random
    import time
    random.seed(time.time())

    def is_within_rectangle(x, y, rect):
        """Check if point (x, y) is within the specified rectangle."""
        x1, y1, x2, y2 = rect
        return x1 <= x <= x2 and y1 <= y <= y2


    class Doll:
        def __init__(self, x, y, image):
            self.x = x
            self.y = y
            self.image = image

        def reset(self, x, y):
            """Reset the doll's position."""
            self.x = x
            self.y = y

        def get_scaled_image(self):
            """Return the scaled image (load lazily)."""
            return self.image

        def contains(self, x, y):
            """Check if a point (x, y) is inside the doll's bounds."""
            return self.x + 160 <= x <= self.x + 320 and self.y + 130 <= y <= self.y + 382


    class DollBar(renpy.Displayable):
        def __init__(self, image):
            super().__init__()
            self.image = image
            self.x = 0
            self.y = 0
            self.x_direction = 8
            self.y_direction = 8  # Negative to move upward
            self.x_moving = False
            self.y_moving = False
            self.limit_x = 1360  # Horizontal limit
            self.limit_y = 640# Vertical limit for upward movement
            self.speed = 8

        def render(self, width, height, st, at):
            """Render the DollBar and handle movement."""

            # Handle horizontal movement boundaries
            if self.x > self.limit_x or self.x < 0:
                self.x_direction = -self.x_direction

            # Handle vertical movement boundaries (reverse if at top or bottom)
            if self.y < 0 or self.y > self.limit_y:  # Adjust for vertical limits
                self.y_direction = -self.y_direction

            # Move the DollBar if needed
            if self.x_moving:
                self.x += self.x_direction
            if self.y_moving:
                self.y += self.y_direction

            # Apply transformation and render
            t = Transform(self.image, xanchor=0.5, yanchor=0.5)
            child_render = renpy.render(t, width, height, st, at)
            rv = renpy.Render(*child_render.get_size())
            rv.blit(child_render, (self.x, self.y))

            renpy.redraw(self, 0)
            return rv



    class doll_game:
        def __init__(self, player_name):
            self.player_name = player_name
            self.coin = 0
            self.attempts_left = 3
            self.running = False
            self.winner = False
            self.collected_doll = None  # Track the collected doll

            # Initialize dolls with random positions and types only once when starting the screen
            self.dolls = []  # Initially empty

            # Initialize arrows
            self.claw = DollBar("claw")
            self.reset_game()

        def generate_dolls(self):
            """Generates dolls, ensuring 'P_pan' is included and randomly placed."""
            fixed_positions = [
                (25, 25), (1315, 25), (236, 25), (1315, 562),  # Corners
                (657, 25), (657, 552), (25, 293), (1315, 293),  # Middle points on sides
                (300, 333), (399, 25), (850, 225), (670, 289),  # Random points
                (1120, 25), (200, 186), (448, 511), (1100, 550), (300, 550),
                (800, 500), (1100, 300), (565, 200), (1050, 150), (800, 25),  # Random points
            ]

            # List of other doll types
            available_doll_types = ["doll1", "doll2", "doll3", "doll4", "doll5", "doll6"]

            # Shuffle the positions
            random.shuffle(fixed_positions)

            # Randomly select a position for "P_pan"
            p_pan_position = fixed_positions.pop()  # Remove one position for "P_pan"
            dolls = [Doll(p_pan_position[0], p_pan_position[1], "P_pan")]

            # Shuffle the other doll types to ensure variety
            random.shuffle(available_doll_types)

            # Assign remaining dolls to the positions
            for i, position in enumerate(fixed_positions):
                x_base, y_base = position
                doll_type = available_doll_types[i % len(available_doll_types)]  # Loop through doll types

                # Add a slight random offset within ±20 pixels for variety
                x = x_base + random.randint(-20, 20)
                y = y_base + random.randint(-20, 20)

                dolls.append(Doll(x, y, doll_type))

            return dolls


        def reset_game(self):
            """Reset the game state but keep the same dolls."""
            self.running = False
            self.coin = 0
            self.attempts_left = 3
            self.winner = False
            self.claw.x = 0
            self.claw.y = 0


            # Only generate dolls once when the game starts
            if not self.dolls:  # Generate dolls if they haven't been generated yet
                self.dolls = self.generate_dolls()

        def insert_coin(self):
            """Inserts a coin."""
            if self.coin < 3:
                self.coin += 3

        def start_game(self):
            """Starts the game after inserting coins."""
            if self.coin >= 3:
                self.running = True
                self.coin -= 3

        def throw(self):
            """Throws the arrow and checks for collision."""
            if self.attempts_left <= 0 or self.winner:
                return

            x = self.claw.x + 189
            y = self.claw.y + 180

            # Check collision with dolls
            for doll in self.dolls:
                if doll.contains(x, y):
                    self.collected_doll = doll
                    self.dolls.remove(doll)  # Remove the collected doll
                    if doll.image == "P_pan":
                        self.winner = True
                    break

            self.attempts_left -= 1
            self.claw.x = 0  # Reset bottom arrow position
            self.claw.y = 0

        def clicked(self):
            """Handles the arrow movement and throwing."""
            if self.claw.x_moving:
                self.claw.x_moving = False
                self.claw.y_moving = True
            elif self.claw.y_moving:
                self.claw.y_moving = False
                self.throw()
            else:
                self.claw.x_moving = True

screen doll_screen():
    default game = doll_game("Player 1")

    modal True

    if not game.running:
        for doll in game.dolls:
            add doll.get_scaled_image() xpos doll.x ypos doll.y
        vbox:
            align .5, .5
            if game.coin < 3:
                button:
                    background "#006"
                    insensitive_background "#eae4e4"
                    hover_background "#00a"
                    padding 20,20
                    text "Use 3 coins to START" color "#ed3d89"
                    action Function(game.insert_coin)
            else:
                button:
                    background "#006"
                    insensitive_background "#eae4e4"
                    hover_background "#00a"
                    padding 20,20
                    text "START GAME" color "#36d559"
                    action Function(game.start_game)


    if game.running:
        for doll in game.dolls:
            add doll.get_scaled_image() xpos doll.x ypos doll.y

        # Draw the arrows
        add game.claw align 0.0, 0.0

        vbox:
            align .5, .025
            text "[game.attempts_left]/3" align (0.5,0.5)
            if game.attempts_left <= 0:
                text "เอาใหม่ๆยังไม่ได้พี่แพนเลย" color "#f81528"
            else:
                text "คีบพี่แพนไปให้มายด์สิ" color "#2709cf"

    # Bind space key for throwing action
    if game.running and not (game.attempts_left <= 0 or game.winner):
        key "K_SPACE" action Function(game.clicked)
    if game.attempts_left <= 0:
        vbox:
            align .5, .5
            button:
                background "#006"
                insensitive_background "#eae4e4"
                hover_background "#00a"
                padding 20,20
                text "RETRY" color "#ac0303"
                action Function(game.reset_game)
    elif game.winner:
        timer 0.05 action Return()


label doll_game_center:
    scene doll_bg
    play music arcade_bgm
    $ quick_menu = False
    call screen doll_screen
    $ povname = "test"
    $ quick_menu = True
    jump act2_3_shot_4