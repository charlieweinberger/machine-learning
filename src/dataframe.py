class DataFrame():
    
    def __init__(self, data_dict, column_order):
        self.data_dict = data_dict
        self.columns = column_order

        self.column_keys = list(data_dict.keys())
        self.column_values = list(data_dict.values())

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