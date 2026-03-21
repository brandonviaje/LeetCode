from collections import defaultdict

class Solution:
    def gridIllumination(self, n, lamps, queries):
        result = []
        
        rows = defaultdict(int)
        cols = defaultdict(int)
        posDiag = defaultdict(int)  # row + col
        negDiag = defaultdict(int)  # row - col
        lamps_on = set()
        
        # turn on lamps
        for r, c in lamps:

            # skip if lamp is already on
            if (r, c) in lamps_on:
                continue

            # add to sets
            lamps_on.add((r, c))
            rows[r] += 1
            cols[c] += 1
            posDiag[r+c] += 1
            negDiag[r-c] += 1
        
        for r, c in queries:

            # check if illuminated
            if rows[r] > 0 or cols[c] > 0 or posDiag[r+c] > 0 or negDiag[r-c] > 0:
                result.append(1)
            else:
                result.append(0)
            
            # turn off lamp at (r, c) and adjacent cells
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    nr, nc = r+dr, c+dc

                    # turn off adjacent lamps from the curr origin
                    if (nr, nc) in lamps_on:
                        lamps_on.remove((nr,nc))
                        rows[nr] -= 1
                        cols[nc] -= 1
                        posDiag[nr+nc] -= 1
                        negDiag[nr-nc] -= 1
                        
        return result