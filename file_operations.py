import json

class FileOperations:
    def __init__(self):
        self.records = "storage/records.json"
        
    # Create new Chat ID
    def create_chat_id(self):
        open_temp = {}
        new_id = ""
        with open(self.records, "r") as f:
            temp = json.load(f)
        if not temp:
            new_id = "c1"
            return new_id
        else:
            [open_temp] = temp
            last_id = list(open_temp)[-1]
            id_length = len(last_id)
            id_num = int(last_id[1:id_length]) + 1
            new_id = "c" + str(id_num)
            return new_id
    
    def create_chat_details(self, prompt):
        new_id = self.create_chat_id()
        chat_data = {}
        item_data = {}
        with open(self.records, "r") as f:
            temp = json.load(f)
        item_data['prompt'] = prompt
        item_data['file_name'] = f'storage/{new_id}.json'
        chat_data[new_id] = item_data
        # file_path = item_data['file_name']
        # with open(file_path, 'w') as json_file:
        #     pass
        if not temp:
            temp.append(chat_data)
        else:
            [open_list] = temp
            open_list.update(chat_data)
        with open(self.records, "w") as f:
            json.dump(temp, f, indent=4)
        return item_data['file_name']
    
    def search_all_chats(self):
        with open(self.records, 'r') as f:
            temp = json.load(f)
        if not temp:
            print("No chats have been added")
        else:
            [open_list] = temp
            for chat_id in open_list:
                prompt = open_list[chat_id]["prompt"]
                file_name = open_list[chat_id]["file_name"]
                print(f'Chat ID: {chat_id}')
                print(f'Prompt: {prompt}')
                print(f'File name: {file_name}')
                print('\n')
                
        
    
        
    