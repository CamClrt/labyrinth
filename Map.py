class Map():
    """to create the structure of the labyrinth thanks to the source map.txt"""

    #ATTRIBUTES
    def __init__(self,url_map):
        """init map"""
        self.txt_file = url_map

    #METHODES
    def display_map(self):
        """display the map on screen"""
        with open(self.txt_file,encoding="UTF-8") as file_content: #Open the file
            display_file = file_content.read()
        return display_file

    def generate_maplist(self):
        """pick the file wich contains map and generate it in a list"""
        with open(self.txt_file,encoding="UTF-8") as file_content: #Open the file
            level_structure = []
            for line in file_content: #Read the file and put it in a list
                level_line = [element for element in line if element != '\n']
                level_structure.append(level_line)
        return level_structure

    """     line_rank = 0
            for line in map_list:
                element_rank = 0
                for element in line:
                    if map_list[line_rank][element_rank] == "Wall":
                        window.blit(wall, (40, 0), (160,160,40,20))
                        window.blit(wall, (40, 20), (160,160,40,20))
                    element_rank += 1
                line_rank += 1"""