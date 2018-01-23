class WordCounter :
    def __init__(self):
        self.lines = []
        self.result = {}

    def load(self, file_path):
        with open(file_path, 'r') as file:
            self.lines = file.readlines()

    def save(self, file_path):
        with open(file_path, 'w') as file:
            file.write('-------------------------------\n')
            file.write('분석 결과 (단어 : 횟수)')
            file.write('-------------------------------\n')
            for word, count in self.result.items():
                file.write('%s : %d'%(word, count))
            file.write('-------------------------------\n')

    def print(self):
        print('-------------------------------')
        print('분석 결과 (단어 : 횟수)')
        print('-------------------------------')
        for word, count in self.result.items():
            print('%s : %d' % (word, count))
        print('-------------------------------')


    def analysis(self):
        if not self.lines :
            raise Exception('분석할 데이터가 없습니다.')

        for line in self.lines:
            line = line.strip()
            words = line.split(' ')
            for word in words:
                if not word in self.result.keys():
                    self.result[word] = 0

                self.result[word] += 1