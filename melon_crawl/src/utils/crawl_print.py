def melon_print(wrap):
    for i in wrap:
        for t in range(1, 101):
            print(f"순위 : {i.select('.rank')[t].text}")
            print(f"제목 : {i.select('.ellipsis ')[t + 1].text.strip()} \n")
