from object_3d import *

class FileParser:
    def __init__(self, render, file_path):
        self.render = render
        self.path = file_path
        self.parse_file()

    def parse_file(self):
        self.read_file()
        self.find_type()
        if (self.type == 'MSH 2.2'):
            self.parse_msh_2_2()
        elif (self.type == 'MSH 4.1'):
            self.parse_msh_4_1()
        elif (self.type == 'OBJ'):
            self.parse_obj()
        elif (self.type == 'Unknown' or self.type == 'Not found'):
            print("no good file")
            self.object = Object3D(self.render, [], [])
    
    # format for this version of mesh files can be found here:
    # https://gmshparser.readthedocs.io/en/latest/mesh_formats.html
    # this is for the different type of shapes (third number per shape index):
    # https://www.manpagez.com/info/gmsh/gmsh-2.2.6/gmsh_63.php#SEC63
    def parse_msh_4_1(self):
        vertices, faces = [], []
        nodes_section = False
        faces_section = False
        select_triangles = False
        counter_faces = 0
        for line in self.file.split('\n'):
            if (line == '$Nodes'):
                nodes_section = True
            elif (line == '$EndNodes'):
                nodes_section = False
            elif (line == '$Elements'):
                faces_section = True
            elif (line == '$EndElements'):
                faces_section = False
            elif (line.startswith("2 1 ") and faces_section and len(line.split()) == 4): #2d shapes start here
                select_triangles = True 
            elif (line.startswith("3 1 ") and select_triangles and len(line.split()) == 4): #stop ones we see 3d shapes
                select_triangles = False
            elif (nodes_section):
                if line.strip():
                    if (len(line.split()) == 3):
                        values = [float(val) for val in line.split() + [1]]
                        vertices.append(values)
            elif (select_triangles):
                if line.strip():
                    if (line.split()[0] == '2' and line.split()[2] == '2' and counter_faces == 0):
                        counter_faces = line.split()[3]
                    if (line.split()[0] != '2'):
                        values = [int(val) - 1 for val in line.split()[1:]]
                        faces.append(values)
        self.object = Object3D(self.render, vertices, faces)
    
    def parse_obj(self):
        vertices, faces = [], []
        for line in self.file.split('\n'):
                if line.startswith('v '):
                    vertices.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        self.object = Object3D(self.render, vertices, faces)
        
    def parse_msh_2_2(self):
        vertices, faces = [], []
        nodes_section = False
        faces_section = False
        for line in self.file.split('\n'):
            if (line == '$Nodes'):
                nodes_section = True
            elif (line == '$EndNodes'):
                nodes_section = False
            elif (line == '$Elements'):
                faces_section = True
            elif (line == '$EndElements'):
                faces_section = False

            elif (nodes_section):
                if line.strip():
                    if (len(line.split()[1:]) != 0):
                        values = [float(val) for val in line.split()[1:] + [1]]
                        vertices.append(values)
            elif (faces_section):
                if line.strip():
                    if (len(line.split()[1:]) == 7): #only get faces of triangles, not simple lines or piramids
                        values = [int(val) - 1 for val in line.split()[-3:]]
                        faces.append(values)
        self.object = Object3D(self.render, vertices, faces)

    def find_type(self):
        print(self.path)
        last_dot_index = self.path.rfind('.')
        if (last_dot_index != -1):
            extension = self.path[last_dot_index:]
            if (extension.lower() == '.msh'):
                if (self.file.split('\n')[1] == '2.2 0 8'):
                    self.type = 'MSH 2.2'
                elif(self.file.split('\n')[1] == '4.1 0 8'):
                    self.type = 'MSH 4.1'
                else:
                    self.type = 'Unknown'
                    print('Not a supported msh file version')
            elif (extension.lower() == '.obj'):
                self.type = 'OBJ'
            else: # Add more file types as needed
                self.type = 'Unknown'
                print('Not a supported file extention')
        else:
            self.type = 'Not found'
            print('No file extension found.')


    def read_file(self):
         with open(self.path, 'r') as f:
            self.file = f.read()