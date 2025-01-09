def filter_list(l):
    filtered_list = []  
    for item in l:  # ვათვალიერებთ ყველა ელემენტს მოცემულ სიაში
        if not isinstance(item, str):  # თუ ელემენტი არ არის სტრიქონი
            filtered_list.append(item)  # დავამატოთ იგი ახალ სიაში
    
    return filtered_list  # დავბრუნოთ ახალში ჩადებული არაგამბრიდო ელემენტები
