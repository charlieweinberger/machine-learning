class DataFrame():
    
    def __init__(self, data_dict, column_order):
        self.data_dict = data_dict
        self.columns = column_order

        self.column_keys = list(self.data_dict.keys())
        self.column_values = list(self.data_dict.values())

        self.num_rows = len(self.column_values)
        self.num_cols = len(self.column_values[0])
    
    def copy(self):
        return DataFrame(self.data_dict, self.columns)

    def to_array(self):
        c = self.copy()

        ans = [[0 for num2 in range(c.num_rows)] for num in range(c.num_cols)]
                
        for m in range(c.num_cols):
            for n in range(c.num_rows):
                ans[m][n] = c.column_values[n][m]
        
        return ans
    
    def select_columns(self, name_list):
        c = self.copy()

        dict_ans = {}
        for name in name_list:
            for key, value in c.data_dict.items():
                if name == key:
                    dict_ans[name] = value

        return DataFrame(dict_ans, list(dict_ans.keys()))

    def select_rows(self, row_indices):
        c = self.copy()

        dict_ans = {}
        for key, value in c.data_dict.items():
            dict_ans[key] = [value[index] for index in range(len(value)) if index in row_indices]

        return DataFrame(dict_ans, list(dict_ans.keys()))
    
    def apply(self, name, f):
        c = self.copy()

        row = []
        for key, value in c.data_dict.items():
            if key == name:
                row = value
        
        row = [f(n) for n in row]
        c.data_dict[name] = row

        return c
    
    @classmethod
    def from_array(self, arr, columns):
        
        dict_ans = {}
        for thing in columns:
            dict_ans[thing] = []

        index = 0
        for key, value in dict_ans.items():
            for person in arr:
                value.append(person[index])
            index += 1  

        return DataFrame(dict_ans, columns)

    def convert_row_from_array_to_dict(self, arr):
        c = self.copy()

        dict_ans = {c.columns[elem_index]:arr[elem_index] for elem_index in range(len(arr))}

        return dict_ans

    def select_rows_where(self, f):
        c = self.copy()

        dict_ans = {c.columns[index]:[] for index in range(len(c.columns))}

        people_dict_list = [c.convert_row_from_array_to_dict(person) for person in c.to_array()]
        
        for person_dict in people_dict_list:
            if f(person_dict):
                for key, value in person_dict.items():
                    dict_ans[key].append(value)
        
        return DataFrame(dict_ans, c.columns)
    
    def order_by(self, this_key, ascending):
        c = self.copy()

        people_dict_list = [c.convert_row_from_array_to_dict(person) for person in c.to_array()]
        people_dict_list.sort(reverse = not ascending, key = lambda row: row[this_key])

        values = [list(person_dict.values()) for person_dict in people_dict_list]

        dict_ans = {c.columns[index]:[] for index in range(len(c.columns))}

        for key_index in range(len(c.columns)):
            for person_list in values:
                dict_ans[c.columns[key_index]].append(person_list[key_index])

        return DataFrame(dict_ans, c.columns)