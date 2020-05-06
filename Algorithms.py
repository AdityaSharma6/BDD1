import random
class dictionary_dimension_conversion():
    def __init__(self, dictionary=None):
        self.dictionary = dictionary

    def dict_conversion(self):
        new_dict = {}
        if self.dictionary == None:
            print("Invalid Dictionary Entry")
            return 
        for key, val in self.dictionary.items():
            summation = sum(list(val.values()))
            new_dict[key] = summation
        return new_dict

    def dict_total(self):
        dictionary = self.dict_conversion()
        return sum(list(dictionary.values()))
    
    def introduce_variation(self, name_array, num_array):
        titles = ["Dresses", "Jackets", "Jeans", "Shirts&Tops", "Shorts", "Sweaters"]
        indices = []

        for i in range(len(name_array)):
            word = name_array[i]
            if word in titles:
                indices.append(i)
            if i == len(name_array) - 1:
                indices.append(i)
        
        
        dresses = [int(num_array[i]*random.uniform(1,1.5)) for i in range(len(num_array)) if i > 1 and i < 17]
        jackets = [int(num_array[i]*random.uniform(1,1.5))  for i in range(len(num_array)) if i > 17 and i < 24]
        jeans = [int(num_array[i]*random.uniform(1,1.5))  for i in range(len(num_array)) if i > 24 and i < 33]
        shirts = [int(num_array[i]*random.uniform(1,1.5))  for i in range(len(num_array)) if i > 33 and i < 41]
        shorts = [int(num_array[i]*random.uniform(1,1.5))  for i in range(len(num_array)) if i > 41 and i < 49]
        sweaters = [int(num_array[i]*random.uniform(1,1.5))  for i in range(len(num_array)) if i > 49 and i <= 54]

        num_array[1] = sum(dresses)
        num_array[17] = sum(jackets)
        num_array[24] = sum(jeans)
        num_array[33] = sum(shirts)
        num_array[41] = sum(shorts)
        num_array[49] = sum(sweaters)
        num_array[0] = num_array[1] + num_array[17] + num_array[24] + num_array[33] + num_array[41] + num_array[49]
        return num_array
        '''
        for i in range(len(indices)-1):
            number = random.uniform(1, 1)
            summation = 0

            for j in range(len(num_array)):
                if j > indices[i] and j < indices[i+1]:
                    num_array[j] = int(num_array[j] * number)
                    summation += num_array[j]
            num_array[i] = summation

        num_array[0] = 0
        summation2 = sum(num_array)
        num_array[0] = summation2
        '''
        #print(num_array)
'''
arr1 = ['Total', 'Dresses', 'I hate this product', 'I love this product', 'I recommend this product to my friends', 'I do not recommend this product to my friends', 'The quality of this product is very bad', 'The quality of this product is very good', 'I waste a lot of money purchasing this product', 'The design is very good', 'I hate the design of this product', 'Do not try this ', 'I am very unhappy about this product', 'I am very happy about this product', 'The style is very good', 'I like the color', 'excellent design', 'Jackets', 'The quality of this product is very bad', 'Do not try this ', 'The quality of this product is very good', 'I like the color', 'I do not recommend this product to my friends', 'I recommend this product to my friends', 'Jeans', 'I am very unhappy about this product', 'I waste a lot of money purchasing this product', 'I do not recommend this product to my friends', 'I hate this product', 'Do not try this ', 'The quality of this product is very good', 'I like the color', 'I recommend this product to my friends', 'Shirts&Tops', 'The quality of this product is very bad', 'I hate this product', 'Do not try this ', 'The quality of this product is very good', 'I like the color', 'I do not recommend this product to my friends', 'I recommend this product to my friends', 'Shorts', 'I do not recommend this product to my friends', 'I love this product', 'The quality of this product is very bad', 'Do not try this ', 'The quality of this product is very good', 'I like the color', 'I recommend this product to my friends', 'Sweaters', 'I hate this product', 'Do not try this ', 'The quality of this product is very good', 'I do not recommend this product to my friends', 'I recommend this product to my friends']
arr2 = [21459, 4497, 777, 0, 392, 1175, 0, 619, 0, 0, 476, 542, 66, 0, 101, 82, 257, 3199, 790, 611, 388, 377, 440, 590, 5564, 396, 361, 1419, 454, 514, 834, 632, 952, 4248, 302, 638, 826, 598, 469, 629, 783, 2273, 298, 394, 230, 427, 290, 265, 367, 1675, 461, 374, 227, 413, 199]
introduce_variation(arr1, arr2)
'''
        




    



if __name__ == "__main__":
    dictionary = {"Dresses": {"I hate this product": 889, "I love this product": 1, "I recommend this product to my friends": 449, "I do not recommend this product to my friends": 1345, "The quality of this product is very bad": 1, "The quality of this product is very good": 709, "I waste a lot of money purchasing this product": 1, "The design is very good": 1, "I hate the design of this product": 545, "Do not try this ": 621, "I am very unhappy about this product": 76, "I am very happy about this product": 1, "The style is very good": 116, "I like the color": 94, "excellent design": 295}, "Jackets": {"The quality of this product is very bad": 904, "Do not try this ": 700, "The quality of this product is very good": 444, "I like the color": 432, "I do not recommend this product to my friends": 504, "I recommend this product to my friends": 676}, "Jeans": {"I am very unhappy about this product": 453, "I waste a lot of money purchasing this product": 414, "I do not recommend this product to my friends": 1624, "I hate this product": 520, "Do not try this ": 588, "The quality of this product is very good": 954, "I like the color": 723, "I recommend this product to my friends": 1089}, "Shirts & Tops": {"The quality of this product is very bad": 346, "I hate this product": 730, "Do not try this ": 945, "The quality of this product is very good": 685, "I like the color": 537, "I do not recommend this product to my friends": 720, "I recommend this product to my friends": 896}, "Shorts": {"I do not recommend this product to my friends": 341, "I love this product": 451, "The quality of this product is very bad": 264, "Do not try this ": 489, "The quality of this product is very good": 332, "I like the color": 304, "I recommend this product to my friends": 420}, "Sweaters": {"I hate this product": 528, "Do not try this ": 428, "The quality of this product is very good": 260, "I do not recommend this product to my friends": 473, "I recommend this product to my friends": 228}}
    test = dictionary_dimension_conversion(dictionary)
    test.dict_conversion()
    test.dict_total()
