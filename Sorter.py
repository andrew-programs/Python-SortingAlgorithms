from dataclasses import dataclass

@dataclass
class Sorter:
    def selectionSort(self, listOfInts: list[int], option: str="ascending") -> list[int]:
        sortedList = []

        if option.lower() == "ascending":
            while len(listOfInts) != 0:
                compareInteger = listOfInts[0]

                for integer in listOfInts:
                    if integer < compareInteger:
                        compareInteger = integer
                
                
                listOfInts.remove(compareInteger)
                sortedList.append(compareInteger)
        if option.lower() == "descending":
            while len(listOfInts) != 0:
                compareInteger = listOfInts[0]

                for integer in listOfInts:
                    if integer > compareInteger:
                        compareInteger = integer
                
                
                listOfInts.remove(compareInteger)
                sortedList.append(compareInteger)

        return sortedList
    
def main() -> None:
    sorter = Sorter()
    print(sorter.selectionSort([23, 12, 87, 63, 54]))

if __name__ == "__main__":
    main()