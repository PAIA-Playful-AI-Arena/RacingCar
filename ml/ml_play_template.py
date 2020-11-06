class MLPlay:
    def __init__(self, player):
        self.player = player
        if self.player == "player1":
            self.player_no = 0
        elif self.player == "player2":
            self.player_no = 1
        elif self.player == "player3":
            self.player_no = 2
        elif self.player == "player4":
            self.player_no = 3
        self.other_cars_position = []
        self.coins_pos = []
        print("Initial ml script")

    def update(self, scene_info: dict):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] == "RUNNING":
            self.car_pos = scene_info["player_" + str(self.player_no) + "_pos"]

        self.other_cars_position = scene_info["cars_pos"]
        if scene_info.__contains__("coin"):
            self.coin_pos = scene_info["coin"]

        if scene_info["status"] == "END":
            return "RESET"

        return ["MOVE_LEFT", "SPEED"]

    def reset(self):
        """
        Reset the status
        """
        print("reset ml script")
        pass
