#                                   LIST COMPREHENSION
# val=[1,2,3,4,5,6,7]
# sq_val=[x*x for x in val]
# print(sq_val)

# sq_val_check=[x if x>=4 else 0 for x in val]
# print(sq_val_check)

# sq_val_check1=[x for x in val if x>=4]
# print(sq_val_check1)


#                                       DICT COMPREHENSION
cart={'pen':40.50,'phone':25000.00,'table':5499.99,'lamp':2560.60,'kettle':1500.00,'bag':650.20}
cart1={k:round(v) for (k,v) in cart.items()}
print(cart1)

cart2={k:round(v) for (k,v) in cart.items() if v>1000}
print(cart2)

cart3={k:round(v*0.9) if v>20000 else v for (k,v) in cart.items()}
print(cart3)

def furn_dis(k,v):
    if k=='table' or k=='kettle':
        v*=.95
    return v

cart4={k:furn_dis(k,v) for (k,v) in cart.items()}
print(cart4)
