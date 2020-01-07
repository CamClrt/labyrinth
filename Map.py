class Map():
    """à documenter"""

    #ATTRIBUTES
    def __init__(self):
        #init map
        self.txt_file = "map.txt"
        #a revoir = mettre l'url dans data > main tapper dans data + objet

    #METHODES
    def display_map(self):
        """Display the map on screen"""
        with open(self.txt_file,encoding="UTF-8") as file_content: #Open the file
            display_file = file_content.read()
        return display_file

    def generate_maplist(self):
        """Pick the file wich contains map and generate it in a list"""
        with open(self.txt_file,encoding="UTF-8") as file_content: #Open the file
            level_structure = []
            for line in file_content: #Read the file and put it in a list
                level_line = [element for element in line if element != '\n']
                level_structure.append(level_line)
        return level_structure