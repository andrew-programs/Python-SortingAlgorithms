class Sorter:
    # Selection sorting method. Time complexity : O(n^2)
    def selectionSort(self, intList: list[int], option: str="ascending") -> list[int]:
        """
        Sorts out a list using selection sorting method.
        Time Complexity : O(n^2) 
        """
        
        for index in range(len(intList)):
            minimumIntegerIndex = index

            assert option == "ascending" or option == "descending", "option should be either ascending or descending"

            for secondIndex in range(len(intList)):
                if index < secondIndex:
                    if option.lower() == "ascending":
                        if intList[secondIndex] < intList[minimumIntegerIndex]:
                            minimumIntegerIndex = secondIndex
                    if option.lower() == "descending":
                        if intList[secondIndex] > intList[minimumIntegerIndex]:
                            minimumIntegerIndex = secondIndex
            
            intList.insert(index, intList.pop(minimumIntegerIndex))
        return intList
    
def main() -> None:
    sorter = Sorter()
    print(sorter.selectionSort([23, 12, 87, 63, 54, 84, 79, 28, 11, 1, 0, -12, 32, -40], "ascending"))

if __name__ == "__main__":
    main()