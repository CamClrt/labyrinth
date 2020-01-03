class Map():
    """à documenter"""

    #METHODES
    def __init__(self):
        #init map
        self.txt_file = "map.txt"
        self.map_structure = ""

    #ATTRIBUTES
    def generate_map(self):
        """Pick the file wich contains map and generate it in a list"""
        with open(self.txt_file,encoding="UTF-8") as file_content: #Open the file
            level_structure = []
            for line in file_content: #Read the file and put it in a list
                level_line = [element for element in line if element != '\n']
                level_structure.append(level_line)
            self.map_structure = level_structure #Update the map_structure attribute

    def display_map(self):
        """Display the map on screen"""
        with open(self.txt_file,encoding="UTF-8") as file_content: #Open the file
            display_file = file_content.read()
        return display_file