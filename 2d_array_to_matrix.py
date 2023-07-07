class Main:
    @staticmethod
    def main():
        matrix = [[1,2],[3,4],[4,5]]

        for i in range(3):
            for j in range(2):
                print("matrix[{}][{}]={}".format(i, j, matrix[i][j]))


Main.main()