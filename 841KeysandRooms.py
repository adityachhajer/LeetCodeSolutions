class Solution:
    def solvee(self,rooms,visited,curr):
        if visited[curr]==True:
            return
        visited[curr]=True
        for i in range(len(rooms[curr])):
            self.solvee(rooms, visited, rooms[curr][i])

    def solve(self,rooms):
        a=len(rooms)
        visited=[False]*a
        visited[0]=True
        for i in range(0,1):
            for j in range(len(rooms[i])):
                self.solvee(rooms,visited,rooms[i][j])
        if False in visited:
            return False
        return True

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        return self.solve(rooms)