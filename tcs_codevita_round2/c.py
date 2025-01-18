def rotate_left(cube):
    new_cube = [face[:] for face in cube]
    new_cube[2] = cube[5]  # left <- right
    new_cube[5] = cube[3]  # right <- front
    new_cube[3] = cube[4]  # front <- base
    new_cube[4] = cube[2]  # base <- left
    new_cube[1] = [row[::-1] for row in cube[1]]  # rotate back side
    return new_cube

def rotate_right(cube):
    new_cube = [face[:] for face in cube]
    new_cube[2] = cube[3]  # left <- front
    new_cube[5] = cube[4]  # right <- back
    new_cube[3] = cube[5]  # front <- right
    new_cube[4] = cube[2]  # base <- left
    new_cube[1] = [row[::-1] for row in cube[1]]  # rotate back side
    return new_cube

def rotate_front(cube):
    new_cube = [face[:] for face in cube]
    new_cube[0] = cube[5]  # front <- base
    new_cube[1] = cube[3]  # back <- top
    new_cube[5] = cube[2]  # base <- back
    new_cube[2] = cube[0]  # top <- front
    new_cube[4] = [row[::-1] for row in cube[4]]  # left rotates
    new_cube[5] = [row[::-1] for row in cube[5]]  # right rotates
    return new_cube

def rotate_back(cube):
    new_cube = [face[:] for face in cube]
    new_cube[0] = cube[2]  # front <- top
    new_cube[1] = cube[5]  # back <- base
    new_cube[5] = cube[3]  # back <- front
    new_cube[3] = cube[4]  # base <- back
    return new_cube

def read_cube_from_input():
    N, K = map(int, input().split())
    
    cube = []
    for _ in range(6):
        face = [input().split() for _ in range(N)]
        cube.append(face)
    
    return cube, N, K


def apply_rotations(cube, K, rotations):
    for rotation in rotations:
        if rotation == 'rotate left':
            cube = rotate_left(cube)
        elif rotation == 'rotate right':
            cube = rotate_right(cube)
        elif rotation == 'rotate front':
            cube = rotate_front(cube)
        elif rotation == 'rotate back':
            cube = rotate_back(cube)
    
    return cube

# Mapping of side names to their respective indices
side_map = {
    'top': 3,
    'bottom': 1,
    'front': 4,
    'back': 2,
    'left': 5,
    'right': 6
}

def get_final_color(cube, side, row, col):
    # Get the side index from the map
    side_index = side_map[side]
    # Return the color of the chosen square from the cube
    return cube[side_index-1][row-1][col-1]

def main():
    cube, N, K = read_cube_from_input()
    
    rotations = [input().strip() for _ in range(K)]
    
    cube = apply_rotations(cube, K, rotations)
    
    side, row, col = input().split()
    row = int(row)
    col = int(col)
    
    result = get_final_color(cube, side, row, col)
    
    print(result)

if __name__ == "__main__":
    main()
