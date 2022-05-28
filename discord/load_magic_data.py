def process_data():
    file = open("discord\magic_data.txt", "r", encoding="utf-8")
    lines = file.readlines()
    
    lst = []
    for line in lines:
        # line = line.strip()
        box = {
            "name":None,
            "damage":None,
            "cool_time":None,
            "number":None,
            "shoot_rate":None,
            "exp_range":None,
            "tick_time":None,
            "size":None,
            "rotation":None,
            "duration":None,
            "min_num":None,
            "max_num":None,
            "intensify":None
        }
        
        
        for factor in box.keys():
            id = line.find(f"{factor}=")
            if id == -1:
                continue
            comma_id = line.find(',', id)
            data = line[id + len(factor)+1:comma_id]
            box[factor] = data

        # 해당 마법에서 None인 인자들은 제거 
        keys = []
        for key, value in box.items():
            if value:
                continue
            keys.append(key)
        for key in keys:
            del(box[key])

        lst.append(box)

    return lst

def search_data(magic:str, data_set : list):
    for i in data_set:
        if i["name"] == magic:
            return i
    return "항목 없음"