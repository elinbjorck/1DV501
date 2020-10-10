import table as tbl

d = {"Ella" : 39, "Owen" : 40, "Fred" : 44, "Zoe" : 41, "Adam" : 27, "Ceve" : 37, "Adam" : 27, "Ceve" : 37}

root = tbl.new_empty_root()
for k,v in d.items():
    tbl.add(root,k,v)

print("To_string: ",tbl.to_string(root))     # { (Adam,27) (Ceve,37) (Ella,39) (Fred,44) (Owen,40) (Zoe,41) }
print("Get(Owen):", tbl.get(root,"Owen"))    # 40
print("Get(Jonas):", tbl.get(root,"Jonas"))  # None

print("Size:",tbl.count(root))               # 6
print("Max depth:", tbl.max_depth(root))     # 3
pairs = tbl.get_all_pairs(root)              
print("All pairs: ",pairs)                   # [('Adam', 27), ('Ceve', 37), ('Ella', 39), ('Fred', 44), ('Owen', 40), ('Zoe', 41)]

tbl.add(root,"AA",1)
tbl.add(root,"AAA",2)
tbl.add(root,"AAAA",3)
tbl.add(root,"AAAAA",4)

print("Size:",tbl.count(root))              # 10
print("Max depth:", tbl.max_depth(root))    # 6
print("To_string: ",tbl.to_string(root))    # { (AA,1) (AAA,2) (AAAA,3) (AAAAA,4) (Adam,27) (Ceve,37) (Ella,39) (Fred,44) (Owen,40) (Zoe,41) }

    
