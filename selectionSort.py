class Solution: 
    def select(self, arr, i):
        size = len(arr)
        min_idx = i
        
        for j in range(i + 1, size):
            if arr[j] < arr[min_idx]:
                min_idx = j
        return min_idx
    
    def selectionSort(self, arr,n):
        
        for i in range(n - 1):
            num = self.select(arr, i)
            if i != num:
                arr[num], arr[i] = arr[i], arr[num]