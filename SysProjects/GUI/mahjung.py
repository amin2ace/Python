import customtkinter as ctk
from random import shuffle

class MahjongGame:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title('Mahjong Game')

        self.tiles = []
        for suit in ['bamboo', 'dots', 'characters']:
            for number in range(1, 10):
                self.tiles.append(suit + str(number))

        shuffle(self.tiles)

        self.player_tiles = [1,2,3,4,5,6,7,8,9,10]
        self.wall = 'abcdefghjk'

        # Draw the player's tiles
        player_frame = ctk.CTkFrame(self.root, width=200, height=300)
        player_frame.pack()

        for row in range(3):
            for col in range(10):
                tile_label = ctk.CTkLabel(player_frame, text=self.player_tiles[col])
                tile_label.grid(row=row, column=col)

        # Draw the wall tiles
        wall_frame = ctk.CTkFrame(self.root, width=100, height=200)
        wall_frame.pack()

        for row in range(2):
            for col in range(10):
                tile_label = ctk.CTkLabel(wall_frame, text=self.wall[col])
                tile_label.grid(row=row, column=col)

        # Handle tile drawing
        self.draw_tiles()

        # Start the game loop
        self.root.mainloop()

    def draw_tiles(self):
        # Clear existing tiles
        for tile in self.player_tiles:
            tile.destroy()

        for tile in self.wall:
            tile.destroy()

        # Randomly select tiles for the player and wall
        for _ in range(14):
            self.player_tiles.append(self.tiles.pop())
            self.wall.append(self.tiles.pop())

        # Draw the new player's tiles
        player_frame = self.root.children['Player Frame']
        player_frame.destroy()
        player_frame = ctk.CTkFrame(self.root, width=200, height=300)
        player_frame.pack()

        for row in range(3):
            for col in range(10):
                tile_label = ctk.CTkLabel(player_frame, text=self.player_tiles[col])
                tile_label.grid(row=row, column=col)

        # Draw the new wall tiles
        wall_frame = self.root.children['Wall Frame']
        wall_frame.destroy()
        wall_frame = ctk.CTkFrame(self.root, width=100, height=200)
        wall_frame.pack()

        for row in range(2):
            for col in range(10):
                tile_label = ctk.CTkLabel(wall_frame, text=self.wall[col])
                tile_label.grid(row=row, column=col)

if __name__ == '__main__':
    MahjongGame()
