def print_info(**args):
    print(f"이름 : {args['name']} 나이 : {args['age']} 성별 : {args['sex']}")

print_info(name = "황태영", age = 20, sex = "남자")