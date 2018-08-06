1. Install semua requirements dengan pip install -r requirements.txt

# Tasks
Task-task sudah terdapat pada folder-folder, Kamu dapat membaca dan memodifikasinya.

#Task 1 A Topic Modelling Klasifikasi
1. Jalankan program dengan jupyter notebook atau dengan spyder.
2. Jalankan program satu persatu untuk dapat melihat hasil dari setiap proses.
3. Akan didapatkan hasil prediksi dengan menggunakan algoritma Naive Bayes Classifier dan Support Vector Machine yang sudah di evaluasi dengan data sendiri dan cross validation.

#Task 1 B Topic Modelling Unsupervised Learning
1. Jalankan program dengan jupyter notebook atau dengan spyder.
2. Jalankan program satu persatu untuk dapat melihat hasil dari setiap proses.
3. Akan didapatkan hasil topic modelling dengan algoritma Non-negative Matrix Factorization (NMF) dan juga Latent Dirichlet Allocation (LDA) yang sudah di evaluasi.

#Task 2
1. Jalankan program dengan jupyter notebook atau dengan spyder.
2. Jalankan program satu persatu untuk dapat melihat hasil dari setiap proses.
3. Lalu pada pembuatan keywords dengan Term Frequency dan TF-IDF dapat ditambah document yang ingin dilihat keywordsnya dengan menambahkanya secara manual.
4. Misalkan:
	 document5 = tb(' '.join(df['stopword'][4]))
	 bloblist = [document1,document2,document3,document4,document5]
5. Akan didapatkan hasil dari algoritma tersebut dalam menentukkan keywords dari setiap contentnya.

#Task 3
1. Jalankan program dengan jupyter notebook atau dengan spyder.
2. Jalankan program satu persatu untuk dapat melihat hasil dari setiap proses.
3. Lalu pada pembuatan keywords dengan algoritma RAKE dapat ditambah document yang ingin dilihat title dengan menambahkanya secara manual.
4. Misalkan:
	 r.extract_keywords_from_text(Con[1])
	 atau
	 r.extract_keywords_from_text(Con[2])
	 dan seterusnya.
5. Akan didapatkan hasil dari algoritma RAKE tersebut dalam menentukkan title berdasarkan frasa keywords terpenting dari setiap contentnya.
