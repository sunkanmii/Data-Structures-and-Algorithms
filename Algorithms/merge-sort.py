class MergeSort:

    def sort(self, arr):
        if len(arr) > 1:
            r = len(arr) // 2
            left = arr[:r]
            right = arr[r:]
        
            self.sort(left)
            self.sort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

newArr = [1, 34, 12, 3, 4, 6, 5, 10]
mergeSortObj = MergeSort()
mergeSortObj.sort(newArr)
print(newArr)
