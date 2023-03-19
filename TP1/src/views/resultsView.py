import arcade
from src.utils import get_solution_steps, get_frontier_nodes

class ResultsView(arcade.View):
    
    def __init__(self, visited, solution, time, bfs, N):
        """ Set up the application. """
        super().__init__()
        self.visited = visited
        self.solution = solution
        self.time = time
        self.bfs = bfs
        self.N = N
        self.ALGORITHM = self.window.algorithm_type
        self.HEURISITC = self.window.heuristic_type

    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        self.clear()

        if self.ALGORITHM == 'GREEDY' or self.ALGORITHM == 'A*':
            arcade.draw_text(f"Results with {self.ALGORITHM} and heuristic '{self.HEURISITC}'",
                            self.window.width / 2, 
                            self.window.height - (self.window.width/12),
                            arcade.color.WHITE, 
                            font_size=self.window.width/22, 
                            anchor_x="center", 
                            font_name="Kenney Future", 
                            multiline=True, 
                            align="center", 
                            width=self.window.width - 20)
        else: 
            arcade.draw_text(f"Your results with {self.ALGORITHM}",
                            self.window.width / 2, 
                            self.window.height - (self.window.width/12),
                            arcade.color.WHITE, 
                            font_size=self.window.width/22, 
                            anchor_x="center", 
                            font_name="Kenney Future", 
                            multiline=True, 
                            align="center", 
                            width=self.window.width - 20)

        arcade.draw_text(f"Board dimension: {self.N}x{self.N}\n"
                         f"Solution cost: {len(self.solution)} turns\n"
                         f"Frontier nodes: {get_frontier_nodes(self.visited)} nodes\n"
                         f"Expanded nodes: {len(self.visited)} nodes\n"
                         f"Processing time: {self.time} ms\n"
                         f"Solution steps: {get_solution_steps(self.solution)}\n",
                         self.window.width / 2, 
                         self.window.height / 2+(self.window.width/7),
                         arcade.color.WHITE, 
                         font_size=self.window.width/26, 
                         anchor_x="center",
                         multiline=True, 
                         align="left", 
                         width=self.window.width - 50)