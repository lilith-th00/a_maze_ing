def not_perfect(self) -> None:
        """Introduce random wall removals to create loops
        and make the maze imperfect."""
        if self.perfect is False:
            
            unvisited: list[tuple[int, int]] = []
            visited: list[tuple[int, int]] = []
            dirs: list[str] = ['E', 'W', 'N', 'S']
            w: int = self.width
            h: int = self.height

            wall: int = int(h*w*0.15)

            for r in range(h):
                for c in range(w):
                    found: bool = True
                    i: int = 0
                    while i < 4 and found:
                        if not self.cells[r][c].walls[dirs[i]]:
                            found = False
                        i += 1
                    if found:
                        visited.append((c, r))
                    else:
                        unvisited.append((c, r))
            
            while wall > 0 and unvisited:
                x: int
                y: int
                if not unvisited:
                    break
                x, y = random.choice((unvisited))
                unvisited.remove((x, y))
                dict_42: dict[str, bool] = {}
                count: int = 0
                for d in dirs:
                    m_x, m_y, n_dir, m_dir= self.direction[d]
                    n_x, n_y = x + m_x, y + m_y
                    if 0 <= n_x < w and 0 <= n_y < h:
                        if (n_x, n_y) in visited:
                            dict_42[n_dir] = False
                        else:
                            dict_42[n_dir] = True
                    
                    else:
                        dict_42[n_dir] = False
                    if not self.cells[y][x].walls[n_dir]:
                        count += 1

                random.shuffle(dirs)
                found: bool = True
                i: int = 0
                while i < 4 and found:
                    next_dir = dirs[i]
                    m_x, m_y, n_dir, m_dir = self.direction[next_dir]
                    n_x, n_y = x + m_x, y + m_y
                    if 0 <= n_x < w and 0 <= n_y < h:
                        if (self.cells[n_y][n_x].walls[m_dir]
                                and dict_42[next_dir]
                                and count <= 2):
                                count2: int = 0
                                for d in dirs:
                                    if not self.cells[n_y][n_x].walls[d]:
                                        count2 += 1
                                if count2 <= 2:
                                    self.cells[y][x].walls[n_dir] = False
                                    self.cells[n_y][n_x].walls[m_dir] = False
                                    wall -= 1
                                    found = False
                    i += 1


