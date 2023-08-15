import readchar
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_laberinto(laberinto):
    limpiar_pantalla()
    for row in laberinto:
        print(''.join(row))

def main_loop(laberinto, start, end):
    px, py = start
    
    while (px, py) != end:
        laberinto[py][px] = '\U0001F92B'
        print_laberinto(laberinto)
        laberinto[py][px] = '.'
        
        key = readchar.readkey()

        if key == readchar.key.UP:
            new_py = py - 1
            if new_py >= 0 and laberinto[new_py][px] != '#':
                py = new_py
        elif key == readchar.key.DOWN:
            new_py = py + 1
            if new_py < len(laberinto) and laberinto[new_py][px] != '#':
                py = new_py
        elif key == readchar.key.LEFT:
            new_px = px - 1
            if new_px >= 0 and laberinto[py][new_px] != '#':
                px = new_px
        elif key == readchar.key.RIGHT:
            new_px = px + 1
            if new_px < len(laberinto[py]) and laberinto[py][new_px] != '#':
                px = new_px

    laberinto[py][px] = '\U0001F92B'
    print_laberinto(laberinto)
    print("¡Has llegado al final, FELICIDADES!")

def parse_laberinto(laberinto_str):
    return [list(row) for row in laberinto_str.split("\n")]

def create_laberinto(end):
    laberinto_str = """
..###################
......#.#...........#
#.#.#.#.#.###.#.###.#
#.#.#...#.#...#.#...#
#.#########.###.#.###
#.........#.#...#...#
#.###########.#####.#
#.....#.......#.#.#.#
#.#####.#######.#.#.#
#.#.#.#.....#.#.....#
#.#.#.#####.#.###.#.#
#.#.#.......#.#...#.#
#.#.#.#####.#.###.###
#.......#...#.....#.#
#.#####.###.#.###.#.#
#.#.#.#.#...#.#.#.#.#
#.#.#.#.#####.#.###.#
#...#...#.....#...#.#
###.#####.#.#.#.###.#
#...#.....#.#.......
###################.
"""
    laberinto_str = laberinto_str.replace("end", str(end[0]) + ", " + str(end[1]))
    laberinto_str = laberinto_str.strip()
    return parse_laberinto(laberinto_str)

def main():
    start = (0, 0)
    end = (9, 9)
    maze = create_laberinto(end)
    main_loop(maze, start, end)

if __name__ == "__main__":
    main()
