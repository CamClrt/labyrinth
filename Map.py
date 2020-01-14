class Map():
    """create the structure of the labyrinth thanks to the source map.txt"""

    def __init__(self,url_map):
        """init map"""
        self.txt_file = url_map

    def generate_maplist(self):
        """pick the file wich contains map and generate it in a list"""
        with open(self.txt_file,encoding="UTF-8") as file_content: # Open the file
            level_structure = []
            for line in file_content: # Read the file and put it in a list
                level_line = [element for element in line if element != '\n']
                level_structure.append(level_line)
        return level_structure