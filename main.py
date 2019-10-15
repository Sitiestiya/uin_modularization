nama = 'Siti Estiya Pujiningtiyas'
program = 'Gerak Lurus'

print(f'Program{program} oleh {nama}')

jarak = 1000
waktu = 5 * 60
kecepatan = jarak / waktu

print(f'Jarak = {jarak/1000}km ditempuh dalam waktu = {waktu/60}menit')
print(f'Sehingga kecepatan = {kecepatan} m/s')

jarak = 5000
waktu = 8 * 60
kecepatan = jarak / waktu

print(f'Jarak = {jarak/1000}km ditempuh dalam waktu = {waktu/60}menit')
print(f'sehingga kecepatan = {kecepatan} m/s')

def hitung_massajenis(massa, volume) :
    massajenis = massa / volume
    print(f'massa = {massa/1000}kg dalam sebuah volume = {volume/1000}meterkubik')
    print(f'Sehingga massajenis = {massajenis} kg/m**')
    return massajenis

#massa
#volume
massajenis = hitung_massajenis(1000, 3000)
kecepatan = hitung_massajenis(20000, 5)

