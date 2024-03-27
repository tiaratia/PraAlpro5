#!/usr/bin/env python
# coding: utf-8

# In[25]:


# nomor 7.4
def cari_kata_terpendek_dan_terpanjang(kalimat):
    kata_kalimat = kalimat.split()
    
    kata_terpendek = kata_kalimat[0]
    kata_terpanjang = kata_kalimat[0]
    
    for kata in kata_kalimat:
        if len(kata) < len(kata_terpendek):
            kata_terpendek = kata
        elif len(kata) > len(kata_terpanjang):
            kata_terpanjang = kata
    
    return kata_terpendek, kata_terpanjang

kalimat = input("ed snakes and a black frog in the pool:")
terpendek, terpanjang = cari_kata_terpendek_dan_terpanjang(kalimat)

print("Terpendek:", terpendek)
print("Terpanjang:", terpanjang)


# In[22]:


#nomor 7.2
def hitung_frekuensi_kata(kalimat, kata):
    kata_kalimat = kalimat.split()
    frekuensi = 0
    for k in kata_kalimat:
        if k.lower() == kata.lower():
            frekuensi += 2
            
    return frekuensi
kalimat = "Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan"
kata_dicari = "makan"
print(f"{kata_dicari} ada {hitung_frekuensi_kata(kalimat, kata_dicari)} buah")


# In[26]:


# nomor 7.3
def hapus_spasi_berlebihan(string):
    return ' '.join(string.split())

kalimat = "saya tidak suka memancing ikan "
hasil = hapus_spasi_berlebihan(kalimat)
print("Hasil setelah menghapus spasi berlebih:", hasil)



# In[ ]:




