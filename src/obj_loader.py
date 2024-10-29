import numpy as np

def parse_obj(file_path, scale):
    vertices = []
    faces = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith('#') or not line:
                continue

            parts = line.split()
            if parts[0] == 'v':
                vertex = list(map(float, parts[1:4]))
                vertices.append(vertex)

            elif parts[0] == 'f':
                face = [int(p.split('/')[0]) - 1 for p in parts[1:]]
                faces.append(face)

    return np.array(vertices, dtype=float) * scale, np.array(faces, dtype=int)
