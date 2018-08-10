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
'''
inp = open('data/vaccines')
print('Adding vaccines')
for data in inp:
    if '#' in data: continue
    data = data.strip().split(',')
    c = data[0].split('/')
    m = data[1].split('/')
    v = data[2].split('/')
    ds = [d.split('/') for d in data[3:]]
    vac = Vaccine()
    vac.vaccine = v[0]
    vac.vaccine_en = v[1]
    vac.manufacturer = m[0]
    vac.manufacturer_en = m[1]
    vac.country = c[0]
    vac.country_en = c[1]
    vac.save()
    for d in ds:
        q = Disease.objects.filter(disease=d[0], disease_en=d[1])
        if len(q) == 0:
            dis = Disease()
            dis.disease = d[0]
            dis.disease_en = d[1]
            dis.save()
        dis_id = Disease.objects.get(disease=d[0], disease_en=d[1])
        vac.disease.add(dis_id)
    vac.save()
inp.close()




















