import sys

class Heap:
    def __init__(self, N):
        self.heap = [0]
        self.length = 0
        self.N = N
    
    def insertNode(self, data):
        self.heap.append(data)
        self.length += 1
        
        if self.length > self.N:
            self.deleteNode()
            
        else:
            self.Heapify()
            
    def deleteNode(self):
        if self.heap[1] < self.heap[self.length]:
            self.heap[1], self.heap[self.length] = self.heap[self.length], self.heap[1]
            
        self.heap.pop()
        self.length -= 1
        
        index = 1
        
        while index <= (self.length//2):
            
            minIndex = 0
            minValue = 0
            
            if (index * 2) <= self.length and (index * 2 + 1) <= self.length and self.heap[index*2 + 1] < self.heap[index*2]:
                minIndex = index*2 + 1
                minValue = self.heap[index*2 + 1]
            
            else:
                minIndex = index*2
                minValue = self.heap[index*2]
        
            if self.heap[index] > minValue:
                self.heap[index], self.heap[minIndex] = self.heap[minIndex], self.heap[index]
                index = minIndex
            
            else:
                break
        
    def Heapify(self):
        index = self.length
        
        while index > 1:
            if self.heap[index] < self.heap[index // 2]:
                self.heap[index//2], self.heap[index] = self.heap[index], self.heap[index//2]
            
            else:
                break
                
            index = index // 2
                
    def getTop(self):
        return self.heap[1]
    
    def printHeap(self):
        print(self.heap, self.length)
            
    
N = int(input().strip())

heap = Heap(N)

for line in sys.stdin:
    for _ in line.strip().split():
        heap.insertNode(int(_))
            
print(heap.getTop())
