'''  def not_perfect(self) -> None:
        """Introduce random wall removals to create loops
        and make the maze imperfect."""
        if self.perfect is False:
            print("ayyy")
            
            unvisited: list[tuple[int, int]] = []
            visited: list[tuple[int, int]] = []
            n_dir: str = ""
            dirs: list[str] = ['E', 'W', 'N', 'S']
            w: int = self.width
            h: int = self.height
﻿
            wall: int = int(h*w*0.2)
            for r in range(h):
                for c in range(w):
                    if self.cells[r][c].is_visited:
                        visited.append((c, r))
﻿
            for r in range(h):
                for c in range(w):
                    if not self.cells[r][c].is_visited:
                        unvisited.append((c, r))
            
            while wall != 0 and unvisited:
                x: int
                y: int
﻿
                x, y = random.choice((unvisited))
                unvisited.remove((x, y))
                
                dict_42: dict[str, bool] = {}
                for d in dirs:
                    x_m, y_m, n_dir, m_dir= self.direction[d]
                    n_x, n_y = x+m_x, y+m_y
                    if (n_x, n_y) in visited:
                        dict_42.update({n_dir: False})
                    else:
                        dict_42.update({n_dir: True})
                
                dirs = random.shuffle(dirs)
                if self.cells[y][x].wall[dirs]:
                    found: bool = True
                    i: int = 0
                    while i < 4 and found:
                        next_dir = dirs[i]
                        if (dict_42[next_dir] is True
                            and (x != 0 or d != 'W')
                            and (x != w-1 or d != 'E')
                            and (y != 0 or d != 'N')
                            and (y != h-1 or d != 'S')):
                            self.cells[y][x].walls[d] = False
                            wall -= 1
                            found = False
                        i += 1
