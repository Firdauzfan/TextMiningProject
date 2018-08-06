# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 13:31:46 2018

@author: Firdauz_Fanani
"""

import csv,numpy,pandas,nltk
from nltk import sent_tokenize, word_tokenize, pos_tag

from rake_nltk import Rake

#%%

#Baca data CSV dengan pandas
df = pandas.read_csv('../data/ds_asg_data.csv')

head = df.head()
print (head)

#View berdasar label
groupby= df.groupby('article_topic').size()
print (groupby)

Id=df['article_id']
Con= df['article_content']
Topic = df['article_topic']

#%%

#Cek data dan normalisasi

#cek bila ada yang kosong
cek_bentuk= df['article_content'].shape
cek_null=df.isnull()
cek_jumlah_null=df.isnull().sum()

print (cek_bentuk)
print (cek_null)
print (cek_jumlah_null)

#Drop/Hapus data yang kosong
modifiedData = df.dropna()

#Cek data apakah masih ada yang null
cek_bentuk= modifiedData['article_content'].shape
cek_null=modifiedData.isnull()
cek_jumlah_null=modifiedData.isnull().sum()

#Save Data yang sudah dimodifikasi ->opsional
modifiedData.to_csv('modifiedData.csv',index=False)

#Baca data CSV dengan pandas
df = pandas.read_csv('modifiedData.csv')
Id=df['article_id']
Con= df['article_content']
Topic = df['article_topic']

#%%

#Pembuatan Judul dengan algoritma Rake dan didapatkan frasa yang berisi kata-kata penting dari content

r = Rake()

r.extract_keywords_from_text(Con[0])

Judul1=r.get_ranked_phrases()[0] # Dapatkan frasa judul pertama
Judul2=r.get_ranked_phrases()[1] # Dapatkan frasa judul kedua

print(Judul1)
print(Judul2)