class DataFrame():
    
    def __init__(self, data_dict, column_order):
        self.data_dict = data_dict
        self.columns = column_order
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

    @classmethod
    def from_array(cls, arr, columns):
        
        dict_ans = {}        
        for thing in columns:
            dict_ans[thing] = []
        
        index = 0
        for key, value in dict_ans.items():
            value += [person[index] for person in arr]
            index += 1
        
        return DataFrame(dict_ans, columns)
    
    @classmethod
    def from_csv(cls, path_to_csv, header=True):
        
        with open(path_to_csv, "r") as file:
            
            file_str = file.read()
            big_list = file_str.split("\n")

            arrays = [string.split(",  ") for string in big_list]
            arrays = arrays[1:len(arrays)]

            columns = big_list[0].split(", ")
            
            return DataFrame.from_array(arrays, columns)
    
    def create_interaction_terms(self, dependent_variable):
        
        dependent_variable_index = self.columns.index(dependent_variable)
        dependent_variable_value = self.data_dict[dependent_variable]
        del self.data_dict[dependent_variable]
        del self.columns[dependent_variable_index]

        new_columns = []
        for i in range(len(self.columns)):
            for j in range(len(self.columns)):
                if i < j:
                    new_column = self.columns[i] + ' * ' + self.columns[j]
                    new_columns.append(new_column)
        self.columns += new_columns
        
        for i in range(len(self.columns)):
            
            key_string = self.columns[i]
            key_list = key_string.split(' * ')

            value_list = []
            for j in range(len(self.column_values[0])):
                value = 1
                for key in key_list:
                    value *= self.data_dict[key][j]
                value_list.append(value)
            
            self.data_dict[key_string] = value_list

        self.data_dict[dependent_variable] = dependent_variable_value
        
        self.column_values = list(self.data_dict.values())
        self.num_rows = len(self.column_values)
        self.num_cols = len(self.column_values[0])

        return self
    
    def create_dummy_variables(self, column_name):
        column_index = self.columns.index(column_name)
        column_list = self.column_values[column_index]
        
        # only works if one of the elements in column_list has all the condiments.
        condiment_keys_lengths = [len(elem) for elem in column_list]
        for len_index in range(len(condiment_keys_lengths)):
            if condiment_keys_lengths[len_index] == max(condiment_keys_lengths):
                condiments = column_list[len_index]

        columns = self.columns
        del columns[column_index]
        for condiment in condiments[::-1]:
            columns.insert(column_index, condiment)

        numbers_list = []
        for elem in column_list:
            
            to_add = [0 for _ in range(len(condiments))]
            for condiment in elem:
                
                for n in range(len(condiments)):
                    if condiment == condiments[n]:
                        to_add[n] = 1

            numbers_list.append(to_add)
        
        column_values = self.column_values
        del column_values[column_index]
        all_condiment_nums = [[thing[n] for thing in numbers_list] for n in range(column_index)]
        for thing in all_condiment_nums[::-1]:
            column_values.insert(column_index, thing)

        data_dict = {}
        for i in range(len(column_values)):
            key = columns[i]
            value = column_values[i]
            data_dict[key] = value

        return DataFrame(data_dict, columns)