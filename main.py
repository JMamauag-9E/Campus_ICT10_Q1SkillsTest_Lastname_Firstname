from pyscript import display, document

def ordering_summary(e):
    item1 =  document.getElementById('menu1')
    item2 = document.getElementById('menu2')
    item3 =  document.getElementById('menu3')
    item4 = document.getElementById('menu4')
    item5 =  document.getElementById('menu5')
    n = document.getElementById('name').value
    a = document.getElementById('address').value
    c = document.getElementById('contact').value

    total = (float(item1.value) * item1.checked + 
             float(item2.value) * item2.checked + 
             float(item3.value) * item3.checked +
             float(item4.value) * item4.checked +
             float(item5.value) * item5.checked)

    display(f'Order For: {n}', target='output')
    display(f'You live in: {a}', target='output')
    display(f'Your phone number is: {c}', target='output')
    display(f'Your price is {total} pesos.', target='output')