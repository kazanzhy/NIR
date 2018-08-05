from registry.models import *
'''
inp = open('data/mnames')
print('Adding names')
for firstname in inp:
    obj = Firstname()
    obj.name = firstname
    obj.save()
inp.close()

inp = open('data/fnames')
for firstname in inp:
    obj = Firstname()
    obj.name = firstname
    obj.save()
inp.close()

inp = open('data/patros')
print('Adding patros')
for patro in inp:
    obj = Patronymic()
    obj.name = patro
    obj.save()
inp.close()
'''
inp = open('data/vaccines')
print('Adding vaccines')
for data in inp:
    data = data.strip().split(',')
    vac = Vaccine()
    vac.vaccine = data[2]
    vac.manufacturer = data[1]
    vac.country = data[0]
    vac.save()
inp.close()

inp = open('data/diseases')
print('Adding diseases')
for disease in inp:
    obj = Disease()
    obj.disease = disease
    obj.save()
inp.close()

inp = open('data/localities')
print('Adding localities')
for data in inp:
    data = data.strip().split(',')
    q = Region.objects.filter(region=data[0])
    if len(q) == 0:
        reg = Region()
        reg.region = data[0]
        reg.save()
    reg_id = Region.objects.get(region=data[0])
    q = District.objects.filter(district=data[1], region=reg_id)
    if len(q) == 0:
        dis = District()
        dis.district = data[1]
        dis.region = reg_id
        dis.save()
    dis_id = District.objects.get(district=data[1], region=reg_id)

    q = Locality.objects.filter(locality=data[2], district=data[1])
    if len(q) == 0:
        loc = Locality()
        loc.locality = data[2]
        loc.district = dis_id
        loc.save()
inp.close()
















